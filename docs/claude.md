# clem2k et Claude

Deux mécanismes pour que Claude applique clem2k partout, dans les projets actuels et futurs.

## 1. Le skill `clem2k-design`

Fichier : [`skills/clem2k-design/SKILL.md`](../skills/clem2k-design/SKILL.md).

Il dit à Claude, dès qu'il crée ou restyle une interface (page web, app, dashboard, slides, visuel) :

- où lire la source de vérité (le design system Claude « clem2k » et ce dépôt) ;
- comment adapter le système à la cible (HTML, React, Tailwind, FastAPI/Flask/Django, Qt, Tauri, Rich/Textual) ;
- les règles non négociables et les valeurs de secours.

Installation :

- **Claude (app / claude.ai / Cowork)** : enregistré depuis la conversation qui a créé le kit (carte « skill »). Pour le réinstaller : Paramètres → Skills → importer le dossier `skills/clem2k-design`.
- **Claude Code, pour tous tes projets** : `mkdir -p ~/.claude/skills && cp -r skills/clem2k-design ~/.claude/skills/`
- **Claude Code, pour un seul projet** : copier le dossier dans `<projet>/.claude/skills/`.

## 2. Le snippet `CLAUDE.md` à mettre dans chaque projet

À coller dans le `CLAUDE.md` (ou `AGENTS.md`) à la racine de chaque projet qui a une interface :

```markdown
## Design

Ce projet utilise le design system **clem2k** via `clem2k-ui` (https://github.com/clem2k/clem2k-ui, version épinglée dans les dépendances).

- Charger `clem2k.css` (ou `tokens.css` + Tailwind preset) ; `data-theme="dark"` sur `<html>` (`light` pour le clair, `hc` pour le haut contraste, `auto` pour suivre le système).
- Utiliser les composants `clem2k-ui` (React) ou les classes `ck-` ; ne jamais coder une couleur, un rayon ou une police en dur : toujours les variables (`var(--neon)`, `var(--radius-sm)`…).
- Ce qui flotte (nav, toolbars, sidebar, menus, toasts, dialogs) est en verre et arrondi ; ce qui est posé (texte, cartes, tableaux, code, champs) est opaque et carré.
- Lisible d'abord : texte en `ink` sur `bg-100`, néon pour les accents seulement, statuts avec préfixe `[ok] [warn] [info] [err]`.
- Icônes : `Icon` / `dist/icons/*.svg`, tailles multiples de 12. Pas d'emoji dans l'UI.
- Textes d'interface en français, tutoiement. « clem2k » toujours en minuscules.
- Charte complète : `node_modules/clem2k-ui/docs/brand.md` (ou `vendor/clem2k-ui/docs/brand.md`).
```

## 3. Le design system de référence

Le design system vit aussi dans Claude, comme artefact « Design System » : https://claude.ai/artifact/B7erxb7Ut5e5Zp2fREiDFH (aperçus live de tous les composants, charte, assets complets dont avatars et bannière). Claude peut le rattacher directement aux slides et designs qu'il crée. Voir [maintenance.md](maintenance.md) pour garder les deux synchronisés.
