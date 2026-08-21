# Wave 200 shard 12 continuity/safety preflight

Scenes: `SC_J0100_08_J0100_09`, `SC_J0100_09_J0100_10`, `SC_J0100_10_J0100_15`, `SC_J0100_16_J0100_20`.

Recovered source from `data.fpk` block 0037 yields 47, 47, 70, and 0 translatable rows respectively. `SC_J0100_16_J0100_20` is a zero-text routing scene and requires no translation payload. Neither canonical exclusions nor the active wave overlay declares a restricted range in the three text-bearing scenes, so all 164 source rows are eligible.

## Continuity

- `J0100_08`: immediate aftermath of Mecha Takane's self-destruction. Otome is unharmed; the crossover group reviews the surveillance and decides the Ryuumeikan executive committee may need to be confronted.
- `J0100_09`: Serori stops Yoshimi and Shinichi on the way to school, incapacitates Shinichi, and brings Yoshimi to Matsukasa Park. Tomoe keeps Yoshimi calm while Serori sends a challenge to the executive committee.
- `J0100_10`: the full Ryuumeikan group reaches Matsukasa Park. Serori claims Yoshimi is being bullied and tests the group's bond by asserting one of the girls is an impostor. Leo narrows the candidates to Erika, Nagomi, and Inori and runs a reaction test.
- `J0100_16`: routing only; do not invent text.

Crossover name locks add `海` -> `Umi`; existing Serori, Tomoe, Takane, Kaname, Iruka, and Tsuyokiss locks remain unchanged. Preserve exact indexes, Japanese dialogue brackets, ASCII punctuation, and CP932-clean text.
