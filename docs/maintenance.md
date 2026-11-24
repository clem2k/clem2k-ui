# Maintenance

## Modifier une valeur

1. Éditer `tokens/tokens.json` (format : listes `{"name","value","usage"}` ; couleurs par thème `{"dark": …, "hc": …, "light": …}`).
2. `python3 scripts/build.py` (ou `npm run build`) : régénère `dist/` et `docs/tokens.md`.
3. Vérifier `examples/web.html` et `examples/desktop.html` dans le navigateur, en `dark`, `light` et `hc`.
4. Vérifier les contrastes si une couleur de texte ou de fond change (règles dans [accessibility.md](accessibility.md)).

## Modifier un composant

- Styles : `src/clem2k.css`. Composants : `src/clem2k.js` (script classique qui lit `window.React` ; le build en tire l'ES module `dist/clem2k.mjs`). Types : `src/clem2k.d.ts`. Doc : `docs/components.md`.
- Icônes : grilles 12×12 dans `src/icons.json` (`#` = pixel). Le build produit `dist/icons/*.svg` et `dist/icons.svg` ; penser à reporter la grille dans `GRIDS` de `src/clem2k.js`.
- Jamais d'édition directe dans `dist/`.

## Publier une version

1. Mettre à jour `version` dans `package.json`, `pyproject.toml` et `python/clem2k_ui/__init__.py`.
2. Ajouter une entrée au [CHANGELOG](../CHANGELOG.md).
3. `git commit`, `git tag vX.Y.Z`, `git push --follow-tags`.
4. Dans les projets : changer le tag épinglé.

Versionnage : patch = correctif visuel, mineure = nouveau composant/token, majeure = renommage ou suppression de token/composant/prop.

## Synchro avec le design system Claude

Le design system « clem2k » dans Claude et ce dépôt partagent `tokens.json`, `clem2k.css` (`components/bundle.css`), `clem2k.js` (`components/bundle.js`) et les types (`components/index.d.ts`). Quand l'un change, demander à Claude de reporter le changement dans l'autre (« synchronise clem2k-ui avec le design system » ou l'inverse).
