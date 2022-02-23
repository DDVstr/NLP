#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Importing libs
import nltk
#nltk.download('cmudict')
from nltk.corpus import cmudict
import sys,os

#generating rhyme for word
def rhyme(inp, level):
    entries = nltk.corpus.cmudict.entries()
    syllables = [(word, syl) for word, syl in entries if word == inp]
    rhymes = []
    for (word, syllable) in syllables:
        rhymes += [word for word, pron in entries if pron[-level:] == syllable[-level:]]
    return set(rhymes)

#defining main()
if __name__ == '__main__':
    """checking out rhymes"""
    list_of_rhymes = rhyme('car',4)
    print(list_of_rhymes)
