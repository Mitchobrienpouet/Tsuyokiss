#!/usr/bin/env python3
from tsuyokiss_wrap import wrap_words


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


if __name__ == "__main__":
    for name, fn in sorted(globals().copy().items()):
        if name.startswith("test_"):
            fn()
            print(f"ok {name}")
