import glob
import spacy
import json
import os

from pathlib import Path
from collections import Counter


def build_movie_from_description(description):

    # split all element in description
    elements = description.split('\n')
    # data set form movie
    movie = {
        'title': elements[0],
        'duration': elements[1],
        'rating': elements[2],
        'genre': elements[3].split(','),
        'release': elements[4],
        'productor': elements[5],
        'actor': elements[6].split(',')
    }
    return movie


def generate_knowledge(dist):
    # load spacy english web model
    nlp = spacy.load('en_core_web_sm')
    # list of actor
    actors = []
    # list of movies
    movies = []
    print('Compute intersection between actors in description and reviews...')
    # for all dir in dist directory
    for path in Path(dist).glob('*'):
        dirs = str(path)
        # open description file
        description = open(dirs + '/description', encoding='utf-8').read()
        # open review
        reviews = open(dirs + '/reviews', encoding='utf-8').read()
        # build data set for movie
        movie = build_movie_from_description(description)
        # use nlp to extract named entity
        doc = nlp(reviews)
        # for all actor detected in review
        ne_type = [el.text for el in doc.ents if el.label_ == 'PERSON']
        # intersect whit movies data set actors
        intersect = list(set(movie['actor']) & set(ne_type))
        # append intersect whit data set
        movie['controversial_actors'] = intersect
        # append to movies list
        movies.append(movie)
        # append intersect to actors
        actors += intersect
        print('Intersection for ' + movie['title'] + ' : ')
        print(intersect)
    print('All done !')

    # compute most common controversy actor
    actors_most_common = Counter(actors).most_common()
    print(actors_most_common)

    if not os.path.exists('./output'):
        # then make directory
        os.makedirs('./output')
    with open('./output/movies.json', 'w') as outfile:
        json.dump(movies,outfile,ensure_ascii=False,sort_keys=True,indent=4)
        outfile.close()

    with open('./output/actor_most_common.json', 'w') as outfile:
        json.dump(actors_most_common, outfile, ensure_ascii=False, sort_keys=True,indent=4)
        outfile.close()
