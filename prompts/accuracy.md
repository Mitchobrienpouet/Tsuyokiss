Perform accuracy QC on scene {{SCENE}}. Compare {{TRANSLATION_FILE}} line by
line against {{SOURCE_FILE}}, with every bible file and {{SPEC_FILE}} open.

Correct only hard errors: subject/object reversal, negation, modality,
tense/aspect, referent or speaker, dropped or added meaning, ruby, terminology,
glossary drift, or incompleteness. Write {{QC_FILE}} with each changed index,
before/after, reason, and any materially defensible alternative. Do not perform
cosmetic rewriting or reconstruct excluded rows. Return the required structured
run report.
