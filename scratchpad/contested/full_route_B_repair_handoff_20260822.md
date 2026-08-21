# Full-route B targeted translation repair handoff

Stage: targeted translation repair after
`scratchpad/readthrough/full_route_B_critical_20260822.md`.

Scope was limited to findings B-M01 through B-M03 and B-m01 through B-m08.
This repair changed seven translation JSON files and this handoff only. It did
not edit source/model projections, the bible, QC, per-scene arbitration,
readthrough, exclusions, gates, configuration, pipeline state, or Git. The
pending `Samehyo` / `Samesuga` global naming question was not touched.

## Exact target-text changes

| Scene:index | Before | After | Reason |
|---|---|---|---|
| `SC_B0130_00_K0900_00:87` | `Come to think of it, the Kurogane had apparently always led the vanguard in battle.` | `Come to think of it, the Kurogane clan had apparently always led the vanguard in battle.` | Supply the collective noun without changing the historical claim. |
| `SC_B0180_00_B0190_00:3` | `Sato had something to take care of, so I was cleaning up the Dragon Palace in her place.` | `Sato had something to take care of, so I was cleaning up Ryugu in her place.` | Restore the locked proper name `Ryugu`. |
| `SC_B0370_00_B0380_00:3` | `「Our destination is Ika Island, the one you can see from here.」` | `「Our destination is Ikajima, the one you can see from here.」` | Restore the locked proper name `Ikajima`. |
| `SC_B0370_00_B0380_00:116` | `「But to keep things fair, the Combat Festival tournament uses boxing, which our school doesn't have as a club. That's your opening.」` | `「But to keep things fair, the Sports Martial Arts Festival's tournament is boxing, and our school doesn't have a boxing club. That's your opening.」` | Distinguish the full festival from its boxing tournament. |
| `SC_B0370_00_B0380_00:371` | `「I'm entering the Combat Festival tournament this weekend. I'm training for that.」` | `「I'm entering the boxing tournament this weekend. I'm training for that.」` | Source names only the tournament here; do not add the festival name. |
| `SC_B0370_00_B0380_00:407` | `「I just signed up for the Combat Festival tournament.」` | `「I just signed up for the Sports Martial Arts Festival's boxing tournament.」` | Restore the locked full-event name while retaining the tournament distinction. |
| `SC_B0370_00_B0380_00:553` | `「Though the Combat Festival divides us into eastern and western teams, so it feels as if I'm sending salt to my enemy.」` | `「Though the Sports Martial Arts Festival divides us into eastern and western teams, so it feels as if I'm sending salt to my enemy.」` | Restore the locked full-event name. |
| `SC_B0380_00_B0390_00:1` | `--The Combat Festival began.` | `--The Sports Martial Arts Festival began.` | Restore the locked full-event name. |
| `SC_B0380_00_B0390_00:27` | `Day two of the Combat Festival.` | `Day two of the Sports Martial Arts Festival.` | Restore the locked full-event name. |
| `SC_B0380_00_B0390_00:126` | `「Ladies and gentlemen, thank you for waiting! The Combat Festival's main event, the Dragon Cup, will decide our mightiest warrior!」` | `「Ladies and gentlemen, thank you for waiting! The Sports Martial Arts Festival's main event, the Dragon Cup, will decide our mightiest warrior!」` | Restore the locked full-event name. |
| `SC_B0390_00_B0400_00:189` | `「School again this week. Put the Combat Festival behind you.」` | `「School again this week. Put the Sports Martial Arts Festival behind you.」` | Restore the locked full-event name. |
| `SC_B0390_00_B0400_00:603` | `「You trained for the Combat Festival. Keep it up.」` | `「You trained for the Sports Martial Arts Festival. Keep it up.」` | Restore the locked full-event name. |
| `SC_B0390_00_B0400_00:1084` | `「But for some reason... you alone, I did not want to call me boring.」` | `「But for some reason... I didn't want you, of all people, to call me boring.」` | Repair subject/object syntax while preserving Otome's exclusive emphasis on Leo. |
| `SC_B0390_00_B0400_00:1231` | `「Women hold things so long. Troublesome. With Date, we nearly fought, but now we speak easily.」` | `「Things with women drag on, which is a pain. Date and I nearly got into a fight once, but we were back to talking normally in no time. That's much easier.」` | Remove translationese and preserve Yohei's contrast between prolonged trouble with women and quickly recovering with Date. |
| `SC_B0400_00_B0500_00:339` | `「Hey, Tecchan. 'Sup?」` | `「Hey, Tetchan. 'Sup?」` | Restore the established nickname spelling. |
| `SC_B0400_00_B0500_00:341` | `「How's that little-brother problem you asked me about before summer break? You called to say you'd worked it out and gotten close...」` | `「Tetchan, how's that little-brother problem you asked me about before summer break? You called to say you'd worked it out and gotten close...」` | Restore the source's omitted direct address. |
| `SC_B0400_00_B0500_00:345` | `「Aw, Tecchan, that's such an adorable problem! Love makes a maiden weak.」` | `「Aw, Tetchan, that's such an adorable problem! Love makes a maiden weak.」` | Restore the established nickname spelling. |
| `SC_B0400_00_B0500_00:351` | `「I'm not trying to tell you what to believe, Tecchan.」` | `「I'm not trying to tell you what to believe, Tetchan.」` | Restore the established nickname spelling. |
| `SC_B0880_00_B0900_00:166` | `He was a pretty hot-blooded guy himself.` | `「He was a pretty hot-blooded guy himself.」` | Restore the required dialogue wrapper around Leo's spoken line. |

Target-text total: **19 exact rows**. No surrounding line was rewritten.

## Exact speaker-map changes

| Translation | Source speaker | Before | After | Exact permitted rows affected |
|---|---|---|---|---|
| `SC_B0370_00_B0380_00` | `イガグリ` | `Igaguri` | `Burrhead` | `370,372` |
| `SC_B0380_00_B0390_00` | `イガグリ` | `Igaguri` | `Burrhead` | `184` |
| `SC_B0390_00_B0400_00` | `イガグリ` | `Igaguri` | `Burrhead` | `215,742` |
| `SC_B0390_00_B0400_00` | `土永さん` | `Tsuchinaga` | `Mr. Tsuchinaga` | `197,220,223,848,1144` |
| `SC_B0400_00_B0500_00` | `土永さん` | `Tsuchinaga` | `Mr. Tsuchinaga` | `256` |
| `SC_B0400_00_B0500_00` | `３年女生徒` | `Third-year Girl` | `Third-Year Girl` | `339,341,343,345,351-353,360` |

Speaker-map total: **6 exact map values**, affecting **19 permitted
nameplate rows**. No speaker key was added, removed, or remapped to another
character.

## Files changed

- `translations/SC_B0130_00_K0900_00.json`
- `translations/SC_B0180_00_B0190_00.json`
- `translations/SC_B0370_00_B0380_00.json`
- `translations/SC_B0380_00_B0390_00.json`
- `translations/SC_B0390_00_B0400_00.json`
- `translations/SC_B0400_00_B0500_00.json`
- `translations/SC_B0880_00_B0900_00.json`
- `scratchpad/contested/full_route_B_repair_handoff_20260822.md`

## Contested readings and follow-on state

Materially contested permitted readings introduced by this repair: **NONE**.
The full-event/tournament distinction and all name renderings were explicit
supervisor decisions. Existing accuracy, literary, arbitration, and readthrough
records remain untouched and therefore require the separately assigned
post-repair recertification/reread stages before route completion can be
claimed.

## Deterministic validation

`PASS` after repair:

- seven changed translation files retain their exact 4,051 permitted indexes;
- all 4,051 permitted source hashes and unique engine IDs match current
  authoritative metadata;
- complete speaker-map source-key coverage, with all six repaired values and
  their exact effective row sets verified;
- every authoritative dialogue row in the changed files has `「...」` wrappers;
- all target strings encode as CP932 and contain no forbidden smart typography
  or manual line breaks;
- JSON parses without duplicate keys, all quote/parenthesis counts balance,
  and no excluded or unknown index is present;
- route-wide repair sentinels contain no remaining `Combat Festival`,
  `Tecchan`, `Dragon Palace`, `Ika Island`, or the repaired legacy speaker-map
  values in any `SC_B` translation.

Runtime nameplate, textbox, backlog, wordwrap, and visual proof were not part of
this translation-stage repair.
