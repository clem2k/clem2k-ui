# clem2k-ui — notes pour Claude

Dépôt du kit du design system clem2k (voir README.md).

- Source unique des valeurs : `tokens/tokens.json`. Ne jamais éditer `dist/` ni `docs/tokens.md` : lancer `python3 scripts/build.py`.
- Sources : `src/clem2k.css`, `src/clem2k.js` (script classique, `window.React`, pas d'`import`, pas de `</script` littéral), `src/clem2k.d.ts`, `src/icons.json`.
- Toute modification de couleur doit respecter `docs/accessibility.md` (4.5:1 texte, 3:1 bordures/icônes, 7:1 en `hc`).
- Après un changement : rebuild, ouvrir `examples/*.html` en dark et hc, mettre à jour `docs/components.md` et `CHANGELOG.md`.
- Le design system Claude de référence est https://claude.ai/artifact/B7erxb7Ut5e5Zp2fREiDFH ; garder les deux synchronisés (`docs/maintenance.md`).
- Langue : documentation et UI en français, tutoiement. « clem2k » toujours en minuscules.
