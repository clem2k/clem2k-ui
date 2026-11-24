# Changelog

## 0.2.0 — 2026-11-24

- Nouveau thème **light** (`data-theme="light"`) : papier légèrement vert, vert phosphore profond `#156b08` lisible en texte, ocre pour les avertissements, verre blanc à 85 %. Tous les textes ≥ 4.5:1, détail dans `docs/accessibility.md`.
- `data-theme="auto"` : suit `prefers-color-scheme` (dark par défaut, light si le système le demande).
- Nouveaux tokens `hover-tint`, `hover-tint-strong`, `scrim`, `field-on-glass`, `wall-dot` : plus aucune couleur codée en dur dans les composants.
- `dist/clem2k-light.qss`, `clem2k_ui.qss("light")`, `apply_qt(app, "light")`, `textual_theme("light")`.
- `scripts/build.py` ne vide plus `dist/` d'un coup : il réécrit les fichiers puis retire seulement ceux devenus obsolètes.

## 0.1.0 — 2026-11-21

Première version.

- Tokens : thèmes `dark` et `hc`, 21 couleurs, verre (`glass-fill`, `glass-edge`, `glass-sheen`, `glass-shadow`, `blur-glass`), 8 styles de texte JetBrains Mono, 5 espacements, 6 rayons.
- 41 composants React 18 (web + desktop) en ES module et script global, classes `ck-` utilisables sans React.
- Preset Tailwind, feuilles QSS dark/hc, thèmes Rich et Textual.
- Paquet Python `clem2k_ui` (FastAPI/Starlette, Flask, Django, Qt).
- 25 icônes pixel (SVG + sprite), logo, favicon, `.ico`.
- Skill Claude `clem2k-design`, documentation et exemples.
