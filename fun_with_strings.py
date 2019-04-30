#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# Programmiertechniken in der Computerlinguistik II
# Uebung 4, Aufgabe 2
# Autoren: Frik Bauer, Salome Wildermuth

from typing import Iterable

def longest_substrings(x: str, y: str) -> Iterable[str]:
    lst_str1 = list(x.lower())
    lst_str2 = list(y.lower())
    matrix = [[0 for i in range (0,len(lst_str2)+1)]for i in range(0,len(lst_str1)+1)]
    max = 0
    max_str_dict = {}
    # Wir iterieren durch die beiden Ausdrücke, die wir zuvor in Listen umgewandelt haben. Dabei fügen wir jedem
    # Buchstabenpaar einen Wert hinzu, sodass eine Matrix entsteht. Der Wert entspricht der bisherigen Länge eines
    # allfälligen gemeinsamen Substrings der beiden Wörter. Als Verarbeitungshilfe, beinhaltet unsere Matrix je eine
    # Zeile bzw. Spalte mehr, als die Länge des ersten bzw. zweiten Substrings.
    # Bsp:
    #   A n d r e a
    # B 0 0 0 0 0 0 0
    # a 1 0 0 0 0 1 0
    # n 0 2 0 0 0 0 0
    # d 0 0 3 0 0 0 0
    #   0 0 0 0 0 0 0
    #
    for i in range(0,len(lst_str1)+1):
        for j in range(0, len(lst_str2)+1):
            # Zuallererst checken wir ab, ob das aktuelle Buchstabenpaar zweimal denselben Buchstaben enthält. Und mit
            # den ersten beiden Argumenten verhindern wir, dass wir am Schluss Indexüberlauf haben (da wir ja über die
            # Länge der Eingabestrings hinaus operieren).
            if i < len(lst_str1) and j < len(lst_str2) and lst_str1[i] == lst_str2[j]:
                # Falls wir uns nicht beim ersten Buchstaben eines der beiden Eingabestrings befinden, zählen wir zum
                # letzten Wert in der Diagonale 1 dazu.
                if i > 0 and j > 0:
                    matrix[i][j] = matrix[i-1][j-1]+1
                # Ist bereits das erste Buchstabenpaar gleich, addieren wir zum aktuellen Feld, das im Moment mit 0
                # initialisiert ist, 1.
                else:
                    matrix[i][j] += 1
            # Wenn die beiden aktuellen Buchstaben nicht übereinstimmen, aber der letzte Wert in der Diagonale in der
            # Matrix > als der aktuell zwischengespeicherte Maximalwert (Länge des bis dahin längsten gefundenen Sub-
            # strings), dann haben wir da einen neuen längsten Substring gefunden. Anhand der Länge verfolgen wir den
            # Eingabestring zurück bis zum Anfang und speichern ihn als neuen längsten Substring ab. Ebenfalls müssen
            # auch den neuen Maximalwert speichern.
            elif matrix[i-1][j-1] > max:
                # Wir gehen in einem der beiden Eingabestrings (egal welcher) um den Wert im letzten Diagonalenfeld
                # zurück, um den neuesten längsten Substring zuerst in einer Liste abzuspeichern aus der wir anschlies-
                # send einen String für die Ausgabe machen.
                k = i-matrix[i-1][j-1]
                max_str_lst = []
                while k < i:
                    max_str_lst.append(lst_str1[k])
                    k+=1
                max_str = ''.join(max_str_lst)
                max = matrix[i-1][j-1]
                max_str_dict = {}
                max_str_dict[max_str] = max
            # Wenn die beiden aktuellen Buchstaben nicht übereinstimmen, aber der letzte Wert in der Diagonale in der
            # Matrix dem aktuell zwischengespeicherte Maximalwert (Länge des bis dahin längsten gefundenen Sub-
            # strings) entspricht, dann haben wir da einen zusätzlichen längsten Substring gefunden. Hier müssen wir
            # aber speziell aufpassen, denn wir müssen verhindern, dass wir in diese Entscheidung geraten, wenn wir in
            # der Matrix 0 haben und max auch noch mit 0 initialisiert ist (das ist der Fall, solange keine gleichen
            # Buchstabenpaare entdeckt wurden).
            elif matrix[i-1][j-1] == max and max != 0:
                # Wir gehen in einem der beiden Eingabestrings (egal welcher) um den Wert im letzten Diagonalenfeld
                # zurück, um den neuesten längsten Substring zuerst in einer Liste abzuspeichern aus der wir anschlies-
                # send einen String für die Ausgabe machen.
                k = i-matrix[i-1][j-1]
                max_str_lst = []
                while k < i:
                    max_str_lst.append(lst_str1[k])
                    k+=1
                max_str = ''.join(max_str_lst)
                max_str_dict[max_str] = max

    for substr in max_str_dict:
        yield substr

#def main():
    #for str in longest_substrings('aooammmmss', 'oamss'):
        #print(str)

#if __name__ == '__main__':
    #main()






