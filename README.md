# PFE 2018 : Seul on va plus vite, à plusieurs on va plus loin ! Est-ce vrai pour l'assemblage des génomes ?

## Etudiant

- Yann Garbé

## Auteur / Encadrant du sujet

- Pierre Marijon de l'équipe Bonsai - CRIStAL

## TODO

### Général

- Ajouter un attribut aux intervalles : l'orientation (0 : normal | 1 : inversé) *
- **Retransformer toute l'architecture en faisant une triple hashmap (id_A, id_B, orientation)** *
- Ajouter un paramètre dans le programme :
    - "--strict" : n'accepte l'intervalles que si tous les overlappers sont d'accord (création d'un intervalle qui unifie les intervalles en prenant l'intervalle le plus grand)
    - "--gentle" : accepte tous les intervalles (création d'un intervalle qui unifie les intervalles en prenant l'intervalle le plus petit)
    - Par défaut, le programme est "--gentle"

- Avoir une sortie en fichier paf
- Refaire tous les tests

### Précis

- Ajouter une information de statistique qui utilise la moyenne d'intervalles et la divise par le nombre d'overlappeurs * 
- Utiliser une boucle avec un pop
- Ajouter une fonction  dans la classe intervalle qui prend en entrée deux entiers et qui ressord le fond si les intervalles sont corrects

## DONE

- Faire des recherches sur les hashMap
- Créer un objet interval
- Utilisation d'une double hashmap

- Trier les intervalles par start_A croissant

- Ajouter un paramètre "--stats" qui permet d'afficher quelques informations dans le terminal :
    - La moyenne d'intervalles entre les fichiers d'entrée
    - La moyenne d'intervalles cohérent entre les fichiers d'entrée
    - La moyenne d'intervalles venant du même fichier


## Infos complémentaires

### Général

Créer une classe qui garde les informations importantes

- Table de hash qui avec A > Tous les overlaps de A
- Table [Read A][Read B] > Tableau d'objets contenant l'overlap
- Table[Read B][Read A] = Table[Read A][Read B]
- Fonction de hash :

    - "1" -> 56
    - "2" -> 56 => Collision, du coup python duplique la valeur
    - =>> Le nombre d'opérations dans une table

### Objet Interval

#### Attributs

- filename : nom du fichier
- id_A : id du read A
- id_B : id du read B
- length_A : longueur de la séquence A
- length_B : longueur de la séquence B
- start_A : indice de début de A
- start_B : indice de début de B
- end_A : indice de fin de A
- end_B : indice de fin de B

## Quelques idées supplémentaires

### Type de fichier générique

Avoir un type de fichier input générique, ce qui permet une meilleure modularité ainsi qu'une diminution de la redondance du code.

Récupération d'un fichier "bibliothèque" qui contient les formats + champs des fichiers acceptés

Pour chaque fichier d'input :

- Vérification que son type fait bien partie des fichiers acceptés
