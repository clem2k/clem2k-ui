# Intégration

Trois choses à retenir, quel que soit le projet :

1. Charger **`clem2k.css`** (tokens + composants) ou, si tu as déjà ton CSS, **`tokens.css`** seul.
2. Poser `data-theme="dark"` (défaut) ou `data-theme="hc"` sur `<html>`.
3. Épingler une **version** (`v0.1.0`) : tes projets ne bougent pas tant que tu ne mets pas à jour.

## Comment récupérer le kit

| méthode | commande | quand |
|---|---|---|
| npm depuis GitHub | `npm i github:clem2k/clem2k-ui#v0.1.0` | projets JS/TS |
| pip depuis GitHub | `pip install "clem2k-ui @ git+https://github.com/clem2k/clem2k-ui@v0.1.0"` | projets Python |
| sous-module git | `git submodule add https://github.com/clem2k/clem2k-ui vendor/clem2k-ui` | n'importe quoi, sans gestionnaire de paquets |
| CDN jsDelivr | `https://cdn.jsdelivr.net/gh/clem2k/clem2k-ui@v0.1.0/dist/clem2k.css` | sites statiques (dépôt public uniquement) |
| VISION | sers `dist/` derrière Traefik, ex. `https://ui.<ton-domaine>/v0.1.0/clem2k.css` | dépôt privé, homelab |

Mettre à jour : changer le tag (`#v0.2.0`, `@v0.2.0`) puis réinstaller ; sous-module : `git -C vendor/clem2k-ui checkout v0.2.0`.

## HTML statique (Hugo, Jekyll, Eleventy, pages à la main)

```html
<!doctype html>
<html lang="fr" data-theme="dark">
<head>
  <link rel="stylesheet" href="/vendor/clem2k-ui/dist/clem2k.css">
  <link rel="icon" href="/vendor/clem2k-ui/assets/logo/clem2k.ico">
</head>
<body class="ck-wall">
  <nav class="ck-glass ck-nav">…</nav>
  <main style="background:var(--bg-100)">…</main>
</body>
</html>
```

Classes principales : `ck-glass` (+ `ck-glass-lg`, `ck-glass-pill`), `ck-btn ck-btn-primary|secondary|ghost|danger|glass`, `ck-input`, `ck-field`/`ck-label`/`ck-help`, `ck-card`, `ck-badge ck-badge-ok|warn|info|err|bot`, `ck-table`, `ck-code`, `ck-term`, `ck-alert ck-alert-*`, `ck-nav`, `ck-tabs`, `ck-footer`, typo `ck-t-display|h1|h2|h3|body|small|code|label`. Voir `examples/html-only.html`.

Icônes en HTML pur (héritent de la couleur du texte) :

```html
<svg class="ck-icon" width="24" height="24"><use href="/vendor/clem2k-ui/dist/icons.svg#terminal"/></svg>
```

## React (Vite, Next, Remix…)

```jsx
import "clem2k-ui/clem2k.css";
import { Window, Sidebar, Toolbar, IconButton, StatusBar, Table } from "clem2k-ui";
```

- Next.js : importer le CSS dans `app/layout.tsx`, mettre `<html data-theme="dark">`. Les composants interactifs utilisent des hooks : fichiers `"use client"`.
- Types : fournis (`dist/clem2k.d.ts`).
- Pas de bundler ? Charger React 18 UMD puis `dist/clem2k.js` → `window.clem2k` (voir `examples/web.html`).

## Tailwind

```js
// tailwind.config.js
module.exports = { presets: [require("clem2k-ui/tailwind")], content: ["./src/**/*.{html,jsx,tsx}"] };
```

Charger aussi `clem2k-ui/tokens.css` (les classes pointent vers les variables CSS, donc le thème `hc` marche tout seul). Exemples : `bg-bg-100 text-ink border-line-strong rounded-sm`, `text-neon`, `rounded-xl backdrop-blur-glass bg-glass-fill`, `text-ck-body`, `p-ck-3`, `shadow-glass-shadow`.

## FastAPI / Starlette

```python
from fastapi.templating import Jinja2Templates
import clem2k_ui

templates = Jinja2Templates(directory="templates")
clem2k_ui.mount(app, "/clem2k", templates=templates)
```

Dans le template : `{{ clem2k_head() }}` (CSS + favicon), `{{ clem2k_head(react=True) }}` pour aussi charger les composants React, `{{ clem2k_icon("server", 24) }}` pour une icône inline. Voir `examples/fastapi/`.

## Flask

```python
import clem2k_ui
app.register_blueprint(clem2k_ui.flask_blueprint())   # sert /clem2k/... ; clem2k_head() et clem2k_icon() dans les templates
```

## Django

`STATICFILES_DIRS = [clem2k_ui.STATIC_DIR]` puis `{% static 'clem2k.css' %}` dans le template de base.

## Desktop web (Tauri, Electron, pywebview)

Comme le web. Le verre fonctionne (`backdrop-filter`). Pour une vraie fenêtre translucide, rendre la fenêtre native transparente et poser `ck-wall` ou un fond d'écran derrière la `Window`.

## Desktop Qt (PySide6 / PyQt6)

```python
import clem2k_ui
clem2k_ui.apply_qt(app)            # ou apply_qt(app, "hc")
button.setProperty("variant", "primary")   # primary | danger | ghost
label.setProperty("role", "muted")         # muted | h1 | h2
```

Qt n'a pas de flou d'arrière-plan : le verre devient opaque `bg-200` avec le liseré `glass-edge`. Installer JetBrains Mono sur le système. Voir `examples/pyside/`.

## Terminal (Rich, Textual)

```python
from rich.console import Console
console = Console(theme=clem2k_ui.rich_theme())
console.print("[ok][ok][/ok] backup terminé   [err][err][/err] sentinel arrêté")

app.register_theme(clem2k_ui.textual_theme()); app.theme = "clem2k"   # Textual >= 0.86
```

## Valeurs brutes

- JS : `import tokens from "clem2k-ui/tokens.json"` → `tokens.themes.dark.neon`.
- Python : `clem2k_ui.tokens("dark")["neon"]`.
- Tout autre outil (Figma, Excalidraw, matplotlib, Grafana…) : [tokens.md](tokens.md).
