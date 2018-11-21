import spacy
from spacy import displacy

from pprint import pprint

from collections import Counter

def get_named_entities():

    nlp = spacy.load('en_core_web_sm')

    doc = nlp('European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices')
    pprint([(X.text, X.label_) for X in doc.ents])

    # pprint([(X, X.ent_iob_, X.ent_type_) for X in doc])

    labels = [x.label_ for x in doc.ents]
    items = [x.text for x in doc.ents]

    pprint(labels)
    pprint(items)

    # Counter(items).most_common(3)
    # pprint(Counter(labels))