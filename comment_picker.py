#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# Programmiertechniken in der Computerlinguistik II
# Uebung 4, Aufgabe 1.1
# Autoren: Salome Wildermuth, Frederik Bauer

from typing import BinaryIO
import bz2
import gzip
import json


def mk_meme_corpus(  infile: BinaryIO
                   , outfile: str
                   , min_score: int=100
                   , min_len: int=1
                   , max_len: int=50):
    with gzip.open(outfile, 'w') as outfile:
        dict_out = {}
        for line in infile:
            dict_lin = json.loads(line.decode('utf-8'))
            if int(dict_lin['score']) > min_score and len(dict_lin['body']) >= min_len and len(dict_lin['body']) <= max_len:
                if dict_lin['body'] not in dict_out:
                    out_bin = dict_lin['body'].encode('utf-8')
                    print(out_bin)
                    outfile.write(out_bin)
                    outfile.write('\r\n'.encode("utf-8"))
                    dict_out[dict_lin['body']] = 1
    print("Process finished")

#def main():
    #infile = 'C:/Users/Salome/pcl2_ex4/Korpusdaten/RC_2012-06.bz2'
    #with bz2.open(infile, mode='rb', compresslevel=9) as infile:
        #mk_meme_corpus(infile, 'outfile.txt.gz', 500, 1, 20)

#if __name__ == '__main__':
        #main()