#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Time-stamp: <2016-09-19 06:40:08 cp983411>

import sys 

def count_lines_words(text):
    """ input: 
            text: a string
        output:
            number of lines and words in text """ 
    nlines, nwords = 0, 0
    for line in text:
	nlines += 1
	nwords += len(line.split())
    return (nlines, nwords)	

if __name__ == '__main__':
    fname = sys.argv[1]
    text = file(fname).readlines()
    print(count_lines_words(text))
