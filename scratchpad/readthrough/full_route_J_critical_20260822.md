# Critical full-route speed readthrough: route J

## Verdict

**FAIL / BLOCKED.** All 775 permitted rows in all 15 route-J translation files
were read continuously in narrative order, including a fresh route-context
read of the four final-J scenes. The review found `1` blocking finding, `0`
major findings, and `1` minor finding. The critical narrative gate cannot pass
until the false client-gender assertion is corrected and the affected reveal
chain is revalidated and reread. This audit changed no translation, QC,
arbitration, source, projection, exclusion, manifest, configuration, pipeline,
or Git artifact.

## Scope and exact coverage

The authoritative overlay-aware route-J projections cover 15 source scenes and
802 source rows. The canonical manifest excludes 27 rows in one partially
translated scene; the active overlay adds no J exclusion. The exact permitted
scope is therefore 15 translation files and 775 rows.

| Scene | Exact permitted indexes read | Rows |
|---|---:|---:|
| `SC_J0000_00_J0100_01` | `1` | 1 |
| `SC_J0100_01_J0100_02` | `1-109` | 109 |
| `SC_J0100_02_J0100_03` | `1-45` | 45 |
| `SC_J0100_03_J0100_04` | `1-76` | 76 |
| `SC_J0100_04_J0100_05` | `1-10,38-61` | 34 |
| `SC_J0100_05_J0100_06` | `1-36` | 36 |
| `SC_J0100_06_J0100_07` | `1-84` | 84 |
| `SC_J0100_07_J0100_08` | `1-60` | 60 |
| `SC_J0100_08_J0100_09` | `1-47` | 47 |
| `SC_J0100_09_J0100_10` | `1-47` | 47 |
| `SC_J0100_10_J0100_15` | `1-70` | 70 |
| `SC_J0100_16_J0100_20` | `1-14` | 14 |
| `SC_J0100_17_J0100_20` | `1-9` | 9 |
| `SC_J0100_18_J0100_20` | `1-16` | 16 |
| `SC_J0100_20_Z9999_99` | `1-127` | 127 |
| **Total** |  | **775** |

The exact excluded gap is `SC_J0100_04_J0100_05:11-37` (27 rows). It is absent
from the model projection, translation, and QC artifacts. It was not opened,
quoted, summarized, inferred, reconstructed, or bridged during this audit.
There is no fully excluded J scene.

Evidence reviewed: all 15 current translations; all 15 public overlay-aware
`scratchpad/model_sources/SC_J*.json` projections; the route-J continuity
preflights, including the current final-J preflight that supersedes historical
zero-text classifications; the project bible; exclusions and narrative gates;
all 15 accuracy records, all 15 literary records, all 15 per-scene
contested/arbitration records, the final-J translation handoff, and the global
Samesuga arbitration closure. No raw source dump was opened.

## Blocking finding

### J-B01 — the still-anonymous client is falsely made male

- **Scene/indexes:** `SC_J0100_08_J0100_09:29,32`
- **Severity/category:** `blocking / hallucination, reveal, continuity`
- **Current text at 29:** `「It's fine for the client to worry because his
  daughter's been down lately, but hiring a detective to investigate her feels
  kind of petty.」`
- **Current text at 32:** `「The client also said that if anyone's bullying his
  daughter, we should teach them a painful lesson.」`
- **Filtered source evidence:** both rows say only `依頼主` (`the client`) and
  `娘` (`daughter`). Neither row marks the client's gender. The English
  possessive `his` is unsupported at both indexes.
- **Project/reveal evidence:** `SC_J0100_20_Z9999_99:68` explicitly identifies
  the client as Yoshimi's mother (`私のお母さん`), and `76-77` continues with
  the mother/daughter explanation. The final-J preflight locks that recognition
  to the common convergence.
- **Diagnosis/fix direction:** the two added masculine possessives create a
  false client identity and a direct contradiction when the mother is revealed.
  Keep the client gender-neutral before the reveal, using `their daughter` or
  an equivalent construction at both indexes. Do not name or imply the mother
  early.
- **Systemic/status:** `false (two-line local referent chain) / open`

## Minor finding

### J-m01 — the locked location name `Ryugu` is literalized once

- **Scene/index:** `SC_J0100_03_J0100_04:2`
- **Severity/category:** `minor / lore and continuity`
- **Current text:** `The Ryuumeikan student-council room, also known as the
  Dragon Palace.`
- **Filtered source evidence:** `竜鳴館生徒会室、別名“竜宮”。`
- **Project evidence:** `bible/glossary.md` locks `竜宮` to the recurring proper
  name `Ryugu` and explicitly disallows ad hoc translation.
- **Diagnosis/fix direction:** restore `Ryugu` while preserving the sentence's
  room/appositive structure; for example, `The Ryuumeikan student-council room,
  also known as Ryugu.`
- **Systemic/status:** `false / open`

## Narrative and route-wide checks

- **Route continuity:** The crossover disclaimer, Serori's failed infiltration,
  street-food encounter, council debrief, Kaname/Iruka visit, watcher sequence,
  Mecha Takane incident, investigation recap, Yoshimi's abduction, bond test,
  three answer branches, common confrontation, and ensemble coda remain in
  coherent order. The frame shift back to the school grounds at
  `SC_J0100_20_Z9999_99:107` stays abrupt as sourced.
- **Agency and causality:** Serori performs the infiltration and later issues
  the challenge; Otome detects and pursues her; Yoshimi senses the watcher;
  Shinichi confesses his separate tailing; Otome captures Mecha Takane; the
  crossover group conducts surveillance and takes Yoshimi; Kinu triggers the
  hostage machine; Hinano and Kaname stop the fight. No other agent/patient
  reversal survived source checking.
- **Reveal timing:** The apparent Nagomi in the reaction test remains Honami in
  disguise, while the real Nagomi appears only as Mecha Takane's captive in the
  common scene. Generic `Voice` remains at `J0100_20:53-54`; Takane names Hinano
  at `56`, and the explicit `Hinano` speaker begins at `57`. Yoshimi's colder
  beat at `79-81` remains unexplained. J-B01 is the sole reveal-chain failure.
- **Branch integrity:** `J0100_16`, `J0100_17`, and `J0100_18` were read as
  mutually exclusive outcomes before the common `J0100_20` convergence. The
  Erika and Inori accusations retain bad outcomes; only the correct Nagomi
  branch contains Otome and Erika's praise. No branch-only reaction leaks into
  a sibling or the common scene.
- **Character voice:** Serori stays hyperactive and selectively catlike;
  Honami theatrical; Poem shy, sparse, and deadpan; Takane haughty; Tomoe gentle;
  Kaname cool; Iruka frantic; Hinano grandiose; Otome martial; Erika polished;
  Kinu brash; and Leo briskly self-deprecating. Yoshimi's friendly surface and
  momentary colder undercurrent remain distinct.
- **Names and lore:** `Samesuga` is correct at
  `SC_J0100_09_J0100_10:4,13`, with zero `Samehyo`, `Samehyou`, or `Samejima`
  residue. `Igaguri` follows the explicit final-J preflight decision. All
  crossover speaker maps remain stable. J-m01 is the only confirmed proper-name
  drift.
- **Non-graphic controls:** the Mecha Takane explosions and Shinichi's
  interrupted disrobing remain brief slapstick without added injury, exposure,
  or lethal outcome. `take out` at J0100_20:45 preserves the written dark
  undertone without asserting a killing.
- **Investigated non-findings:** the blonde-ninja comparison at J0100_01:51,
  shrimp-hair image at J0100_06:51, dry-gaze wording at J0100_07:29, apparent
  Takane destruction at J0100_08:12, firearms-and-swords joke at J0100_08:34,
  Yoshimi/Tomoe proximity at J0100_09:45, and J0100_20:39/89/104 are all
  source-faithful. The `Poepoe`, `privates` / `pride`, sister-hierarchy forms,
  unwrapped `Sato... san?`, unnamed younger brother, crest catchphrase, and
  `Kuu, kuu` decisions remain supported by the final QC/arbitration record.
- **Title-quote sentinel:** `SC_J0100_01_J0100_02:2` is not missing a spoken
  wrapper. Its null-speaker source is a disclaimer whose opening corner quote
  closes immediately after the embedded work title; the sentence itself does
  not end in `」`. The extracted `kind` label reflects that title-leading
  punctuation. The unwrapped English disclaimer is therefore retained as a
  documented non-finding.

## Deterministic validation

- **Public validator:** `PASS` — `python tools/codex_vn_pipeline.py validate`
  exited `0`; all 15 J scenes reported exact `OK` counts.
- **Cardinality/index joins:** `PASS` — 15 translations and 15 projections;
  775/775 exact permitted indexes; all 27 excluded indexes absent.
- **Internal file identity:** `PASS` — all 15 translation `file` values match
  their scene filenames.
- **Source identity:** `PASS` — 775/775 present, unique engine IDs and 775/775
  canonical 64-hex SHA-256 fields; the public source/join gate accepted every
  scene.
- **Artifact inventory:** `PASS` — exact matching sets of 15 accuracy, 15
  literary, and 15 contested/arbitration records.
- **Speaker maps:** `PASS` — every permitted non-null source speaker resolves
  to a nonempty localized map entry; cross-scene values are stable.
- **Wrappers:** `PASS after semantic sentinel review` — all actual spoken
  dialogue retains `「...」`; narration is unwrapped. The one mechanical
  kind/wrapper discrepancy is the embedded-title disclaimer at J0100_01:2
  documented above, not spoken dialogue.
- **Codec/controls:** `PASS` — all 775 target strings encode as CP932; no smart
  quotes, Unicode ellipses, em/en dashes, manual line breaks, unresolved `XX`,
  source control tokens, or placeholders were found.
- **Manifest narrative gates:** `PASS` — no source mirror or repeated-choice
  group is declared. The three structurally exclusive answer branches also
  pass their manual outcome/convergence check.
- **Terminology continuity:** `FAIL` only at J-m01.
- **Critical narrative gate:** `FAIL` because J-B01 remains open.

## Story-image and runtime limitations

`docs/UI_STORY_IMAGE_LOCALIZATION_MANIFEST.md` was used as the sole visual
authority. Its ledger covers aggregate title, gallery, and ending UI assets but
maps no asset to an SC_J scene, index, branch, or crossover variant. No
scene-linked image was inspected or used as evidence. This report therefore
makes no claim about route-J CGs, sprites/expressions, backgrounds, prop text,
image triggers, ending labels, or any other scene-image correctness.

No live engine, textbox, nameplate, backlog, wordwrap, build, image-trigger, or
reinjection proof was available. Static joins, wrappers, metadata, and CP932
checks do not establish runtime fit or visual correctness.

## Required routing

1. Route J-B01 through a two-index accuracy correction that removes the
   unsupported masculine client possessive while preserving the mother reveal
   at J0100_20:68.
2. Route J-m01 through a one-index glossary/continuity correction to `Ryugu`.
3. Revalidate both scenes, then reread the J0100_08 client discussion through
   the J0100_20 mother reveal and the immediate J0100_03 location block.

No broader rewrite is indicated. Route J remains **FAIL / BLOCKED** until the
blocking referent/reveal finding is closed.
