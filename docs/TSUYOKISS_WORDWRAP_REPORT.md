# Tsuyokiss Full Edition — audit EXE et chaîne de wordwrap

## Conclusion

`tkfe.exe` ne fait pas de wordwrap occidental fiable dans sa couche de police. Il mesure d'abord le texte, puis dessine **une ligne à la fois** avec `ID3DXFont::DrawTextA` et `DT_SINGLELINE`. Les retours présents dans le scénario sont donc déterminants pour la textbox et sont ensuite conservés dans l'historique.

La chaîne fournie impose donc les invariants suivants avant injection :

- mesure en pixels, jamais en nombre de caractères ;
- coupure uniquement sur une frontière de mots ;
- trois lignes au maximum ;
- aucune césure d'un token trop long : rejet et retour au traducteur ;
- marge conservatrice configurable de 0 à 3 %, jamais davantage ;
- même texte composé pour la textbox et le backlog ;
- vérification CP932 avant toute écriture ;
- correspondance stable par ID et empreinte de la source japonaise.

## Preuves relevées dans l'EXE et les ressources

EXE examiné : `tkfe.exe`, PE32, 1 031 168 octets, SHA-256 `150d617681cc103527aea9a7e1cd7e313df63baac0aa049c201374d3780a561c`.

- La fonction à `0x44D790` appelle `ID3DXFont::DrawTextA` une première fois avec `0x420` (`DT_CALCRECT | DT_SINGLELINE`), puis dessine avec `0x20` (`DT_SINGLELINE`). La couche de police ne compose donc pas plusieurs lignes.
- La création à `0x44D650` appelle `D3DXCreateFontA` avec largeur 0, graisse 400, `SHIFTJIS_CHARSET` (128) et une hauteur fournie par l'appelant. Le choix de police est exposé par `cfgGraFont` ; les métriques sont dynamiques.
- La ressource de configuration donne la zone texte normale `723 × 196`, le départ du message `(34,453)` et une fenêtre globale `800 × 208`. Les contrôles commencent à droite vers x=693 : la largeur de travail conservatrice dérivée est **659 px** (`693 - 34`). Elle doit être confirmée par capture instrumentée avant gel définitif.
- Le backlog affiche quatre entrées espacées de 122 px (y=49, 171, 293, 415), ce qui correspond à la même enveloppe de trois lignes par message.
- Les scénarios japonais comportent déjà leurs retours manuels. Ils doivent être supprimés lors de la composition anglaise, puis reconstruits aux frontières de mots.

Corpus extrait : 13 blocs scénario (0028–0040), 299 627 lignes physiques, 59 765 messages détectés dans les scènes `SC_*` (40 576 dialogues, 19 189 narrations).

## Outils

- `tsuyokiss_scenario.py extract` produit le JSONL de traduction avec IDs stables et SHA-256 de la source.
- `tsuyokiss_wrap.py` compose et audite le JSONL. Sous Windows, son backend GDI mesure la police ANSI sélectionnée ; `--font-file` permet une pré-QA portable, mais ne remplace pas la validation Windows.
- `tsuyokiss_scenario.py apply` réinjecte seulement les lignes ayant le statut `ok`, vérifie que la source n'a pas changé et encode strictement en CP932.
- `zlc2_repack_inplace.py` recomprime un bloc dans son créneau FPK sans déplacer la table chiffrée. Il rejette tout dépassement au lieu de produire une archive douteuse.

Exemple Windows, après avoir renseigné les traductions dans le champ `text` :

```powershell
python scripts/tsuyokiss_wrap.py translations.jsonl wrapped.jsonl --face "MS UI Gothic" --height 26 --width 659 --margin 0.00
python scripts/tsuyokiss_scenario.py apply data_blocks wrapped.jsonl translated_blocks
python scripts/zlc2_repack_inplace.py data.fpk data_blocks/manifest.json translated_blocks data.patched.fpk
```

## Validation effectuée

- décompression ZLC2 reconstruite d'après l'EXE : 547 blocs, roundtrip contrôlé ;
- recompression du bloc 0028 original dans son créneau, redécompression identique octet pour octet ;
- tous les octets hors créneau sont restés identiques ;
- extraction de 59 765 messages et application d'un remplacement test sur les 13 blocs ;
- décodage CP932 intégral des blocs reconstruits ;
- tests unitaires : retours japonais normalisés, frontière de mots, rejet d'un mot trop long, rejet d'une quatrième ligne.

## Limites à ne pas masquer

La preuve statique établit le comportement de mesure/rendu, mais une validation visuelle native reste obligatoire pour figer la hauteur de police et confirmer la borne droite exacte. Le défaut proposé (`MS UI Gothic`, hauteur 26, largeur 659) est une hypothèse étayée par la géométrie et le corpus japonais, pas encore une mesure runtime.

La réinjection FPK en place est sûre mais volontairement restrictive : une traduction qui rend un bloc compressé plus grand que son créneau est rejetée. Le test anglais volontairement plus long a bien déclenché ce garde-fou. Pour supprimer cette contrainte, il faudra reconstruire puis prouver la table d'index RLE/chiffrée du FPK, ou patcher le chargeur afin de lire un conteneur externe. Aucun de ces deux changements n'est présenté ici comme terminé.
