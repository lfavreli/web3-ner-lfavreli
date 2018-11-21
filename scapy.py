import glob
import spacy
from spacy import displacy

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



def get_named_entities():
    nlp = spacy.load('en_core_web_sm')

    actors = []
    print('Compute intersection between actors in description and reviews...')
    for path in Path("./dist").glob('*'):
        dir = str(path)
        description = open(dir + '\\description', encoding='utf-8').read()
        reviews = open(dir + '\\reviews', encoding='utf-8').read()
        
        movie = build_movie_from_description(description)

        doc = nlp(reviews)
        ne_type = [el.text for el in doc.ents if el.label_ == 'PERSON']
        intersect = list(set(movie['actor']) & set(ne_type))
        actors += intersect
        print('Intersection for ' + movie['title'] + ' : ')
        print(intersect)

    print('All done !')
 
    print(Counter(actors).most_common())
    