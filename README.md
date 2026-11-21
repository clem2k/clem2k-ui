# clem2k-ui

Le design system **clem2k** en kit réutilisable : esthétique terminal / Matrix **lisible d'abord**, chrome en verre façon Liquid Glass, une seule police mono, des icônes pixel.

![règle d'or](https://img.shields.io/badge/r%C3%A8gle-ce%20qui%20flotte%20%3D%20verre%20et%20arrondi%2C%20ce%20qui%20est%20pos%C3%A9%20%3D%20opaque%20et%20carr%C3%A9-3be81a?labelColor=0e120f)

| | |
|---|---|
| Tokens | 2 thèmes (`dark` par défaut, `hc` haut contraste), couleurs, typo, espacements, rayons, verre |
| CSS | `dist/clem2k.css` = tokens + styles des composants, classes `ck-` utilisables sans React |
| React 18 | 41 composants web + desktop (`NavBar`, `Hero`, `Window`, `Sidebar`, `Dock`, `CommandPalette`…) en ES module ou script global |
| Tailwind | preset branché sur les variables CSS |
| Python | paquet `clem2k_ui` : FastAPI/Starlette, Flask, PySide/PyQt (QSS), Rich, Textual |
| Icônes | 25 icônes pixel 12×12 en SVG (`currentColor`) + sprite |
| Logo | buste à cravate néon, favicon `.ico`, apple-touch-icon |
| Claude | skill `clem2k-design` pour que Claude applique le système partout |

## Démarrage rapide

### HTML statique / n'importe quel site

```html
<html data-theme="dark">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/clem2k/clem2k-ui@v0.1.0/dist/clem2k.css">
<button class="ck-btn ck-btn-primary">Déployer</button>
```

(Le CDN jsDelivr ne marche que si le dépôt est public ; sinon copie `dist/` dans ton projet ou sers-le depuis VISION.)

### React / Vite / Next

```bash
npm i github:clem2k/clem2k-ui#v0.1.0
```

```jsx
import "clem2k-ui/clem2k.css";
import { NavBar, Hero, Button } from "clem2k-ui";

<Button variant="primary" icon="play">Déployer</Button>
```

### Python

```bash
pip install "clem2k-ui[fastapi] @ git+https://github.com/clem2k/clem2k-ui@v0.1.0"
```

```python
import clem2k_ui
clem2k_ui.mount(app, "/clem2k", templates=templates)   # FastAPI : puis {{ clem2k_head() }} dans le <head>
clem2k_ui.apply_qt(qapp)                                # PySide6 / PyQt6
console = Console(theme=clem2k_ui.rich_theme())         # Rich : [ok] [warn] [info] [err]
```

Tous les cas (Flask, Django, Tailwind, Tauri/Electron, Textual, sous-module git…) : **[docs/integration.md](docs/integration.md)**.

## Exemples

Ouvre-les directement dans un navigateur :

- [`examples/web.html`](examples/web.html) : page d'accueil (NavBar en verre, Hero, cartes, terminal, formulaire, footer, bascule de thème).
- [`examples/desktop.html`](examples/desktop.html) : app desktop (Window, Sidebar, Toolbar, Tabs, Table, StatusBar, Dock, Ctrl K, Dialog, Toast).
- [`examples/html-only.html`](examples/html-only.html) : les mêmes classes sans React.
- [`examples/fastapi/`](examples/fastapi) et [`examples/pyside/`](examples/pyside).

## Documentation

| doc | contenu |
|---|---|
| [docs/brand.md](docs/brand.md) | la charte : principes, couleur, typo, verre, logo, icônes, ton |
| [docs/tokens.md](docs/tokens.md) | tous les tokens et leurs valeurs (généré) |
| [docs/components.md](docs/components.md) | les 41 composants : quand les utiliser, props, à faire / à éviter |
| [docs/integration.md](docs/integration.md) | intégrer le kit dans chaque type de projet |
| [docs/accessibility.md](docs/accessibility.md) | contrastes, verre, mouvement, clavier |
| [docs/claude.md](docs/claude.md) | le skill Claude et le snippet `CLAUDE.md` pour tes projets |
| [docs/maintenance.md](docs/maintenance.md) | modifier les tokens, rebuild, versions, synchro avec le design system |

## Structure

```
tokens/tokens.json      source unique des valeurs
src/                    styles et composants sources, grilles des icônes
scripts/build.py        génère dist/ et docs/tokens.md (Python standard, zéro dépendance)
dist/                   fichiers à consommer (versionnés, ne pas éditer)
assets/logo/            logo, favicon, ico
python/clem2k_ui/       paquet Python
skills/clem2k-design/   skill Claude
examples/               démos web, desktop, HTML pur, FastAPI, PySide
docs/                   documentation
```

## Marque

« clem2k » s'écrit toujours en minuscules. clem2k est une marque déposée : le logo et le nom ne sont pas réutilisables hors des projets de clem2k. Aucune licence open source n'est appliquée au dépôt pour l'instant.
