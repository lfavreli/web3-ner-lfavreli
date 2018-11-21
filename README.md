# Script - Peuplement de l'ontologie "Films"

Script Python facilitant le peuplement de l'ontologie "Film".

## Requis

* Python ≥ 3.5
* BeautifulSoup ≥ 4.6.x
* SpaCy ≥ 2.0.x
* Téléchargement du modèle :

```console
    python -m spacy download en_core_web_sm
```

## Mise en place

L'objectif de ce script est de faciliter le peuplement de notre ontologie de films.

Rappel des principales classes :

* dbo:Person > Actor, Director, Male, Female
* Genre > Action, Comedy, Fantastic
* Movie > Original, Remake
* MovieRating [ 1 .. 5 ]

Détaillons son fonctionnement interne :

1. 

## Évolution envisageable

1. Pour la classification par sexe, nous pourrions utiliser des dictionnaires afin des distinguer le genre des acteurs et des producteurs. Néansmoins, il aurait des ambigûités pour les prénoms mixtes.

## Étudiants

* Loïc FAVRELIERE
* Nicola FOISSAC