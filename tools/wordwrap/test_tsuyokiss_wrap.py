#!/usr/bin/env python3
from tsuyokiss_wrap import layout_message, wrap_words


class Units:
    def width(self, text: str) -> int:
        return len(text)


def test_word_boundaries() -> None:
    got = wrap_words("one two three four", Units(), 9, 3)
    assert got.lines == ("one two", "three", "four")
    assert "".join(got.lines).replace(" ", "") == "onetwothreefour"


def test_newlines_are_source_layout() -> None:
    got = wrap_words("alpha\r\nbeta", Units(), 20, 3)
    assert got.lines == ("alpha beta",)


def test_long_word_rejected() -> None:
    try:
        wrap_words("short extraordinarilylong", Units(), 10, 3)
    except ValueError as exc:
        assert "unbreakable" in str(exc)
    else:
        raise AssertionError("long token was split or accepted")


def test_fourth_line_rejected() -> None:
    try:
        wrap_words("aa bb cc dd", Units(), 2, 3)
    except ValueError as exc:
        assert "more than 3" in str(exc)
    else:
        raise AssertionError("four-line message was accepted")


def test_no_avoidable_waste() -> None:
    got = wrap_words("one two three four", Units(), 9, 3)
    words = "one two three four".split()
    consumed = 0
    for line in got.lines[:-1]:
        count = len(line.split())
        consumed += count
        assert len(line + " " + words[consumed]) > got.limit_px


class ScaledUnits:
    def __init__(self, height: int) -> None:
        self.height = height

    def width(self, text: str) -> int:
        return len(text) * self.height


def test_reduce_then_paginate() -> None:
    text = "aa bb cc dd ee ff gg"
    got = layout_message(text, ScaledUnits, 10, nominal_height=3, minimum_height=2, max_lines=3)
    assert got.font_height == 2
    assert len(got.pages) == 2
    assert all(len(page.lines) <= 3 for page in got.pages)
    rebuilt = " ".join(line for page in got.pages for line in page.lines)
    assert rebuilt == text


def test_reduce_avoids_pagination_when_it_fits() -> None:
    text = "aa bb cc dd"
    got = layout_message(text, ScaledUnits, 10, nominal_height=3, minimum_height=2, max_lines=3)
    assert got.font_height == 2
    assert len(got.pages) == 1
    assert " ".join(got.pages[0].lines) == text


if __name__ == "__main__":
    for name, fn in sorted(globals().copy().items()):
        if name.startswith("test_"):
            fn()
            print(f"ok {name}")
