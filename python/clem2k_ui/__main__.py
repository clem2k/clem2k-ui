"""python -m clem2k_ui : affiche la version, le dossier statique et un aperçu des couleurs."""
from . import STATIC_DIR, __version__, tokens

t = tokens()
print(f"clem2k-ui {__version__}")
print(f"static: {STATIC_DIR}")
for name in ("bg-100", "ink", "ink-muted", "neon", "py-yellow", "py-blue-text", "bot-text"):
    r, g, b = (int(t[name][i:i + 2], 16) for i in (1, 3, 5))
    print(f"\x1b[38;2;{r};{g};{b}m██\x1b[0m {name:<13} {t[name]}")
