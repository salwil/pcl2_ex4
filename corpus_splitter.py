#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# Programmiertechniken in der Computerlinguistik II
# Uebung 4, Aufgabe 1.2
# Autoren: Frik Bauer, Salome Wildermuth


import xml.etree.ElementTree as ET
import random

def split_corpus(infile, outdir):

    abstract = []
    document_start = False
    for _,article in ET.iterparse(infile):

        # detects if we are currently inside an abstract
        if article.tag=='document':
            if document_start==True:
                document_start=False
                print("AbstractFinished")
                print('\n')
                # writing completed abstract to file (by using distribution function (1/3) because I couldn't implement the Algorithm R..
                distribut(abstract, outdir)
                abstract=[]
            # detects start of new abstract
            elif document_start==False:
                document_start=True
                print('New Abstract')
                print('\n')
        # appends every sentence in abstract to a temporary list
        elif article.tag=='sentence':
            abstract.append(article.text)
            abstract.append(' ')


def distribut(abstract, outdir):
    con_var = random.randint(1, 3)
    if con_var == 1:
        outfile = open(outdir + '/abstracts_training.txt', 'a', encoding='utf8')
    elif con_var == 2:
        outfile = open(outdir + '/abstracts_test.txt', 'a', encoding='utf8')
    elif con_var == 3:
        outfile = open(outdir + '/abstracts_development.txt', 'a', encoding='utf8')
    for sent in abstract:
        outfile.write(sent)
    outfile.write('\n')
    outfile.close()


if __name__ == '__main__':
        split_corpus()