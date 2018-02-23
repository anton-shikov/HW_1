#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 11:04:32 2017

@author: anton
"""




import argparse
import numpy as np

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='My parser try')
    parser.add_argument('-sq1', help='Input the first sequence', metavar='Str',type=str, default = 'ATG')
    parser.add_argument('-sq2', help='Input the second sequence', metavar='Str',type=str, default = 'CTA')
    args = parser.parse_args()
    seq1=args.sq1
    seq2=args.sq2
    
    def levendist(seq1, seq2):
        n, m = len(seq2), len(seq1)  # делавем провверку на длину строк, чтобы не вылететь по индексам
        if n > m:
            seq1, seq2 = seq2, seq1
            n, m = m, n
        Wmin = np.zeros((n+1, m+1))
        for i in range(1, m+1):
            Wmin[0][i] = Wmin[0][i-1]+1
        for j in range(1, n+1):
            Wmin[j][0] = Wmin[0][j-1]+1 
        for i in range(1, n+1):  # заполняем матрицу сравнения последовательностей
            for j in range(1, m+1):
                DEL = Wmin[i][j-1] + 1
                INS = Wmin[i-1][j] + 1
                MM = Wmin[i-1][j-1] + int(seq1[j-1] != seq2[i-1])
                Wmin[i][j] = min(INS, DEL, MM)
        i, j = n, m
        alignment1, alignment2 = [], []
        while i > 0 or j > 0:  # восстанавливаем значения выравнивания, двигаясь в обратном порядке
            DEL = Wmin[i][j-1] + 1
            INS = Wmin[i-1][j] + 1
            MM = Wmin[i-1][j-1] + int(seq1[j-1] != seq2[i-1])
            path = min(DEL, INS, MM)
            if path == MM and seq1[j-1] == seq2[i-1]:
                alignment1.append(seq1[j-1])
                alignment2.append(seq2[i-1])
                j -= 1
                i -= 1
            elif path == DEL:
                alignment1.append(seq1[j-1])
                alignment2.append("_")
                j -= 1
            elif path == INS:
                alignment1.append("_")
                alignment2.append(seq2[i-1])
                i -= 1
            elif path == MM and seq1[j-1] != seq2[i-1]:
                alignment1.append(seq1[j-1])
                alignment2.append(seq2[i-1])
                j -= 1
                i -= 1
        alignment1.reverse()
        alignment2.reverse()
        return(''.join(alignment1), ''.join(alignment2), Wmin[n][m])
        
        
    print(levendist(seq1, seq2))


