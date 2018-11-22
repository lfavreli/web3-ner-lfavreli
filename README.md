# Script - Peuplement de l'ontologie "Films"

Script Python facilitant le peuplement de l'ontologie de notre ontologie de Film.

## Prérequis

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

1. Récupération des identifiants (IMDb) des films présents dans le fichier `res/ids_movies.txt` ou `res/ids_movies_full.txt` permettant de se constituer une base de connaissance. Le nombre d'identifiants est extensible.

2. Récupération, avec BeautifulSoup, de l'arbre DOM de la fiche descriptive de chacun des films. Pour exemple, pour le film `tt0092067` : `https://www.imdb.com/title/tt0092067/`.

3. Extraction, à l'aide des sélecteurs CSS, des informations pertinentes au peuplement : titre, note, durée, réalisateur, genre, date de sortie et acteurs.

4. Création d'une fiche récapitulative dans le répertoire : `tt0092067/description`.

5. Récupération, avec BeautifulSoup, des critiques associés au film. Pour exemple, pour le film `tt0092067` : `https://www.imdb.com/title/tt0092067/reviews`.

6. Nettoyage des critiques et suppression des balises paragraphe (`<p>`) avec JusText. Utilisation de la "stop list" Anglaise.

7. Concaténation des critiques dans un fichier texte de sortie : `tt0092067/reviews`.

8. Génération des objets `Movie`, sur la base des fichiers `description`, servant au peuplement de l'ontologie.

9. Pour chaque film, récupération de ses critiques `tt0092067/reviews` puis extraction à l'aide de SpaCy des entités nommées de types `PERSON`.

10. Calcul l'intersection entre les acteurs présents dans la fiche fiche de description et les acteurs cités dans les critiques. Nous récupérons ainsi les acteurs les plus controversés. Ce sont ceux qui seront importants d'importer dans notre ontologie.

À noter que les sorties seront plus pertinentes avec un nombre de films et de critiques par film important. Nous pourrions ainsi ressortir les acteurs les plus plébiscités ou critiquer.

## Évolutions possibles

1. Pour la classification par sexe, nous pourrions utiliser des dictionnaires afin de distinguer le genre des acteurs et des producteurs. Néansmoins, il y aurait des ambigüités pour les prénoms mixtes.

2. Pour chacun des films, il serait possible de déterminer si les entités nommées dans les critiques le sont positivement ou négativement.

## Étudiants

* Loïc FAVRELIERE
* Nicola FOISSAC
