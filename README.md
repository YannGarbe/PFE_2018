# PFE 2018 : Seul on va plus vite, à plusieurs on va plus loin ! Est-ce vrai pour l'assemblage des génomes ?

## Etudiant

- Yann Garbé

## Auteur / Encadrant du sujet

- Pierre Marijon de l'équipe Bonsai - CRIStAL

## TODO

### Général

- Ajouter un attribut aux intervalles : l'orientation (0 : normal | 1 : inversé) *

- Ajouter un paramètre dans le programme :
    - "--strict" : n'accepte l'intervalles que si tous les overlappers sont d'accord (création d'un intervalle qui unifie les intervalles en prenant l'intervalle le plus grand)

- QoL sur l'utilisation du programme
- QoL pour éviter la dedondance de code
- Faire une fusion des longueurs?
- **Refaire tous les tests**

- (remarque quand on a des exceptions relevées, bien indiquer au moins le fichier concerné.)

### Précis

- Utiliser une boucle avec un pop

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

- Sorties :
    - Paf
    - Mhap


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

### Type de fichier générique

Avoir un type de fichier input générique, ce qui permet une meilleure modularité ainsi qu'une diminution de la redondance du code.

Récupération d'un fichier "bibliothèque" qui contient les formats + champs des fichiers acceptés

Pour chaque fichier d'input :

- Vérification que son type fait bien partie des fichiers acceptés
