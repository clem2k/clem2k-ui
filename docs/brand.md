# Charte clem2k

> Copie du guide de marque du design system de référence (artefact Claude « clem2k »). En cas de divergence, `tokens/tokens.json` fait foi pour les valeurs.

**clem2k** (toujours en minuscules) est un système sombre, monospace, inspiré des terminaux et de l'esthétique Matrix — mais **lisible d'abord, toujours**. Le vert néon des avatars est un signal, pas un papier peint : il marque ce qui est actif, cliquable ou vivant ; le texte courant reste en blanc phosphore doux.

## Principes

- **Lisible avant tout.** Le texte courant est en `ink` sur `bg-100` (13:1). Chaque couleur de texte atteint au moins 4.5:1 sur tous les fonds, et 7:1 en High contrast. Jamais de paragraphe en `neon`, jamais de texte qui défile, scintille ou « pleut ».
- **Un seul néon à la fois.** Dans une vue, `neon` signale l'élément principal (bouton primaire, onglet actif, curseur, prompt). Si tout est vert, plus rien ne l'est.
- **Terminal, pas cosplay.** Filets fins, une seule police mono. Pas de glitch, pas de scanlines, pas de pluie de caractères dans l'interface.
- **Ce qui flotte est en verre et arrondi ; ce qui est posé est opaque et carré.** Le verre (barres, sidebar, dock, menus, toasts, dialogs, fenêtres) prend `radius-lg`, `radius-xl` ou `radius-pill`. Le contenu (texte, cartes, tableaux, code, terminal, champs) reste sur `radius-0` à `radius-md`.
- **Le glow se mérite.** `glow` uniquement sur l'élément actif ou primaire au survol. Jamais sur un bloc de texte.

## Couleur

Trois thèmes : **Dark** (défaut), **Light** (`light` : papier légèrement vert, vert phosphore profond `#156b08` comme accent, verre blanc) et **High contrast** (`hc`) — texte ≥ 7:1 partout, filets `line` visibles (5:1), anneau de focus 3px, pas de `glow`. Les noms de tokens sont identiques : basculer avec `data-theme="light"`, `"hc"` ou `"auto"` (suit le réglage clair/sombre du système).

- Fonds, du plus profond au plus élevé : `bg-000` (panneaux terminal, blocs de code) → `bg-100` (page) → `bg-200` (panneaux, cartes, champs) → `bg-300` (survol, ligne active). Ne jamais utiliser `#000` pur.
- Texte : `ink` pour tout le texte courant, `ink-strong` pour les titres, `ink-muted` pour les métadonnées, horodatages, placeholders et commentaires de code. En Dark, `ink-muted` dépasse 7:1 sur `bg-000` à `bg-200` (6.8:1 sur `bg-300`).
- Accent : `neon` pour liens, prompt `>` ou `$`, curseur, anneau de focus, remplissage du bouton primaire (texte `on-neon`), indicateurs actifs et succès. `neon-soft` pour le survol des liens et les surlignages plus longs.
- Sélection : `selection` en fond, le texte garde sa couleur.
- Bordures : `line` pour les séparateurs décoratifs, `line-strong` pour toute bordure de contrôle (3:1 minimum).
- **Bots** : `bot` (rouge-orangé de l'avatar bot) marque tout ce qu'un bot dit ou fait, et les erreurs / actions destructrices. `bot` sert aux remplissages, icônes et bordures (texte posé dessus : `on-bot`) ; pour du TEXTE rouge, toujours `bot-text`, lisible sur tous les fonds.
- **Python** : `py-yellow` pour les avertissements, les tags Python et les correspondances de recherche ; `py-blue` pour les remplissages, icônes et bordures d'info ; pour du TEXTE bleu, `py-blue-text`.
- Statuts (texte) : succès `neon`, avertissement `py-yellow`, info `py-blue-text`, erreur `bot-text`. Toujours accompagnés d'un mot ou d'un préfixe (`[ok]`, `[warn]`, `[info]`, `[err]`) — jamais la couleur seule.

## Typographie

Une seule famille : `mono` (JetBrains Mono, servie par Google Fonts ; repli `ui-monospace`). Elle sert à tout : titres, prose, UI, code.

- `display` pour une ligne d'accroche par page, `h1` pour les sections, `h2` pour les panneaux, `h3` pour les cartes.
- `body` (16/26) pour toute la prose. Limiter les lignes à 72 caractères (`max-width: 72ch`).
- `small` pour les métadonnées et tableaux denses, `code` pour les blocs de code sur `bg-000`.
- `label` en MAJUSCULES pour étiquettes, tags, en-têtes de tableau et texte de bouton.
- Les titres peuvent porter un préfixe de prompt en `neon` : `> Réseau`, `$ deploy`, `## Notes`. Le texte du titre reste en `ink-strong`.

Exemple :

```
> clem2k@viper:~$ docker compose ps
[ok]   vision-proxy     running
[warn] vision-backup    restarting
[err]  bot-sentinel     exited (1)
```

Ici : prompt en `neon`, sortie en `ink`, `[ok]` en `neon`, `[warn]` en `py-yellow`, `[err]` en `bot-text`, le tout sur `bg-000`.

## Espacement, formes, profondeur

- Grille de 4px : `space-1` (4) écart icône/texte, `space-2` (8) padding vertical des boutons, `space-3` (16) padding des panneaux, `space-4` (24) entre panneaux, `space-5` (40) entre sections.
- Rayons du contenu : `radius-0` pour terminal, blocs de code, tableaux ; `radius-sm` pour boutons, champs, tags ; `radius-md` pour cartes et alertes.
- Rayons du verre : `radius-lg` (menus, toasts, infobulles, éléments de sidebar), `radius-xl` (fenêtres, dialogs, palette, dock), `radius-pill` (NavBar, Toolbar, SegmentedControl, boutons `glass`, recherche).
- Profondeur par les fonds et les filets dans le contenu. Seules ombres : `focus-ring`, `glow` et `glass-shadow` (réservée au verre).

## Verre (Liquid Glass façon clem2k)

- Matériau : `glass-fill` (80 % opaque), flou `blur-glass` + saturation 140 %, liseré `glass-edge`, reflet `glass-sheen`, ombre `glass-shadow`. Utiliser le composant `Glass` ou la classe `.ck-glass`, jamais une recette refaite à la main.
- **Uniquement pour le chrome** : navigation, barres d'outils, sidebar, dock, menus, toasts, infobulles, dialogs, coques de fenêtre. Jamais derrière un paragraphe, une carte, un tableau ou du code.
- Lisibilité : `ink` garde 6.4:1 sur le verre même au-dessus d'une zone blanche ou néon (7.7:1 en usage normal). Sur du verre, `ink-muted` seulement pour les libellés de section et les compteurs ; tout texte à lire en `ink` ou `ink-strong`.
- Le verre a besoin de quelque chose derrière : fond `ck-wall` (halos néon/bleu Python et grille de points), une image ou le contenu qui défile.
- `prefers-reduced-transparency` rend le verre opaque (`bg-200`) ; le thème High contrast le rend quasi opaque, coupe le reflet et renforce le liseré.

## Composants

Bundle React 18 : `window.clem2k` (classes CSS préfixées `ck-`). 41 composants :

- Fondations : `Icon` (les 25 icônes pixel en SVG inline, tailles 12/24/36/48), `Glass`.
- Actions : `Button`, `IconButton`, `SegmentedControl`, `Switch`.
- Formulaires : `TextField`, `TextArea`, `Select`, `Checkbox`, `RadioGroup`, `Slider`, `SearchField`.
- Navigation web : `NavBar`, `Hero`, `Tabs`, `Breadcrumbs`, `Pagination`, `Footer`.
- App desktop : `Window`, `Toolbar`, `Sidebar`, `StatusBar`, `Dock`, `CommandPalette`, `Menu`.
- Contenu : `Card`, `Badge`, `Avatar`, `Kbd`, `Table`, `CodeBlock`, `Terminal`, `EmptyState`.
- Feedback : `Alert`, `Toast`, `Progress`, `Spinner`, `Skeleton`, `Tooltip`, `Dialog`.

Page web type : fond `ck-wall`, `NavBar` en verre collée en haut, `Hero`, sections de `Card` sur `bg-100`, `Footer`. App desktop type : `Window` avec `Sidebar`, `Toolbar`, contenu opaque, `StatusBar` ; `CommandPalette` sur Ctrl K ; `Dock` si plusieurs apps.
- Focus : `focus-ring` sur tout élément focusable, sans exception.
- Animation : sobre. Le curseur clignotant (`▋` en `neon`) est la seule animation permanente autorisée. Respecter `prefers-reduced-motion`.

## Logo

Le logo clem2k est le buste en costume à cravate néon (`assets/logo/`). Son liseré `ink` le détache sur tous les fonds.

- `logo-dark.png` : version par défaut, sur `bg-100` (avatar d'app, réseaux, carte de visite numérique).
- `logo-transparent.png` : fond transparent, pour poser sur `bg-000` à `bg-300` ou sur un fond clair.
- `logo-bust.png` : recadré sur le haut du buste, pour les tailles 32–48px.
- `favicon-16.png` : à 16px le buste devient illisible, on passe à la cravate pixel en `neon`.
- `apple-touch-icon.png` (180px). Le fichier `clem2k.ico` (16→256) suit les mêmes règles.
- Zone de protection : au moins `space-3` autour. Ne pas recolorer, étirer, ni ajouter de glow.

## Imagerie

- avatar actuel (dans le design system, pas dans ce dépôt) : avatar actuel, à utiliser partout où clem2k apparaît.
- figurine Pop (dans le design system) : la figurine, réservée aux très grands formats (bannière d'événement, affiche, écran de présentation) où ses détails se lisent ; jamais en petit avatar.
- ancien avatar (dans le design system) : ancien avatar (cravate pixel), fond blanc ; à réserver aux contextes rétro ou historiques.
- avatar bot (dans le design system) : avatar des bots. Toujours associé à la couleur `bot`.
- bannière Python (dans le design system) : bannière (format très large, ~2.75:1). En-tête de profil ou de page d'accueil uniquement ; ne pas superposer de texte dessus.
- Les illustrations vivent dans des cadres `radius-0` ou `radius-md`, sans bordure néon ajoutée.

## Iconographie

Icônes pixel art maison dans `dist/icons/` (et `dist/icons.svg`) (25 icônes, grille 12×12 de pixels 2px, viewBox 24). Encre `ink` par défaut ; recolorer en inline : `neon` pour l'état actif, `bot` pour un bot ou une erreur, `py-yellow` pour un avertissement, `py-blue` pour une info.

- Tailles multiples de 12 seulement (12, 24, 36, 48) : le composant `Icon` arrondit automatiquement. En `<img>`, ajouter `image-rendering: pixelated`.
- Toujours une icône + un libellé pour les actions ; icône seule uniquement avec `aria-label` et infobulle.
- `tie.svg` (la cravate pixel) est la marque clem2k : favicon, signature.
- Les glyphes texte mono (`>`, `$`, `▋`, `[ok]`) restent bienvenus dans le flux de texte. Pas d'emoji dans l'interface.

## Ton

- Direct, technique, un peu de clin d'œil geek bienvenu (`> wake up, neo`) — dans les titres et états vides, jamais dans les messages d'erreur.
- Tutoiement en français. Les messages d'erreur disent quoi faire : `[err] port 8080 déjà utilisé — arrête le conteneur ou change le port`.
- Minuscules pour l'UI façon commande (`deploy`, `logs`), casse normale pour la prose.
