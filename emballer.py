"""Fabrique donnees.js des applis élève et prof à partir de cross-training-donnees.js (cycle-cross-training) :
le même contenu, enfermé dans une fonction pour que ses noms courts (S, F, P, T…) ne gênent pas les applis."""
import sys
src=open('/home/claude/cycle-cross-training/cross-training-donnees.js').read()
exp=['MOUV','mvById','MATERIEL','ZONES','NIVEAUX','MOBILES','GAREEPS','PARCOURS','CHARGES','REF','FORMATS','FC','RESSENTIS','ETIREMENTS','mvVisuel','svgEtoile','svgFig','schema','DUREE','mvVignetteKO','mvSansImage']
out='/* donnees.js — copie de cycle-cross-training/cross-training-donnees.js, enfermée dans une fonction.\n   Ne pas modifier ici : modifier le cycle, puis relancer emballer.py. */\n(function(){\n'+src+'\n'+''.join(f'window.{n}={n};\n' for n in exp)+'})();\n'
for d in sys.argv[1:]:open(d+'/donnees.js','w').write(out)
