import spacy
from spacy import displacy

from pprint import pprint

from collections import Counter



def get_named_entities():

    nlp = spacy.load('en_core_web_sm')

    try:
        # open database file in read mode whit utf-8 encoding
        with open(file='./dist/tt6145612', mode='r', encoding="utf-8", errors='ignore') as file:
            # extend list of references whit content of file
            references = ' '.join(file.read().split('\n'))
            # close file
            file.close()
    except:
        pass

    doc = nlp(references)
    pprint([(X.text, X.label_) for X in doc.ents])

    # pprint([(X, X.ent_iob_, X.ent_type_) for X in doc])

    labels = [x.label_ for x in doc.ents]
    items = [x.text for x in doc.ents]

    pprint(labels)
    pprint(items)

    # Counter(items).most_common(3)
    # pprint(Counter(labels))
#if __name__ == '__main__':
#    get_named_entities()