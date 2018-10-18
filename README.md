# PFE 2018 : Seul on va plus vite, à plusieurs on va plus loin ! Est-ce vrai pour l'assemblage des génomes ?

## Etudiant

- Yann Garbé

## Auteur / Encadrant du sujet

- Pierre Marijon de l'équipe Bonsai - CRIStAL

## TODO

- Faire des recherches sur afin de créer l'objet d'overlap
- Implémenter une fonction par type de fichier qui donne une double hash map
- Utiliser le module csv de python pour parser les lignes
- Ajouter des commentaire au début de chaque block d'inscruction (if, for etc....)

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

### Objet Interval

#### Attributs

- filename : nom du fichier
- id_A : id du read A (int)
- id_B : id du read B (int)
- reverse_A : indique si A est inversé ou non (bool)
- reverse_B : indique si B est inversé ou non (bool)
- start_A : indice de début de A
- start_B : indice de début de B
- end_A : indice de fin de A
- end_B : indice de fin de B