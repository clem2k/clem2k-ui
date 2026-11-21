# Composants

41 composants React 18. Trois façons de les charger (voir [integration.md](integration.md)) :

- ES module : `import { Button, Window } from "clem2k-ui"` (+ `import "clem2k-ui/clem2k.css"`).
- Script global : React 18 UMD puis `dist/clem2k.js` → `window.clem2k.Button`…
- Sans React : les classes `ck-` en HTML pur (voir `examples/html-only.html`).

Les props exactes sont dans [`dist/clem2k.d.ts`](../dist/clem2k.d.ts). Exemples complets : `examples/web.html`, `examples/desktop.html`.

Règle d'or : **ce qui flotte est en verre et arrondi ; ce qui est posé est opaque et carré.**

## Sommaire

- **Fondations** : [Icon](#icon), [Glass](#glass)
- **Actions** : [Button](#button), [IconButton](#iconbutton), [SegmentedControl](#segmentedcontrol), [Switch](#switch)
- **Formulaires** : [TextField](#textfield), [TextArea](#textarea), [Select](#select), [Checkbox](#checkbox), [RadioGroup](#radiogroup), [Slider](#slider), [SearchField](#searchfield)
- **Navigation web** : [NavBar](#navbar), [Tabs](#tabs), [Breadcrumbs](#breadcrumbs), [Pagination](#pagination), [Footer](#footer), [Hero](#hero)
- **App desktop** : [Window](#window), [Toolbar](#toolbar), [Sidebar](#sidebar), [StatusBar](#statusbar), [Dock](#dock), [CommandPalette](#commandpalette), [Menu](#menu)
- **Contenu** : [Card](#card), [Badge](#badge), [Avatar](#avatar), [Kbd](#kbd), [Table](#table), [CodeBlock](#codeblock), [Terminal](#terminal), [EmptyState](#emptystate)
- **Feedback** : [Alert](#alert), [Toast](#toast), [Progress](#progress), [Spinner](#spinner), [Skeleton](#skeleton), [Tooltip](#tooltip), [Dialog](#dialog)

## Fondations

### Icon

Les 25 icônes pixel art clem2k en SVG inline, qui prennent la couleur du texte (`currentColor`).

Fournir : `name` (une des clés de `clem2k.Icon.names`), `size` (24 par défaut ; utiliser 16, 24 ou 48 seulement), `label` si l'icône est seule et porte du sens (sinon elle est décorative, `aria-hidden`).

- Colorer via le parent ou `color` : `ink` par défaut, `neon` actif, `bot-text` erreur/bot, `py-yellow` avertissement, `py-blue-text` info.
- Ne pas mettre à l'échelle à 18 ou 32px : les pixels bavent.

### Glass

Le matériau verre clem2k : fond teinté `glass-fill`, flou `blur-glass`, liseré `glass-edge`, reflet en haut et ombre `glass-shadow`. Base de tout ce qui flotte.

Fournir : `children`, `shape` (`"xl"` par défaut, `"lg"`, `"pill"`), `as` (balise), et tout attribut HTML.

- Uniquement pour le chrome : navigation, barres d'outils, sidebar, dock, menus, toasts, dialogs. Jamais derrière un paragraphe ou un tableau.
- Toujours du contenu derrière, sinon le verre ne se voit pas : c'est fait pour flotter au-dessus d'une page ou d'un fond d'écran.
- Respecte `prefers-reduced-transparency` (devient opaque `bg-200`) et le thème High contrast (quasi opaque).

## Actions

### Button

Bouton d'action, carré (`radius-sm`) et en capitales `label`, posé dans le contenu.

Fournir : `children` (verbe d'action), `variant` (`primary`, `secondary` par défaut, `ghost`, `danger`, `glass`), `size` (`sm`, `lg`), `icon` (nom d'Icon), `onClick`, `disabled`.

- Un seul `primary` (néon) par vue : l'action pour laquelle la page existe.
- `danger` (rouge bot) pour les actions destructrices, toujours confirmées par un Dialog.
- `glass` (pilule translucide) uniquement posé sur du verre ou sur une image ; voir le Hero.

### IconButton

Bouton carré ne contenant qu'une icône pixel.

Fournir : `icon`, `label` (obligatoire : sert d'`aria-label` et d'infobulle native), `variant` (`ghost` par défaut, `secondary`, `primary`, `glass`), `size` (`sm`), `onClick`.

- Dans une Toolbar ou une barre de titre, utiliser `ghost` ; `glass` pour un bouton flottant seul (fermer un panneau, retour en haut).

### SegmentedControl

Choix exclusif entre 2 à 5 vues, en pilule de verre ; l'option active passe en `neon`.

Fournir : `options` (chaînes ou `{value,label}`), `value`/`onChange` (contrôlé) ou `defaultValue`, `label` (nom du groupe pour les lecteurs d'écran).

- Pour changer de vue ou de filtre dans la même page. Pour naviguer entre des contenus distincts, utiliser Tabs.

### Switch

Interrupteur on/off à effet immédiat ; état actif en `neon` sur `selection`.

Fournir : `label`, `checked`/`onChange` ou `defaultChecked`, `disabled`.

- Effet immédiat uniquement (réglage appliqué tout de suite). Dans un formulaire validé par un bouton, utiliser Checkbox.

## Formulaires

### TextField

Champ texte d'une ligne avec libellé, aide et erreur ; fond `bg-000`, curseur néon, carré.

Fournir : `label`, `placeholder`, `help` ou `error` (message qui dit quoi faire), `prompt` (ajoute le `>` néon, pour les commandes), et les attributs `input` (`value`, `onChange`, `type`…).

- Le libellé est toujours visible ; le placeholder montre un exemple, jamais la consigne.
- Erreur : bordure `bot`, message `[err]` en `bot-text`.

### TextArea

Zone de texte multiligne, mêmes règles que TextField.

Fournir : `label`, `help`/`error`, attributs `textarea` (`rows`, `value`, `onChange`).

### Select

Liste déroulante native, habillée clem2k (chevron néon).

Fournir : `label`, `options` (chaînes ou `{value,label}`), `value`/`onChange` ou `defaultValue`, `help`/`error`.

- Au-delà de 12 options, préférer un SearchField filtrant ou la CommandPalette.

### Checkbox

Case à cocher carrée, cochée en `neon`.

Fournir : `label`, `checked`/`onChange` ou `defaultChecked`, `disabled`.

### RadioGroup

Choix exclusif entre 2 à 6 options visibles.

Fournir : `label` (légende du groupe), `options`, `value`/`onChange` ou `defaultValue`.

### Slider

Curseur de valeur continue ; la piste remplie est néon, la valeur s'affiche à droite.

Fournir : `label`, `min`, `max`, `step`, `value`/`onChange` ou `defaultValue`, `format` (affichage de la valeur).

### SearchField

Champ de recherche en pilule avec loupe pixel.

Fournir : `placeholder`, `label` (si pas de texte visible autour), `onGlass` quand il est posé sur du verre (NavBar, Toolbar), attributs `input`.

## Navigation web

### NavBar

Barre de navigation web en pilule de verre, collée en haut (`sticky`), flottant au-dessus du contenu.

Fournir : `brand` (texte, « clem2k » par défaut), `logo` (url, `logo-transparent.png`), `links` (`{label,href,current}`), `actions` (un Button `primary` `sm` au plus), `homeHref`.

- Liens en minuscules façon commande ; le lien courant en `neon`.
- 5 liens maximum. Au-delà, regrouper dans un Menu.

### Tabs

Onglets de contenu : soulignement et prompt `>` néon sur l'onglet actif.

Fournir : `tabs` (`{id,label,content}`), `value`/`onChange` ou `defaultValue`.

- Posé dans le contenu, donc pas de verre. Pour une simple bascule de vue, SegmentedControl.

### Breadcrumbs

Fil d'Ariane façon chemin de fichiers, séparé par `/`.

Fournir : `items` (`{label,href}` ; le dernier est la page courante, sans lien).

### Pagination

Pagination numérotée avec précédent/suivant ; page courante encadrée en `neon`.

Fournir : `pages`, `page`/`onChange` ou `defaultPage`.

### Footer

Pied de page web, posé et opaque (`bg-000`), en colonnes.

Fournir : `brand`, `tagline`, `legal`, `columns` (`{title,links:[{label,href}]}`), 4 colonnes maximum.

### Hero

En-tête de page d'accueil : surtitre, titre `display` avec prompt `>`, texte, actions, visuel à droite.

Fournir : `title`, `eyebrow`, `text`, `actions` (un `primary` `lg` + un `glass` `lg`), `aside` (logo, avatar ou visuel).

- Posé sur le fond `ck-wall` ou sur une image ; le texte reste opaque et ≥ 7:1.

## App desktop

### Window

Fenêtre d'application desktop : coque de verre `radius-xl`, barre de titre, sidebar, barre d'outils, contenu opaque et barre d'état.

Fournir : `title`, `sidebar` (un Sidebar), `toolbar` (une Toolbar), `children` (le contenu, sur `bg-100`), `statusbar` (une StatusBar), `titlebarStart`/`titlebarEnd` (contrôles en plus), `onMinimize`/`onMaximize`/`onClose`.

- Contrôles de fenêtre à droite (– □ ×), le × passe en rouge `bot` au survol.
- Le verre est réservé à la coque, la sidebar et la toolbar ; le contenu reste opaque pour la lecture.

### Toolbar

Barre d'outils flottante en pilule de verre.

Fournir : `children` (IconButton `ghost`, au plus un Button `primary` `sm`), `label`, et `clem2k.Toolbar.Separator` entre les groupes.

### Sidebar

Liste de sources latérale (desktop) en verre, avec sections, icônes et compteurs.

Fournir : `sections` (`{title,items:[{label,icon,href,current,count,onClick}]}`), `floating` (détachée, arrondie, pour une app sans Window), sinon collée au bord gauche d'une Window.

- Élément courant : fond néon léger, icône `neon`, texte `ink-strong`.

### StatusBar

Barre d'état en bas de fenêtre : opaque, `small`, en `ink-muted` ; un point néon signale la connexion.

Fournir : `left` et `right` (listes de textes ou nœuds), `online` (false pour masquer le point).

### Dock

Dock / barre d'apps flottante en verre, icônes pixel 24px, point néon sous les apps ouvertes, infobulle au survol.

Fournir : `items` (`{label,icon,current,onClick}` ou `"-"` pour un séparateur), `label`.

### CommandPalette

Palette de commandes (Ctrl K) en verre : saisie avec prompt `>`, filtrage, navigation flèches + Entrée.

Fournir : `items` (`{label,icon,hint}`), `onSelect(item)`, `placeholder`, `autoFocus`. L'app gère l'ouverture (dans un `.ck-overlay`) et Échap.

### Menu

Menu contextuel / déroulant en verre `radius-lg`, avec raccourcis clavier.

Fournir : `items` (`{label,icon,shortcut,danger,onClick}` ou `"-"`). Le positionnement est à la charge de l'app.

- Action destructrice en dernier, en `bot-text`, après un séparateur.

## Contenu

### Card

Carte de contenu posée : opaque `bg-200`, carrée (`radius-md`), filet `line`.

Fournir : `title`, `meta`, `children` (texte court), `actions`, `href` (toute la carte devient un lien, bordure néon au survol).

- Pas de verre : une carte contient du texte à lire.

### Badge

Étiquette d'état ou de catégorie, en capitales, liseré de la couleur du ton.

Fournir : `children` (un ou deux mots), `tone` (`neutral`, `ok`, `warn`, `info`, `err`, `bot`), `solid` (rempli, pour un seul état fort par vue), `icon`.

- Le mot porte le sens ; la couleur ne fait que le renforcer.

### Avatar

Avatar rond (image ou initiales en minuscules), avec point en ligne optionnel ; liseré `bot` pour les bots.

Fournir : `src`, `name` (alt et initiales), `size` (28, 40, 56), `online`, `bot`.

### Kbd

Touche de clavier pour raccourcis dans le texte, menus et palettes.

Fournir : `children` (nom de la touche).

### Table

Tableau de données posé, carré, en-têtes `label`, chiffres alignés à droite (tabulaires).

Fournir : `columns` (`{key,label,numeric,render}`), `rows`, `selected` (id ou index de la ligne sélectionnée), `caption`.

### CodeBlock

Bloc de code carré sur `bg-000`, numéros de ligne, bouton copier.

Fournir : `code`, `title` ou `lang`, `lineNumbers` (false pour masquer), `copy` (false pour masquer l'en-tête).

### Terminal

Sortie de terminal : prompt néon, préfixes de statut colorés, curseur `▋` clignotant (seule animation permanente autorisée).

Fournir : `lines` (chaînes, ou `{prompt,tone,text}` avec `tone` = `ok`/`warn`/`info`/`err`/`mut`), `prompt`, `cursor` (false pour masquer).

### EmptyState

État vide : icône pixel 48px, titre, explication, une action.

Fournir : `title`, `text`, `icon`, `action`. Un clin d'œil est permis dans le titre, jamais dans une erreur.

## Feedback

### Alert

Message dans la page, posé : bordure et icône de la couleur du ton, titre préfixé `[ok]` `[warn]` `[info]` `[err]`.

Fournir : `tone`, `title`, `children` (ce qu'il faut faire).

### Toast

Notification éphémère en verre `radius-lg`, en bas à droite.

Fournir : `children` (une phrase), `tone` (`ok` par défaut, `err`, `warn`, `info`), `action` (un Button `ghost` `sm`), `onClose`. L'app gère la pile et la durée (5 s, jamais pour une erreur).

### Progress

Barre de progression en blocs, façon téléchargement terminal ; sans `value` elle est indéterminée.

Fournir : `value` (0–100), `label`.

### Spinner

Indicateur d'attente textuel `| / - \` en néon, suivi d'un libellé.

Fournir : `label`. Au-delà de 2 s, préférer Progress.

### Skeleton

Placeholder de chargement qui reprend la forme du contenu à venir.

Fournir : `width`, `height`, `circle`.

### Tooltip

Infobulle en verre au survol ou au focus.

Fournir : `content` (quelques mots), `children` (l'élément déclencheur, focusable), `open` (forcer l'affichage).

### Dialog

Boîte de dialogue modale en verre `radius-xl`, voile sombre, boutons en pilule, Échap pour fermer.

Fournir : `open`, `title` (question explicite), `children`, `actions` (Annuler + action), `onClose`.

- Action destructrice : bouton `danger` à droite, libellé = le verbe (« Supprimer »), jamais « OK ».
