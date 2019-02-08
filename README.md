# PFE 2018 : Seul on va plus vite, à plusieurs on va plus loin ! Est-ce vrai pour l'assemblage des génomes ?

## Etudiant

- Yann Garbé

## Auteur / Encadrant du sujet

- Pierre Marijon de l'équipe Bonsai - CRIStAL

    - get_all afin d'obtenir l tous les intervals et non le plus long

## HOW TO

### Français

Le but de ce programme est de réaliser différents types d'assemblage d'analyses d'overlappers.

Pour lancer le programme, placez-vous dans le répertoire `src` et lancer le fichier `Analyser.py` avec python.

#### Paramètres d'entrée

Voici les paramètres principaux : 

- `Analyse type` [gentle, strict, max, custom]: le type d'analyse à réaliser. Cela peut être gentle, strict, max ou custom (voir le point `Les Types d'analyses` pour avoir plus d'informations sur ces analyses)

- `Output type` [paf, mhap, hisea]: le type de fichier de retour. Cela peut être paf, mhap ou hisea (note : hisea n'est pas implémenté pour le moment)

- `Input files` [chemins]: les différents fichiers d'entrées à analyser : ils ne peuvent être que d'extension mhap et paf pour le moment.

D'autres paramètres peuvent également être utilisés :

- `Statistics` [--stats / -s]: Permet, au lieu d'effectuer une analyse, d'afficher certaines statistiques sur les fichiers d'entrée

- `Get all` [--get_all / -all]: Utilisable uniquement pour les analyses strict, max et custom. Par défaut, c'est analyse retourne l'intervalle le plus long parmis tous ceux qui valident les critères d'acceptation. Cette option prend en compte tous les intervalle au lieu de prendre uniquement le plus grand.

- `More than` [--moreThan / -m <VALUE>]: Utilisable uniquement pour les analyses custom. Spécifie l'analyse de ne valider les intervalles que si plus de <VALUE> overlappers l'ont détecté.

- `Less than` [--lessThan / -l <VALUE>]: Utilisable uniquement pour les analyses custom. Spécifie l'analyse de ne valider les intervalles que si moins de <VALUE> overlappers l'ont détecté.

- `Equals to` [--equalsThan / -e <VALUE>]: Utilisable uniquement pour les analyses custom. Spécifie l'analyse de ne valider les intervalles que exactement <VALUE> overlappers l'ont détecté.

#### Les types d'analyses

- `Gentle` : Analyse acceptant tous les intervalles des overlappers. Les intervalles sont fusionnés s'il est possible de le faire.

- `Strict` : Analyse acceptant les intervalles uniquement repérés par tous les overlappers (soit les fichiers passés en paramètres du programme). Si plusieurs intervalles 

- `Max` :

- `Custom` : `

#### Comment ajouter des nouveaux types de fichier d'entrée

#### Comment ajouter des nouveaux types de fichier de sortie



### English

## Informations complémentaires

### Général

- Table de hash qui avec A > Tous les overlaps de A
- Table [Read A][Read B][+] > Tableau d'objets contenant l'overlap
- Table[Read B][Read A][+] = Table[Read A][Read B][+]
- Fonction de hash :

    - "1" -> 56
    - "2" -> 56 => Collision, du coup python duplique la valeur
    - =>> Le nombre d'opérations dans une table

### Objet Interval

#### Attributs

- filename : nom du fichier
- id_A : id du read A
- id_B : id du read B
- strand : '+' si les séquence sont dans la même orientation. '-' s'il ne le sont pas
- length_A : longueur de la séquence A
- length_B : longueur de la séquence B
- start_A : indice de début de A
- start_B : indice de début de B
- end_A : indice de fin de A
- end_B : indice de fin de B

## Quelques idées supplémentaires

### Calculs sur minimum par une courbe de couverture

- Faire un tableau (valeurs initialisées à zero) qui par de 0 jusqu'à la fin de l'intervalle le plus loin. On boucle pour chaque intervalle du début à la fin d'intervalle. On ajoute +1. Il suffira de prendre la partie qui a un nombre le plus grand.

- Exemple :

``` console
A -> de 1 à 3
B -> de 2 à 5
C -> de 7 à 8

Cela donne
0 1 2 2 1 1 0 1 1

Si on utilise l'option --cover, l'intervalle est 2 - 3
Si on utilise l'option --strict , il n'y a pas d'intervalle car le nombre max (2) n'est pas égal au nombre d'intervalles de départ (3)
```

#### Limites

Cela ne marche que pour R1 ou R2, mais pas R1 ET R2.

Possible solution : faire un dictionnaire avec les intervalles au lieu de juste des entier?

### Type de fichier générique

Avoir un type de fichier input générique, ce qui permet une meilleure modularité ainsi qu'une diminution de la redondance du code.

Récupération d'un fichier "bibliothèque" qui contient les formats + champs des fichiers acceptés

Pour chaque fichier d'input :

- Vérification que son type fait bien partie des fichiers acceptés