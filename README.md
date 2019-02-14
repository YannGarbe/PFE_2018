# PFE 2018 : Seul on va plus vite, à plusieurs on va plus loin ! Est-ce vrai pour l'assemblage des génomes ?

## Etudiant

- Yann Garbé

## Auteur / Encadrant du sujet

- Pierre Marijon de l'équipe Bonsai - CRIStAL

    - get_all afin d'obtenir l tous les intervals et non le plus long

## HOW TO

### Français

Le but de ce programme est de réaliser différents types d'analyses sur des overlappers.

Pour lancer le programme, placez-vous dans le répertoire `src` et lancer le fichier `Analyser.py` avec python.

Les résultats du programme sont dans le répertoire `Output`.

#### Paramètres d'entrée

Voici les paramètres principaux :

- `Analyse type` [gentle, strict, max, custom]: le type d'analyse à réaliser. Cela peut être gentle, strict, max ou custom (voir le point `Les Types d'analyses` pour avoir plus d'informations sur ces analyses).

- `Output type` [paf, mhap, hisea]: le type de fichier de retour. Cela peut être paf, mhap ou hisea (note : hisea n'est pas implémenté pour le moment).

- `Input files` [chemins]: les différents fichiers d'entrées à analyser : ils ne peuvent être que d'extension mhap et paf pour le moment.

D'autres paramètres peuvent également être utilisés :

- `Statistics` [--stats / -s]: Permet, au lieu d'effectuer une analyse, d'afficher certaines statistiques sur les fichiers d'entrée.

- `Get all` [--get_all / -all]: Utilisable uniquement pour les analyses strict, max et custom. Par défaut, c'est analyse retourne l'intervalle le plus long parmis tous ceux qui valident les critères d'acceptation. Cette option prend en compte tous les intervalle au lieu de prendre uniquement le plus grand.

- `More than` [--moreThan / -m <VALUE>]: Utilisable uniquement pour les analyses custom. Spécifie l'analyse de ne valider les intervalles que si plus de <VALUE> overlappers l'ont détecté.

- `Less than` [--lessThan / -l <VALUE>]: Utilisable uniquement pour les analyses custom. Spécifie l'analyse de ne valider les intervalles que si moins de <VALUE> overlappers l'ont détecté.

- `Equals to` [--equalsThan / -e <VALUE>]: Utilisable uniquement pour les analyses custom. Spécifie l'analyse de ne valider les intervalles que exactement <VALUE> overlappers l'ont détecté.

#### Les types d'analyses

- `Gentle` : Analyse acceptant tous les intervalles des overlappers. Les intervalles sont fusionnés s'il est possible de le faire.

- `Strict` : Analyse acceptant les intervalles uniquement repérés par tous les overlappers (soit les fichiers passés en paramètres du programme). Par exemple, si l'on donne en entrée deux overlappers en lançant le programme, l'analyse ne va accepter les intervalles uniquement que si ces deux overlappers ont repéré les intervalles.

- `Max` : Analyse acceptant les intervalles uniquement repérés par le maximum d'overlapper entre les deux reads. Par exemple, si entre ces deux reads, au maximum deux overlappers ont trouvé quelque chose, l'analyse ne va accepter que la zone uniquement repérée par ces deux overlappers.

- `Custom` : Analyse acceptant les intervalles uniquement repérés par un nombre d'overlappers personalisés entre les deux reads. Cette analyse dépend des paramètres `More than` (n'accepte les intervalles repérés par plus de X overlappers), `Less than` (n'accepte les intervalles repérés par moins de X overlappers) et `Equals to` (n'accepte les intervalles repérés par exactement X overlappers).

#### Comment ajouter des nouveaux types de fichier d'entrée

Afin d'ajouter des nouveau types de fichier d'entrée, il suffit de modifier le fichier `allowed_files.csv`. Le fichier indique plusieurs champ.

| Champ           | Description                                                           |
| --------------: | :-------------------------------------------------------------------- |
| file_Type       | Nom de l'extension du fichier.                                        |
| ascii_separator | Caractère de séparation des champs en ascii.                          |
| nb_fields       | Nombre de champs minimals pour le fichier soit accepté.               |
| id_A_field      | Numéro de champ contenant l'id du read A.                             |
| id_B_field      | Numéro de champ contenant l'id du read B.                             |
| length_A_field  | Numéro de champ contenant la longueur de la séquence du read A.       |
| length_B_field  | Numéro de champ contenant la longueur de la séquence du read B.       |
| start_A_field   | Numéro de champ contenant l'indice de début de la séquence du read A. |
| start_B_field   | Numéro de champ contenant l'indice de début de la séquence du read B. |
| end_A_field     | Numéro de champ contenant l'indice de fin de la séquence du read A.   |
| end_B_field     | Numéro de champ contenant l'indice de fin de la séquence du read B.   |
| strand_type     | Indique le type d'orientation. S'il s'agit de `1` alors il existe directement un champ unique indiquant si les séquences des deux reads ont la même orientation ou ont des orientation différentes. S'il s'agit de `2` alors il exsite deux champs. 1 pour l'orientation (normal ou inversée) de la séquence du read A et 1 autre pour l'orientation de la séquence du read B.             |
| strand_A/total  | Numéro de champ contenant l'orientation des deux reads (si strand_type vaut `1`) ou l'orientation de la séquence du read A (si strand_type vaut `2`). |
| strand_B        | Si strand_type vaut `1`, mettre `N`. Si strand_type vaut `2`, numéro de champ contenant l'orientation du read B.                            |

Les numéros de champ correspondent au numéro de champ (en commençant par 0) du type de fichier que l'on veut ajouter.
Pour ajouter un nouveau type de fichier, il suffit donc d'ajouter un ligne en remplissant les informations des champs décrit dans le tableau ci-dessus.

#### Comment ajouter des nouveaux types de fichier de sortie

Il n'existe malheureusement pas d'autres moyen que de modifier le code du programme si l'on veut ajouter unnouveau type de fichier de sortie.

Il faudra modifier trois choses :

- La première se situe dans `read/Parameters.py` à la ligne 46. Il faut ajouter l'extension du fichier à obtenir en sortie dans la variable **choices** (et si possible, mettre à jour la documentation liée à celle-ci)
- La deuxième se situe dans `write/OutputWriter.py`. Il faudra ajouter une méthode écrivant dans le bon ordre la syntaxe du fichier.
- La troisième se situe dans `Analyser.py`. Il faudra ajouter une condition à la ligne 61 pour permettre l'écriture.

### English

The purpose of this program is to perform different types of analyses on overlappers.

To launch the program, go to the `src` directory and launch the `Analyser.py` file with python.

The results of the program are in the `Output` directory.

#### Input Parameters

Here are the main parameters:

- `Analysis Type`[gentle, strict, max, custom]: the type of analysis to be performed. It can be gentle, strict, max or custom (see the section `Types of analyses' for more informations on these analyses).

- `Output type`[paf, mhap, hea]: the type of the output file. It can be paf, mhap or hisea (note: hisea is not implemented at the moment).

- `Input files` [path] : the different input files to be analyzed: they can only be mhap and paf files for the moment.

Other parameters can also be used:

- Statistics[--stats / -s]: Instead of performing an analysis, displays certain statistics on the input files.

- `Get all` [--get_all / -all]: Can only be used for strict, max and custom analyses. By default, this analysis returns the longest interval among all those who validate the acceptance criteria. This option takes into account all intervals instead of only the largest one.

- `More than` [--moreThan / -m <VALUE>]: Can only be used for custom analyses. Specifies the analysis to validate the intervals only if more than <VALUE> overlappers have detected them.

- `Less than` [--lessThan / -l <VALUE>]: Can only be used for custom analyses. Specifies the analysis to validate the intervals only if less than <VALUE> overlappers have detected them.

- `Equals to` [--equalsThan / -e <VALUE>]: Can only be used for custom analyses. Specifies the analysis to validate the intervals only exactly <VALUE> overlappers have detected them.

#### Types of analyses

- `Gentle` : Analysis accepting all overlapper intervals. Intervals are merged if possible.

- `Strict` : Analysis accepting intervals only identified by all overlappers (i.e. files passed as program parameters). For example, if two overlappers are input when the program is started, the analysis will only accept the intervals if these two overlappers have identified the intervals.

- `Max` : Analysis accepting intervals only identified by the maximum overlap between the two reads. For example, if between these two reads, at most two overlappers have found something, the analysis will only accept the area only identified by these two overlappers.

- `Custom`: Analysis accepting intervals only identified by a number of custom overlappers between the two reads. This analysis depends on the parameters `More than` (does not accept intervals marked by more than X overlappers), `Less than` (does not accept intervals marked by less than X overlappers) and `Equals to` (does not accept intervals marked by exactly X overlappers).

#### How to have more input types

In order to add new input file types, it is sufficient to modify the file `allowed_files.csv`. The file indicates several fields.

| Field           | Description                                                           |
| --------------: | :-------------------------------------------------------------------- |
| file_Type       | Name of the file extension.                                           |
| ascii_separator | Character of separation of the fields in ascii.                       |
| nb_fields       | Minimum number of fields to accept the file.                          |
| id_A_field      | Field number containing the ID of the read A.                         |
| id_B_field      | Field number containing the ID of the read B.                         |
| length_A_field  | Field number containing the length of the read A sequence.            |
| length_B_field  | Field number containing the length of the read B sequence.            |
| start_A_field   | Field number containing the start index of the read A sequence.       |
| start_B_field   | Field number containing the start index of the read B sequence.       |
| end_A_field     | Field number containing the end index of the read A sequence.         |
| end_B_field     | Field number containing the end index of the read B sequence.         |
| strand_type     | Indicates the type of orientation. If it is `1` then there is a single field indicating whether the sequences of the two reads have the same orientation or have different orientations. If it is `2` then there are two fields. 1 for the orientation (normal or inverted) of the read A sequence and 1 for the orientation of the read B sequence.             |
| strand_A/total  | Field number containing the orientation of the two reads (if strand_type is `1`) or the orientation of the sequence of the read A (if strand_type is `2`). |
| strand_B        | If strand_type is `1`, put `N`. If strand_type is `2`, field number containing the orientation of the read B.                            |

The field numbers correspond to the field number (starting with 0) of the file type you want to add.
To add a new file type, simply add a line by filling in the informations in the fields described in the table above.

#### How to have more output types

Unfortunately, there is no other way than to modify the program code if you want to add a new type of output file.

Three things will have to be changed:

- The first is in `read/Parameters.py` in line 46, add the extension of the file to be output in the variable **choices** (and if possible, update the documentation related to it)
- The second is located in `write/OutputWriter.py`. It will be necessary to add a method that writes the syntax of the file in the right order.
- The third is located in `Analyser.py`. A condition will have to be added to line 61 to allow writing.

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