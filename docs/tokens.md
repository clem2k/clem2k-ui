# Tokens

> Généré par `scripts/build.py` depuis `tokens/tokens.json`. Ne pas éditer à la main.

## Couleurs et ombres

| token | dark | hc | light | usage |
|---|---|---|---|---|
| `--bg-000` | `#0a0d0b` | `#000000` | `#eaefe9` | Deepest ground: terminal panes, code blocks, the area behind the page shell. |
| `--bg-100` | `#0e120f` | `#050705` | `#f5f8f4` | Page background. Near-black with a faint green cast, never pure #000. |
| `--bg-200` | `#151a16` | `#0d110e` | `#ffffff` | Raised surfaces: panels, cards, menus, inputs. |
| `--bg-300` | `#1d241e` | `#161c17` | `#e0e8df` | Hover and pressed rows, active tab, the lowest ground any text sits on. |
| `--selection` | `#173d12` | `#123a0e` | `#d2f0c9` | Selected rows and text selection. ink and neon both read on it (8.6:1, 7.4:1). |
| `--line` | `#283129` | `#7d907f` | `#ccd6cb` | Hairlines and dividers between surfaces. Decorative in Dark; in High contrast it reaches 5:1 so surfaces are set apart by borders, not shade alone. |
| `--line-strong` | `#5f7261` | `#a3b5a5` | `#6c7f6e` | Control borders (inputs, secondary buttons, checkboxes): 3:1 or more on bg-000 to bg-300. |
| `--ink` | `#cfdccf` | `#f0f7f0` | `#1c241d` | Body text: soft phosphor white. 11:1 or more on bg-000 to bg-300. The default for every paragraph. |
| `--ink-strong` | `#eaf2ea` | `#ffffff` | `#0b100c` | Headings and emphasised words on bg-000 to bg-300. |
| `--ink-muted` | `#9cae9e` | `#c2d0c3` | `#4a5c4c` | Secondary text, metadata, timestamps, placeholders, comments in code. 7.5:1 or more on bg-000 to bg-200, 6.8:1 on bg-300 (Dark); 10.8:1 or more (High contrast). |
| `--neon` | `#3be81a` | `#4dff2b` | `#156b08` | The brand green from the profile pictures. Accents only: links, the prompt sign, cursor, focus ring, primary button fill, active indicators, success. Never for paragraphs. 9.6:1 or more on bg-000 to bg-300. Light: #156b08, a deep phosphor green that keeps 5.3:1 or more as text; the bright #3be81a is too pale on paper. |
| `--neon-soft` | `#a8f59a` | `#c4ffb8` | `#0f5a04` | Link hover and visited-free highlight text; a calmer green for longer accent runs (12:1 or more on all grounds). |
| `--on-neon` | `#0a0d0b` | `#000000` | `#ffffff` | Text and icons on a neon fill (primary button). 11.8:1. Light: white on the deep green (6.7:1). |
| `--bot` | `#f84818` | `#ff6a45` | `#c7380c` | Bot red-orange from the bot avatar's keys, kept exact. Fills, icons, borders and badges for anything said or done by a bot, and errors/danger. For TEXT use bot-text. |
| `--bot-text` | `#ff6a45` | `#ff8f70` | `#b3320a` | Bot and error TEXT on every ground: 5.6:1 or more on bg-000 to bg-300 (Dark), 7.7:1 or more (High contrast). |
| `--on-bot` | `#0a0d0b` | `#000000` | `#ffffff` | Text on a bot fill (destructive button, bot badge). 5.5:1. Light: white (5.3:1). |
| `--py-yellow` | `#ffd43b` | `#ffd43b` | `#7a5c00` | Python yellow from the header. Warnings, Python-related tags, highlighted search matches. 11:1 or more on all grounds. Light: #7a5c00 (dark ochre) so warnings stay readable on paper. |
| `--py-blue` | `#4b8bbe` | `#6aa6d8` | `#306998` | Python blue from the header, kept exact. Info fills, icons, borders, Python tags. For TEXT use py-blue-text. |
| `--py-blue-text` | `#6aa6d8` | `#8fc2ec` | `#2b5f8c` | Info and secondary-link TEXT on every ground: 6:1 or more (Dark), 9:1 or more (High contrast). |
| `--glass-fill` | `rgba(22, 28, 23, 0.8)` | `rgba(13, 17, 14, 0.94)` | `rgba(255, 255, 255, 0.85)` | Tint of every glass surface (Glass, NavBar, Toolbar, Sidebar, Dock, Menu, Toast, Dialog). 80% opaque: ink keeps 6.4:1 or more even over a pure white or neon area behind (7.7:1 typical); 94% in High contrast. Light: 85% white; ink keeps 11:1 even over black content behind. |
| `--glass-fill-hover` | `rgba(40, 50, 42, 0.78)` | `rgba(29, 36, 30, 0.96)` | `rgba(255, 255, 255, 0.95)` | Hover state of glass buttons. |
| `--glass-edge` | `rgba(207, 220, 207, 0.16)` | `rgba(207, 220, 207, 0.55)` | `rgba(28, 36, 29, 0.14)` | 1px rim and inner separators of glass surfaces. Decorative in Dark; a real 3:1 boundary in High contrast. |
| `--glass-sheen` | `rgba(255, 255, 255, 0.07)` | `rgba(255, 255, 255, 0)` | `rgba(255, 255, 255, 0.7)` | Top-down specular highlight that gives glass its liquid look. Off in High contrast. |
| `--hover-tint` | `rgba(207, 220, 207, 0.08)` | `rgba(207, 220, 207, 0.14)` | `rgba(28, 36, 29, 0.06)` | Hover fill of rows and links on glass (nav links, sidebar items, window controls, dock tiles). |
| `--hover-tint-strong` | `rgba(207, 220, 207, 0.12)` | `rgba(207, 220, 207, 0.2)` | `rgba(28, 36, 29, 0.1)` | Resting fill of dock tiles and stronger hover. |
| `--scrim` | `rgba(5, 7, 5, 0.55)` | `rgba(0, 0, 0, 0.75)` | `rgba(20, 30, 20, 0.35)` | Overlay behind dialogs and the command palette. |
| `--field-on-glass` | `rgba(10, 13, 11, 0.55)` | `rgba(0, 0, 0, 0.8)` | `rgba(255, 255, 255, 0.9)` | Background of a search field sitting on glass. |
| `--wall-dot` | `rgba(207, 220, 207, 0.1)` | `rgba(207, 220, 207, 0.1)` | `rgba(28, 36, 29, 0.12)` | Dot grid of the ck-wall backdrop. |
| `--focus-ring` | `0 0 0 2px #3be81a` | `0 0 0 3px #4dff2b` | `0 0 0 2px #156b08` | Keyboard focus on every interactive element: a solid 2px neon ring, 9.6:1 or more on every ground. High contrast: 3px. |
| `--glow` | `0 0 12px rgba(59, 232, 26, 0.35)` | `none` | `0 0 12px rgba(21, 107, 8, 0.25)` | Phosphor glow. Only on the active/primary element of a view (primary button hover, live cursor). Never on text blocks. Off in High contrast. |
| `--glass-shadow` | `0 8px 32px rgba(0, 0, 0, 0.45), inset 0 1px 0 rgba(255, 255, 255, 0.1)` | `0 8px 32px rgba(0, 0, 0, 0.6)` | `0 8px 32px rgba(20, 40, 20, 0.16), inset 0 1px 0 rgba(255, 255, 255, 0.9)` | Lift and inner top light of glass surfaces. The only drop shadow in the system. |

## Espacements, rayons, flou, polices

| token | valeur | usage |
|---|---|---|
| `--space-1` | `4px` | Icon-to-text gap, tag padding (vertical). |
| `--space-2` | `8px` | Button padding (vertical), gaps inside a row of controls. |
| `--space-3` | `16px` | Panel and card padding, gaps between stacked fields. |
| `--space-4` | `24px` | Gap between panels. |
| `--space-5` | `40px` | Gap between page sections. |
| `--radius-0` | `0px` | Terminal panes, code blocks, tables, the page shell. |
| `--radius-sm` | `2px` | Buttons, inputs, tags. |
| `--radius-md` | `4px` | Solid content containers: cards, alerts. The largest radius for anything that is not glass. |
| `--radius-lg` | `12px` | Glass that floats close to content: menus, toasts, tooltips, sidebar items, dock tiles. |
| `--radius-xl` | `20px` | Large glass: windows, dialogs, command palette, floating sidebar, dock. |
| `--radius-pill` | `999px` | Glass bars and controls: NavBar, Toolbar, SegmentedControl, glass buttons, search fields, switches, avatars. |
| `--blur-glass` | `24px` | backdrop-filter blur of every glass surface (with saturate 140%). |
| `--font-mono` | `"JetBrains Mono", ui-monospace, "SF Mono", Menlo, Consolas, monospace` |  |

## Styles de texte

Classe utilitaire `ck-t-<nom>` dans `tokens.css`.

| style | taille / interligne | graisse | usage |
|---|---|---|---|
| `display` | 40px / 48px | 700 | Page titles and hero lines. One per page. |
| `h1` | 28px / 36px | 700 | Section titles. |
| `h2` | 20px / 28px | 600 | Sub-sections, panel titles. |
| `h3` | 16px / 24px | 600 | Card titles, group labels inside panels. |
| `body` | 16px / 26px | 400 | All running text. Keep lines at 72 characters or fewer. |
| `small` | 13px / 20px | 400 | Metadata, captions, help text, table cells in dense views. |
| `code` | 15px / 24px | 400 | Code blocks and terminal output, on bg-000. |
| `label` | 12px / 16px | 600 | Uppercase labels, tags, button text, table headers. |
