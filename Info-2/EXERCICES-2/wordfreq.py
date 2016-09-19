#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys 
import zipf

def words_freq(text):
    """ input:
              text: a list of strings
        output:
              the number of occurences of each words in text
    """
    freqs = {}
    for l in text:
        for w in l.strip().split():
            if w in freqs: 
                freqs[w] += 1
            else: 
                freqs[w] = 1
    return freqs	

    

if __name__ == '__main__':
	fname = sys.argv[1]
	text = file(fname).readlines()
	f = words_freq(text)
        print(f)
        zipf.zipf_plot(f.values())
