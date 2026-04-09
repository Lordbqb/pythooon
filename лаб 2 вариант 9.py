# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 11:12:37 2026

@author: catko
"""
#лабораторная 1 вариант 9
from Bio import SeqIO
IN_path = "D:\\УЧЁБА\\Python\\lab 2\\вариант 9\\IN 1.txt"
seq = str((next(SeqIO.parse(IN_path, 'fasta'))).seq).upper()
complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

def is_too_long(IN_path):
    with open(IN_path, 'r', encoding='utf-8') as f:
        current_seq = ""
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                {}
            else:
                current_seq += line
        if len(current_seq) > 1024:
            print("sequence is too long") 
            return(True)
        return(False)
def is_reverse_palindrome(s):
    comp = ""
    for n in s:
        comp += complement[n]
    comp_rev = comp[::-1]
    return s == comp_rev
def reverse_palindromes(IN_path):
   results = []
   for i in range(len(seq)):
       for l in range(4, 13):
           if i + l <= len(seq):
               sub = seq[i:i+l]
               if is_reverse_palindrome(sub):
                   results.append((i+1, l))
   for a, b in results:
       print(a, b)

reverse_palindromes(IN_path)
##################################################
#черновик
# from Bio import SeqIO
# IN_path = "D:\\УЧЁБА\\Python\\lab 2\\вариант 9\\IN 1.txt"
# record = next(SeqIO.parse(IN_path, 'fasta'))
# seq = str(record.seq).upper()
# complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

# def is_too_long(IN_path):
#     with open(IN_path, 'r', encoding='utf-8') as f:
#         current_seq = ""
#         for line in f:
#             line = line.strip()
#             if line.startswith('>'):
#                 {}
#             else:
#                 current_seq += line
#         if len(current_seq) > 1024:
#             print("sequence is too long") 
#             return(True)
#         return(False)
# is_too_long(IN_path)

# # def reverse_complement(s):
# #     comp = ""
# #     for n in s:
# #         comp += complement[n]
# #     # or comp = ''.join(complement[n] for n in s)
# #     return comp[::-1]
# # reverse_complement("ATGC")

# def is_reverse_palindrome(s):
#     comp = ""
#     for n in s:
#         comp += complement[n]
#     # or comp = ''.join(complement[n] for n in s)
#     comp_rev = comp[::-1]
#     return s == comp_rev


# results = []
# for i in range(len(seq)):
#     for l in range(4, 13):
#         if i + l <= len(seq):
#             sub = seq[i:i+l]
#             if is_reverse_palindrome(sub):
#                 results.append((i+1, l))
# print(results)
# ##################################################
# seq = "TCAATGCATGCGGGTCTATATGCAT"
# results = []
# for i in range(len(seq)):
#     for l in range(4, 13):
#         if i + l <= len(seq):
#             sub = seq[i:i+l]
#             if is_reverse_palindrome(sub):
#                 results.append((i, l))
# for a, b in results:
#     print(a, b)