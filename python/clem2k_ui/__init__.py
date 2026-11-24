"""clem2k-ui for Python projects.

    pip install "clem2k-ui @ git+https://github.com/clem2k/clem2k-ui"

Web (FastAPI / Starlette):   clem2k_ui.mount(app)  then  {{ clem2k_head() }} in templates
Flask:                       clem2k_ui.flask_blueprint()
Qt (PySide6 / PyQt6):        clem2k_ui.apply_qt(app)
Rich / Textual:              clem2k_ui.rich_theme(), clem2k_ui.textual_theme()
Raw values:                  clem2k_ui.tokens("dark")["neon"]  ->  "#3be81a"
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

__all__ = ["STATIC_DIR", "tokens", "qss", "icon_svg", "head_tags", "mount", "flask_blueprint",
           "apply_qt", "rich_theme", "textual_theme"]
__version__ = "0.2.0"

_here = Path(__file__).resolve().parent
# Installed wheel: files live in clem2k_ui/static. Editable / repo checkout: fall back to <repo>/dist.
STATIC_DIR: Path = _here / "static" if (_here / "static" / "clem2k.css").exists() else _here.parent.parent / "dist"


@lru_cache(maxsize=None)
def _resolved() -> dict:
    return json.loads((STATIC_DIR / "tokens.json").read_text(encoding="utf-8"))


def tokens(theme: str = "dark") -> dict[str, str]:
    """Every token for a theme ("dark", "hc" or "light"): colors, shadows, spacing, radii, blur, fonts."""
    data = _resolved()
    return {**data["global"], **data["themes"][theme]}


def qss(theme: str = "dark") -> str:
    """Qt stylesheet for "dark", "hc" or "light". Glass becomes opaque bg-200 (Qt has no backdrop blur)."""
    name = "clem2k.qss" if theme == "dark" else f"clem2k-{theme}.qss"
    return (STATIC_DIR / name).read_text(encoding="utf-8")


def icon_svg(name: str, size: int = 24, color: str | None = None) -> str:
    """Inline pixel icon. size is snapped to a multiple of 12 so pixels stay crisp."""
    size = 12 if size < 24 else round(size / 12) * 12
    svg = (STATIC_DIR / "icons" / f"{name}.svg").read_text(encoding="utf-8")
    svg = svg.replace('width="24" height="24"', f'width="{size}" height="{size}"', 1)
    if color:
        svg = svg.replace('fill="currentColor"', f'fill="{color}"', 1)
    return svg


def head_tags(prefix: str = "/clem2k", react: bool = False, theme: str | None = None) -> str:
    """<link>/<script> tags for an HTML <head>. react=True also loads React 18 + the components.
    theme: "dark" (default), "hc", "light" or "auto" (follows the OS)."""
    tags = [f'<link rel="stylesheet" href="{prefix}/clem2k.css">',
            f'<link rel="icon" href="{prefix}/logo/clem2k.ico">']
    if react:
        tags += ['<script src="https://cdn.jsdelivr.net/npm/react@18.3.1/umd/react.production.min.js"></script>',
                 '<script src="https://cdn.jsdelivr.net/npm/react-dom@18.3.1/umd/react-dom.production.min.js"></script>',
                 f'<script src="{prefix}/clem2k.js"></script>']
    if theme:
        tags.append(f'<script>document.documentElement.dataset.theme="{theme}"</script>')
    return "\n".join(tags)


def mount(app, path: str = "/clem2k", templates=None) -> None:
    """FastAPI / Starlette: serve the kit under `path`; optionally register clem2k_head() in Jinja2Templates."""
    from starlette.staticfiles import StaticFiles
    app.mount(path, StaticFiles(directory=STATIC_DIR), name="clem2k")
    if templates is not None:
        from markupsafe import Markup
        templates.env.globals["clem2k_head"] = lambda **kw: Markup(head_tags(path, **kw))
        templates.env.globals["clem2k_icon"] = lambda *a, **kw: Markup(icon_svg(*a, **kw))


def flask_blueprint(url_prefix: str = "/clem2k"):
    """Flask: app.register_blueprint(clem2k_ui.flask_blueprint()); templates get clem2k_head() / clem2k_icon()."""
    from flask import Blueprint
    from markupsafe import Markup
    bp = Blueprint("clem2k", __name__, static_folder=str(STATIC_DIR), static_url_path="", url_prefix=url_prefix)

    @bp.app_context_processor
    def _ctx():
        return {"clem2k_head": lambda **kw: Markup(head_tags(url_prefix, **kw)),
                "clem2k_icon": lambda *a, **kw: Markup(icon_svg(*a, **kw))}
    return bp


def apply_qt(app, theme: str = "dark") -> None:
    """PySide6 / PyQt6: apply the stylesheet and prefer JetBrains Mono if it is installed."""
    try:
        from PySide6.QtGui import QFont
    except ImportError:  # pragma: no cover
        from PyQt6.QtGui import QFont
    font = QFont("JetBrains Mono")
    font.setStyleHint(QFont.StyleHint.Monospace)
    app.setFont(font)
    app.setStyleSheet(qss(theme))


def rich_theme(theme: str = "dark"):
    """Rich Theme with styles ok / warn / info / err / muted / prompt / accent."""
    from rich.theme import Theme
    t = tokens(theme)
    return Theme({"ok": t["neon"], "warn": t["py-yellow"], "info": t["py-blue-text"], "err": t["bot-text"],
                  "muted": t["ink-muted"], "prompt": f"bold {t['neon']}", "accent": t["neon"],
                  "repr.number": t["py-yellow"], "repr.str": t["neon-soft"]})


def textual_theme(theme: str = "dark"):
    """Textual Theme (textual >= 0.86): app.register_theme(textual_theme()); app.theme = "clem2k"."""
    from textual.theme import Theme
    t = tokens(theme)
    return Theme(name="clem2k" if theme == "dark" else f"clem2k-{theme}", dark=theme != "light",
                 primary=t["neon"], secondary=t["py-blue"], accent=t["neon-soft"], warning=t["py-yellow"],
                 error=t["bot-text"], success=t["neon"], foreground=t["ink"], background=t["bg-100"],
                 surface=t["bg-200"], panel=t["bg-300"])
