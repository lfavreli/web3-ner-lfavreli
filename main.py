import sys

import nltk
from nltk.chunk import conlltags2tree, tree2conlltags
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

import spacy
from spacy import displacy

from collections import Counter

from pprint import pprint

def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent

def main():
    ex = 'European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices'
    sent = preprocess(ex)
    pattern = 'NP: {<DT>?<JJ>*<NN>}'

    cp = nltk.RegexpParser(pattern)
    cs = cp.parse(sent)
    
    
    iob_tagged = tree2conlltags(cs)
    #pprint(iob_tagged)

    ne_tree = nltk.ne_chunk(pos_tag(word_tokenize(ex)))
    # print(ne_tree)

    nlp = spacy.load('en_core_web_sm')

    doc = nlp('European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices')
    # pprint([(X.text, X.label_) for X in doc.ents])

    pprint([(X, X.ent_iob_, X.ent_type_) for X in doc])
    


if __name__ == '__main__':
    sys.exit(main())