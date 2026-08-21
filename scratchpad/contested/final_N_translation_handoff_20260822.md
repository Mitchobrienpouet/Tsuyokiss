# Final lane-N translation-stage handoff

This is a translation-stage handoff, not accuracy QC, literary QC, arbitration,
or readthrough. Every row discussed below is present in the permitted filtered
model-source projections. Lane N has no excluded index.

## Delivered scope

| Scene | Exact translated indexes | Rows |
|---|---:|---:|
| SC_N0000_00_N0100_00 | 1-36 | 36 |
| SC_N0100_00_N0100_10 | 1-16 | 16 |
| SC_N0100_20_N0100_50 | 1-13 | 13 |
| SC_N0100_30_N0100_50 | 1-11 | 11 |
| SC_N0100_40_N0100_50 | 1-8 | 8 |
| SC_N0100_50_N0100_60 | 1-20 | 20 |
| SC_N0100_60_N0100_70 | 1-36 | 36 |
| SC_N0100_70_N0100_80 | 1-27 | 27 |
| SC_N0100_80_N0100_90 | 1-67 | 67 |
| SC_N0100_90_N0110_00 | 1-42 | 42 |
| SC_N0110_00_N0110_10 | 1-37 | 37 |
| SC_N0110_10_N0110_20 | 1-39 | 39 |
| SC_N0110_20_N0110_30 | 1-43 | 43 |
| SC_N0110_30_N0110_40 | 1-28 | 28 |
| SC_N0110_40_Z9999_99 | 1-6 | 6 |
| **Total** | **15 exact contiguous sets** | **429** |

## Adopted readings requiring later QC attention

- SC_N0000_00_N0100_00:12 (必殺・乙女顎門割（おとめあぎとわり）)
  - Draft: 「Finishing Move: Otome Jawbreaker!」
  - Basis: the adaptation preserves the source ruby's Otome branding and
    jaw-breaking function while avoiding an unsupported named-franchise
    reference.
  - Defensible alternative: retain the ruby as Otome Agito Wari and supply a
    compact English gloss if project convention requires technique-name
    transliteration.
- SC_N0100_00_N0100_10:1 (お姉さん（←社交辞令）)
  - Draft: 「Morning, young lady (← just being polite). Coming in.」
  - Basis: young lady carries Leo's conspicuously flattering address to Kinu's
    mother, and the arrow preserves the source's self-deflating aside.
  - Defensible alternative: miss (← social courtesy).
- SC_N0100_20_N0100_50:9,11 (えぐりこむ様に打つべし / 打つべし)
  - Draft: 「Drive it in deep--strike!」 / 「Strike! Strike!」
  - Basis: this retains the numbered boxing-instruction cadence and repeated
    imperative without naming an unstated work or character.
  - Defensible alternative: use the deliberately stiffer refrain Thou shalt
    strike! if literary QC needs a stronger parody signal.
- SC_N0100_60_N0100_70:19 (朝デッド)
  - Draft: 「I only went morning-dead for a little bit, and this is what I get.
    It's your fault for doing a half-assed job waking me up!」
  - Basis: morning-dead keeps Kinu's unexplained comic coinage odd instead of
    normalizing it into sleep, unconsciousness, or external lore.
- SC_N0100_60_N0100_70:33 (３倍だ)
  - Draft: 「All right! Triple speed!」
  - Basis: the exact threefold boast remains, with no named pop-culture
    attribution added.
  - Defensible alternative: 「All right! Three times faster!」
- SC_N0100_80_N0100_90:30,50-51 (破っ / 破 / 閃)
  - Draft: 「Hah!」 / 「Hah!」 / 「Shah!」
  - Basis: these are treated as distinct martial cries, preserving the
    strike/counterstrike order without asserting that the single kanji are
    named techniques.
  - Defensible alternative: a consistent transliteration such as Ha! / Sen!,
    if accuracy QC finds the kanji lexical rather than purely kiai.
- SC_N0100_80_N0100_90:32 (いった！)
  - Draft: 「It connected!」
  - Basis: the following permitted lines establish that Otome's kick landed and
    the silver-haired girl jumped backward to soften it. This is not Leo
    crying out in pain.
- SC_N0110_10_N0110_20:32 (死ぬ気があれば自由に生きられる)
  - Draft: 「...If you are willing to die, you can live freely. Those are words
    Gandhi left behind.」
  - Basis: the wording stays close to the in-world Japanese attribution. It
    does not substitute or expand an external quotation.
  - Defensible alternative: If you are prepared to die, you can live freely.
- SC_N0110_30_N0110_40:28 (青臭い)
  - Draft: 「So green. The scent of green youth is everywhere.」
  - Basis: the deliberately repeated green preserves both immaturity and the
    source's smell joke.

## Locked resolutions and continuity

- Official-source readings remain Serebu Tachibana, Ikuzo Tachibana, and
  battleship Hatsuhi; Serebu was not converted to Celeb.
- Silver-haired girl, ???, and Deep voice stay generic in speaker maps until
  their respective source reveals.
- The three wake-up variants remain independent and converge only at
  SC_N0100_50_N0100_60; no branch action was imported into the continuation.
- SC_N0100_70_N0100_80:23 begins with the exact engine control $L.
- The Serebu/Ikuzo/Heizo family relations, Otome fight agency, Kurogane
  bloodline, future-bodyguard plan, hypothetical non-occurring kiss, and
  limited final-coda knowledge remain source-bounded.

## Translation-stage deterministic self-check

PASS:

- duplicate-key-safe JSON parse: 15/15 projections and translations;
- projection SHA-256 unchanged from the preflight table: 15/15;
- projection metadata and declared counts: 15/15;
- exact ordered source-index/translation joins: 429/429;
- per-row Japanese SHA-256: 429/429;
- authoritative engine IDs: 429 unique, with exact scene/index suffixes;
- speaker-map keys, first-occurrence order, and locked English mappings: 15/15;
- dialogue/narration corner-quote wrappers: 429/429;
- engine-control preservation: SC_N0100_70_N0100_80:23 retains exact $L;
- CP932 encodability and forbidden-typography scan: 15/15 translation files.

Unresolved blocking translation issues: **NONE**.
