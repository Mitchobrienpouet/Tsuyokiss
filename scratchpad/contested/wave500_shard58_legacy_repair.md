# Wave500 shard58 legacy translation repair

Stage: translation-stage mechanical repair after
`state/legacy_repair_preflight_wave500_shard58.md`.

No English text was newly translated or rewritten. Each surviving translation
string was copied byte-for-byte, the audited legacy-only keys were discarded,
and the remaining values were compacted onto the exact authoritative filtered
source indexes. Speaker maps and top-level file metadata were preserved.

## Exact mappings

### `SC_M0431_00_M0432_00`

- Legacy coverage: `1-69`
- Authoritative coverage: `1-65`
- Discarded legacy-only keys: `20`, `29`, `44`, `69`
- Retained mapping:
  - old `1-19` -> new `1-19`
  - old `21-28` -> new `20-27`
  - old `30-43` -> new `28-41`
  - old `45-68` -> new `42-65`
- Displaced valid tail preservation: old `66-68` -> new `63-65`
- Translation SHA-256: old
  `cdfc2a384aeca6ec43d88eb1f84a6ec44ac73a1190b03f8800e91a28a3c8524c`;
  repaired
  `ba882f7215efea9da22c2343036b97a9d37ab9b76e7ecfe3904b7385b89a08b0`

### `SC_M0470_00_M0471_00`

- Legacy coverage: `1-69`
- Authoritative coverage: `1-68`
- Discarded legacy-only key: `48`
- Retained mapping:
  - old `1-47` -> new `1-47`
  - old `49-69` -> new `48-68`
- Displaced valid tail preservation: old `69` -> new `68`
- Translation SHA-256: old
  `5476611e7d52cd5cb69f439b362f2be2147955ac8499dfb165ec24b30f22b96c`;
  repaired
  `e11ae61e80fe88464612bc774267e04f19284fe546bf801681e95c2bc6e5c990`

### `SC_M0500_00_M0501_00`

- Legacy coverage: `1-67`
- Authoritative coverage: `1-65`
- Discarded legacy-only keys: `50`, `56`
- Retained mapping:
  - old `1-49` -> new `1-49`
  - old `51-55` -> new `50-54`
  - old `57-67` -> new `55-65`
- Displaced valid tail preservation: old `66-67` -> new `64-65`
- Translation SHA-256: old
  `ed2d3fd6a01b215e2b40bc29e504ee69fcfc8f046ffdffa8d9c1f9cd15ddc9b7`;
  repaired
  `4b42b91de27078ae985cdcee4203cec2c9bf2d63ca6b8ee8a31dc49997e7649b`

### `SC_M0520_00_M0530_00`

- Legacy coverage: `1-58`
- Authoritative coverage: `1-57`
- Discarded legacy-only key: `9`
- Retained mapping:
  - old `1-8` -> new `1-8`
  - old `10-58` -> new `9-57`
- Displaced valid tail preservation: old `58` -> new `57`
- Translation SHA-256: old
  `484645b99bf82c8da197780b279589ac07bb84c7fc2f0bee876307652782c702`;
  repaired
  `87e34ca89d37b7cbf21e85954bf67629f62e909276ec2621ecc4b96099a07433`

## Translation-stage result

- Exact repaired row counts: `65 + 68 + 65 + 57 = 255`.
- Source index joins: exact for all four scenes.
- Surviving translation values: byte-identical and in audited source order.
- Speaker maps/top-level file metadata: unchanged.
- Dialogue/narration wrappers: preserved against current source kinds.
- CP932 encoding: pass for every retained value.
- Materially contested permitted readings introduced by this repair: NONE.

QC and per-scene arbitration records remain untouched for the independent
post-repair stages.
