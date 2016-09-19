#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Time-stamp: <2016-09-19 06:45:53 cp983411>

import sys

def anagrams(wordlist):
    """ input:
            wordlist: a list of strings (words)
        output:
            a list of lists of words that have the same letters
    """
    anagrams = {}
    for w in wordlist:
        key = str(sorted(w))
        if key in anagrams: anagrams[key].append(w)
        else: anagrams[key] = [ w ]
    return [ l for l in anagrams.itervalues() if len(l) > 1 ]


if __name__ == '__main__':
    # the input is a text file with one word per line
    text = [ l.strip() for l in file(sys.argv[1]).readlines() if l != '\n']
    print(anagrams(text))

