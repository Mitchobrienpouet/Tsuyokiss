Translate scene {{SCENE}} from {{SOURCE_FILE}} into {{TRANSLATION_FILE}}.

Read AGENTS.md, every bible file, {{SPEC_FILE}}, `narrative_gates.json`, and
`content_exclusions.json`. Run draft, adversarial accuracy, naturalness, and
consistency passes. Preserve every projected source index as a string key under
`lines`; translate body text only and use the configured codec-safe punctuation.
Never add an index absent from the filtered source. If a complete translation
already passes validation, return `skipped` without rewriting.

Use identical English for repeated-choice groups. For a declared mirror, copy
the canonical scene's fully arbitrated shared lines; if unavailable, return
`blocked` instead of guessing. Return the required structured run report.
