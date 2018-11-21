import spacy
from spacy import displacy

from pprint import pprint

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

    try:
        # open database file in read mode whit utf-8 encoding
        with open(file='./dist/tt0109830', mode='r', encoding="utf-8", errors='ignore') as file:
            # extend list of references whit content of file
            references = ' '.join(file.read().split('\n'))
            # close file
            file.close()
    except:
        pass


    description = """Forrest Gump (1994) 
2h22min
8.8
Drama,Romance
5 October 1994 (France)
RobertZemeckis
Tom Hanks, Rebecca Williams, Sally Field, Michael Conner Humphreys, Harold G. Herthum, George Kelly, Bob Penny, John Randall, Sam Anderson, Margo Moorer, Ione M. Telech, Christine Seabrook, John Worsham, Peter Dobson, Siobhan Fallon Hogan"""
    movie = build_movie_from_description(description)

    

    

    doc = nlp("""Quite simply, the greatest film ever made.

Humour, sadness, action, drama and a Vietnam film all rolled into one.

I'm not a stone cold, heartless villain, but it takes a lot to make me cry when I watch a movie. Bambi's mother, I couldn't care less. Jimmy Stewart in, "Oh, what a wonderful life," - yeah right! The Lion King, when Mufasa bites the big one - on the verge.

But seriously - I bawled my big brown eyes out, on several occasions in this film. A real tear-jerker, and a wonderful character, played to perfection by Tom Hanks. Every bit as worthy for the Oscar as Rooney was to win the Premiership in 2007. """)



    ne_type = [el.text for el in doc.ents if el.label_ == 'PERSON']
    intersect = set(movie['actor']) & set(ne_type)
    
    # Counter(items).most_common(3)
    # pprint(Counter(labels))