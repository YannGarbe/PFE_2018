# PFE 2018 : Seul on va plus vite, à plusieurs on va plus loin ! Est-ce vrai pour l'assemblage des génomes ?

## Etudiant

- Yann Garbé

## Auteur / Encadrant du sujet

- Pierre Marijon de l'équipe Bonsai - CRIStAL

## TODO

- Ajouter la longueur des séquences dans l'interval
- Faire tableau d'intervals au lieu d'un interval aux données correspondantes (dans la hashmap)
- Vérifier que architecture est adaptée tests d'isolation, la modifier en conséquences
- (facultatif) Faire des tests

### Pour la prochaine séance

- Faire une première analyse :
    - Si A est dans B
    - Si B est dans A
    - Si une partie de A est dans B
    - Si une partie de B est dans A
- (facultatif) Faire un début de sortie

## DONE

- Faire des recherches sur les hashMap
- Créer un objet interval
- Utilisation d'une double hashmap

## Infos complémentaires

### Général

Créer une classe qui garde les informations importantes

- Table de hash qui avec A > Tous les overlaps de A
- Table [Read A] [Read B] > Objet contenant l'overlap
- Table[Read B][Read A] = table [Read A][Read B]
- Fonction de hash :

    - "1" -> 56
    - "2" -> 56 => Collision, du coup python duplique la valeur
    - =>> Le nombre d'opérations dans une table

### Objet Interval

#### Attributs

- filename : nom du fichier
- id_A : id du read A (int)
- id_B : id du read B (int)
- length_A : longueur de la séquence A
- length_B : longueur de la séquence B
- start_A : indice de début de A
- start_B : indice de début de B
- end_A : indice de fin de A
- end_B : indice de fin de B