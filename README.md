# cycle-cross-training

Cycle de cross training CA5 (savoir s’entraîner) du lycée Georges Pompidou : **Première et Terminale**, chacune en **deux démarches** (progressive ou GAREEPS), 9 séances de 75 min, évaluation en S9.

- `index.html` : l’écran de cours (fabriqué par `mon-eps/atelier/ecran-de-cours/construire.py`, ne pas le modifier ici). Bascule 1re / Tle et Progressive / GAREEPS en haut à droite.
- `outils.html` : l’outil complet (bouton « Préparer ») : séances des 4 parcours, mouvements, formats, mobiles et FC, échauffements, banque, différenciation, GAREEPS, épreuve, carnet élève, impression.
- `cross-training-donnees.js` : toutes les données (séances, fiches, mouvements, référentiel, schémas), partagées par les deux pages.
- `img/mv/` : photos détourées des mouvements ; les mouvements à la kettlebell, à la box et à la barre sont dessinés dans `cross-training-donnees.js`.
- `pdf/` : séances, cycles complets, planche des mouvements, carnet, épreuve, banque, échauffements (régénérés à chaque modification).

Matériel : Première = poids de corps, banc, box, kettlebell ou haltère léger ; Terminale = + barre.
Mobiles : les 2 du référentiel (modéré 140-160, élevé 160-180). Les 3 filières de l’ancienne appli chrono y sont rattachées (le chrono est désormais dans l’appli élève) (onglet « Mobiles et FC »).

## Vidéos de démonstration

`videos.js` associe à 77 des 81 mouvements une vidéo YouTube courte (souvent moins d'une minute), surtout en français : 15-Minute Challenge, EPS Nancy-Metz, MUST COACH, WODMOOV, CrossFit… Le bouton ▶ sur l'image ouvre la vidéo en `youtube-nocookie`. Il faut internet pour la lire ; sans connexion, un message renvoie à la fiche. Les vidéos marquées `a:1` sont seulement proches du mouvement de la fiche, et c'est la fiche qui fait foi. Sans vidéo : arlaud, course, sauts-groupes-banc, gainage-mains-cuisses. Pour changer une vidéo, il suffit de remplacer son identifiant `y` dans `videos.js`. La source est `ct/src/videos.py`.

## Origine

Le chrono de l'appli élève reprend des formats et des réglages de l'appli **Cross Training Pompidou** de Yannick Dartois : Tabata à régler, niveaux N0 à N4, EMOM+1, FOR TIME à paliers, son / vibreur / muet. Son dépôt `cross-training-pompidou` reste intact, et le cycle ne renvoie plus vers lui. Le détail de ce qui a été repris est dans `ORIGINE-cross-training-pompidou.md`.
