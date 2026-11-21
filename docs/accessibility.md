# Accessibilité et lisibilité

clem2k est fait pour être lu longtemps. Ces règles ne se négocient pas.

## Contrastes (thème dark)

| texte | fond | ratio |
|---|---|---|
| `ink` | `bg-000` → `bg-300` | 13.8 → 11.2:1 |
| `ink-strong` | `bg-000` → `bg-300` | 17.1 → 13.9:1 |
| `ink-muted` | `bg-000` → `bg-200` / `bg-300` | ≥ 7.5:1 / 6.8:1 |
| `neon` | `bg-000` → `bg-300` | 11.9 → 9.6:1 |
| `bot-text` | tous fonds | ≥ 5.6:1 |
| `py-blue-text` | tous fonds | ≥ 6:1 |
| `py-yellow` | tous fonds | ≥ 11:1 |
| `on-neon` sur `neon` | bouton primaire | 11.8:1 |
| `on-bot` sur `bot` | bouton danger | 5.5:1 |

Le thème **`hc`** monte tout le texte à 7:1 minimum (AAA), rend les filets visibles (5:1), le verre quasi opaque et l'anneau de focus à 3px.

`bot` et `py-blue` (couleurs d'origine) restent pour les remplissages, icônes et bordures ; pour du **texte**, toujours `bot-text` et `py-blue-text`.

## Verre

- `glass-fill` est opaque à 80 % : `ink` garde 6.4:1 même si une zone blanche ou néon passe derrière (7.7:1 en usage normal).
- Sur du verre, `ink-muted` seulement pour libellés de section et compteurs (peut tomber à 3.9:1 sur fond très clair).
- Jamais de texte long sur du verre. Le verre est pour le chrome.
- `prefers-reduced-transparency: reduce` → verre opaque `bg-200`.

## Statuts

Toujours un mot ou un préfixe en plus de la couleur : `[ok]`, `[warn]`, `[info]`, `[err]`. Succès (vert) et erreur (rouge-orangé) diffèrent aussi en clarté.

## Clavier et focus

- `focus-ring` (anneau néon plein) sur tout élément focusable, sans exception.
- `CommandPalette` : flèches + Entrée ; `Dialog` : Échap ; `IconButton` exige un `label`.

## Mouvement

- Seule animation permanente : le curseur `▋` du `Terminal`.
- `prefers-reduced-motion: reduce` coupe le curseur, les skeletons, la barre indéterminée et le spinner.
- Pas de pluie de code animée dans une interface.

## Texte

- Corps 16/26, lignes ≤ 72 caractères.
- Icônes en multiples de 12 px uniquement (sinon les pixels bavent).
