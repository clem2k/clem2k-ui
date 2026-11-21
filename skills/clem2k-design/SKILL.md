---
name: clem2k-design
description: Applique le design system clem2k (terminal/Matrix lisible + verre) à toute interface, page web, app desktop, dashboard, slide ou visuel que Clem demande de créer ou de restyler.
---

# Design system clem2k

Clem a un design system personnel, **clem2k** (toujours en minuscules). Tout ce qui a une interface ou un rendu visuel et qu'il fait créer ou restyler (page web, app desktop, dashboard, outil interne, artefact HTML, slides, design, README illustré) suit ce système, sauf s'il demande explicitement autre chose.

## 1. Lire la source de vérité

Deux sources, synchronisées :

- **Le kit `clem2k-ui`** : https://github.com/clem2k/clem2k-ui (clone local habituel : `~/computer/data/clem2k-ui`). Dans un projet de code, c'est lui qu'on installe et qu'on lit : `README.md`, `docs/brand.md`, `docs/tokens.md`, `docs/components.md`, `docs/integration.md`, `dist/clem2k.d.ts`.
- **Le design system Claude** : artefact `51e92e9e-9211-418e-bb3e-0630cb07e124` (https://claude.ai/artifact/B7erxb7Ut5e5Zp2fREiDFH). Pour un artefact, des slides ou un design, lire avec l'outil Artifact (`read_file`, par `path`) `project/README.md`, puis `project/tokens.json`, et si besoin `project/components/bundle.css`, `bundle.js`, `index.d.ts`. Quand l'outil le permet (Design, Slides…), rattacher ce design system au lieu de recopier les valeurs.

Si aucune source n'est lisible, utiliser les valeurs de secours ci-dessous et le dire.

## 2. Adapter à la cible

Toujours passer par `clem2k-ui` dans un projet de code (version épinglée), jamais de copie des valeurs en dur.

- **HTML statique** : `dist/clem2k.css` + classes `ck-` (`ck-glass`, `ck-nav`, `ck-btn ck-btn-primary`, `ck-card`, `ck-input`, `ck-table`, `ck-term`…), `data-theme` sur `<html>`.
- **React / Vite / Next** : `npm i github:clem2k/clem2k-ui#vX.Y.Z`, `import "clem2k-ui/clem2k.css"`, `import { NavBar, Window, … } from "clem2k-ui"`.
- **Artefact HTML autonome** : inliner `clem2k.css`, charger React 18 UMD puis `clem2k.js` → `window.clem2k`.
- **Tailwind** : `presets: [require("clem2k-ui/tailwind")]` + `tokens.css`.
- **Python web** : `pip install "clem2k-ui[fastapi] @ git+https://github.com/clem2k/clem2k-ui@vX.Y.Z"`, `clem2k_ui.mount(app, templates=…)`, `{{ clem2k_head() }}` ; Flask : `flask_blueprint()` ; Django : `STATIC_DIR`.
- **Qt (PySide/PyQt)** : `clem2k_ui.apply_qt(app)` ; `setProperty("variant", "primary")`. Pas de flou en Qt : verre = `bg-200` opaque + `glass-edge`.
- **Tauri / Electron** : comme le web.
- **CLI / TUI** : `clem2k_ui.rich_theme()`, `clem2k_ui.textual_theme()`.
- **Nouveau projet** : ajouter le snippet de `docs/claude.md` au `CLAUDE.md` du projet.

## 3. Règles non négociables

- **Lisible d'abord.** Texte courant en `ink` sur `bg-100`, 16/26, lignes ≤ 72ch. Jamais de paragraphe en néon, jamais de pluie de code animée dans l'interface.
- **Un seul néon à la fois** : `neon` = accent (liens, prompt, focus, bouton primaire, actif, succès).
- **Ce qui flotte est en verre et arrondi ; ce qui est posé est opaque et carré.** Verre (`glass-fill` + blur 24px + `glass-edge` + `glass-shadow`, rayons 12/20/pill) seulement pour navigation, toolbars, sidebar, dock, menus, toasts, tooltips, dialogs, cadres de fenêtre. Contenu (texte, cartes, tableaux, code, champs) : rayons 0–4px, opaque.
- Statuts : toujours un mot ou préfixe (`[ok]` `neon`, `[warn]` `py-yellow`, `[info]` `py-blue-text`, `[err]` `bot-text`). Texte rouge/bleu : variantes `-text`.
- Bots : couleur `bot` + avatar bot.
- Une seule police : JetBrains Mono, repli `ui-monospace`.
- Icônes : icônes pixel clem2k (`Icon`, `dist/icons/*.svg`, `dist/icons.svg`), tailles multiples de 12 uniquement. Pas d'emoji dans l'interface.
- Toujours `focus-ring` visible ; respecter `prefers-reduced-motion` et `prefers-reduced-transparency` ; proposer le thème `hc`.
- Contraste vérifié : 4.5:1 minimum pour le texte, 3:1 pour bordures de contrôle et icônes.
- Marque : « clem2k » en minuscules ; logo = buste à cravate néon (`assets/logo/`), favicon 16px = cravate pixel.
- Ton des textes d'interface : français, tutoiement, direct et technique ; un clin d'œil geek permis dans les titres et états vides, jamais dans les erreurs.

## 4. Valeurs de secours (thème dark)

| token | valeur | token | valeur |
|---|---|---|---|
| bg-000 | #0a0d0b | ink | #cfdccf |
| bg-100 | #0e120f | ink-strong | #eaf2ea |
| bg-200 | #151a16 | ink-muted | #9cae9e |
| bg-300 | #1d241e | neon | #3be81a |
| selection | #173d12 | neon-soft | #a8f59a |
| line | #283129 | on-neon | #0a0d0b |
| line-strong | #5f7261 | bot / bot-text | #f84818 / #ff6a45 |
| glass-fill | rgba(22,28,23,.8) | py-yellow | #ffd43b |
| glass-edge | rgba(207,220,207,.16) | py-blue / py-blue-text | #4b8bbe / #6aa6d8 |

Typo : display 40/48 700 · h1 28/36 700 · h2 20/28 600 · h3 16/24 600 · body 16/26 · small 13/20 · code 15/24 · label 12/16 600 capitales +0.08em.
Espacements 4/8/16/24/40. Rayons 0, 2, 4 (contenu) · 12, 20, 999 (verre). Focus : `0 0 0 2px #3be81a`.

## 5. Avant de livrer

Relire le rendu (capture si possible) en `dark` et `hc` : néon utilisé avec parcimonie, aucun texte long sur du verre, contrastes OK, icônes nettes. Dire en une ligne que le design suit clem2k et signaler toute entorse faite à la demande de Clem.
