# PFE 2018 : Seul on va plus vite, à plusieurs on va plus loin ! Est-ce vrai pour l'assemblage des génomes ?

## Etudiant

- Yann Garbé

## Auteur / Encadrant du sujet

- Pierre Marijon de l'équipe Bonsai - CRIStAL

## TODO

- Faire des recherches sur afin de créer l'objet d'overlap
- Implémenter une fonction par type de fichier qui donne une double hash map

## DONE

- Faire des recherches sur les hashMap
    - En fait se sont des dictionnaires

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