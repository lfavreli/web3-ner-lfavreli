import glob
import spacy
import json
import os

from pathlib import Path
from collections import Counter


def build_movie_from_description(description):

    elements = description.split('\n')
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
    nlp = spacy.load('en_core_web_sm')
    actors = []
    movies = []
    print('Compute intersection between actors in description and reviews...')
    for path in Path(dist).glob('*'):
        dirs = str(path)
        description = open(dirs + '/description', encoding='utf-8').read()
        reviews = open(dirs + '/reviews', encoding='utf-8').read()
        
        movie = build_movie_from_description(description)

        doc = nlp(reviews)
        ne_type = [el.text for el in doc.ents if el.label_ == 'PERSON']
        intersect = list(set(movie['actor']) & set(ne_type))
        movie['controversial_actors'] = intersect
        movies.append(movie)
        actors += intersect
        print('Intersection for ' + movie['title'] + ' : ')
        print(intersect)
    print('All done !')
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