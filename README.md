# PFE 2018 : Seul on va plus vite, à plusieurs on va plus loin ! Est-ce vrai pour l'assemblage des génomes ?

## Etudiant

- Yann Garbé

## Auteur / Encadrant du sujet

- Pierre Marijon de l'équipe Bonsai - CRIStAL

## TODO

### Général

- Refactoring de code
- Amélioration des warnings
- QoL sur l'utilisation du programme
- **Refaire tous les tests**

- (remarque quand on a des exceptions relevées, bien indiquer au moins le fichier concerné.)

## DONE

- Faire des recherches sur les hashMap
- Créer un objet interval
- Utilisation d'une triple hashmap

- Trier les intervalles par start_A croissant

- Ajouter un paramètre "--stats" qui permet d'afficher quelques informations dans le terminal :
    - Le pourcentage de dépendances entre les fichiers de données
    - La moyenne d'intervalles entre les fichiers d'entrée
    - La moyenne d'intervalles cohérent entre les fichiers d'entrée
    - La moyenne d'intervalles venant du même fichier

- Analyses :
    - Type gentle ajouté
    - Type strict ajouté (avec option get_all)
    - Type max ajouté (avec option get_all)
    * Type custom ajouté (avec option get_all, moreThan, lessThan et equalsTo)

- Sorties :
    - Paf
    - Mhap

- Option :
    - Stats pour avoir quelques statistiques sur les données
    - get_all afin d'obtenir l tous les intervals et non le plus long

## Infos complémentaires

### Général

Créer une classe qui garde les informations importantes

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