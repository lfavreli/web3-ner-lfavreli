# Script - Peuplement de l'ontologie "Films"

Script Python facilitant le peuplement de notre ontologie de Film.

## Prérequis

* Python ≥ 3.5
* JusText ≥ 2.2.x
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

Fonctionnement interne :

1. Récupération des identifiants (IMDb) des films présents dans le fichier `res/ids_movies.txt` ou `res/ids_movies_full.txt` permettant de se constituer une base de connaissance. Le nombre d'identifiants est extensible.

2. Récupération, avec BeautifulSoup, de l'arbre DOM de la fiche descriptive de chacun des films. Pour exemple, pour le film `tt0092067` : `https://www.imdb.com/title/tt0092067/`.

3. Extraction, à l'aide des sélecteurs CSS, des informations pertinentes au peuplement : titre, note, durée, réalisateur, genre, date de sortie et acteurs.

4. Création d'une fiche récapitulative dans le répertoire : `tt0092067/description`.

5. Récupération, avec BeautifulSoup, des critiques associés au film. Pour exemple, pour le film `tt0092067` : `https://www.imdb.com/title/tt0092067/reviews`.

6. Nettoyage des critiques et suppression des balises paragraphe (`<p>`) avec JusText. Utilisation de la "stop list" Anglaise.

7. Concaténation des critiques dans un fichier texte de sortie : `tt0092067/reviews`.

8. Génération des objets `Movie`, sur la base des fichiers `description`, servant au peuplement de l'ontologie.

9. Pour chaque film, récupération de ses critiques `tt0092067/reviews` puis extraction à l'aide de SpaCy des entités nommées de types `PERSON`.

10. Calcul l'intersection entre les acteurs présents dans la fiche de description et les acteurs cités dans les critiques. Nous récupérons ainsi les acteurs les plus controversés (positivement ou négativement). Ce sont ceux qui seront indispensables d'importer dans notre ontologie.

## Sorties (outputs)

* movies.json

Liste des objets `Movie` avec l'ensemble des caractéristiques récupérées où `controversial_actors` correspondant à l'intersection des acteurs récupérés dans la fiche descriptive et les acteurs cités dans les critiques.

* actor_most_common.json

Liste, triée, des acteurs apparaissant le plus de fois dans toutes les critiques.

---

Les sorties seront plus pertinentes avec un nombre de films et de critiques par film important. Nous pourrions ainsi ressortir les acteurs les plus plébiscités ou critiquer.

## Évolutions possibles

1. Pour la classification par sexe, nous pourrions utiliser des dictionnaires afin de distinguer le genre des acteurs et des producteurs. Néansmoins, il y aurait des ambigüités pour les prénoms mixtes.

2. Pour chacun des films, il serait possible de déterminer si les entités nommées dans les critiques le sont positivement ou négativement.

3. Pour chacun des commentaires, calculer le nombre d'occurrences des acteurs dans les critiques et pondérer le nombre d'apparitions avec l'importance qu'ils dans celui-ci.

## Étudiants

* Loïc FAVRELIERE
* Nicola FOISSAC
