# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#лабораторная 2 вариант 1
#чистый:
def check_num(IN_path):
    with open(IN_path, 'r', encoding='utf-8') as f:
        count = 0
        for line in f:
            if line.startswith('>'):
                count += 1
            if count > 10:
                return(True)
        return(False)

def check_len(IN_path):
    with open(IN_path, 'r', encoding='utf-8') as f:
        current_seq = ""
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if len(current_seq) > 1024:
                     return(True)
                current_seq = ""
            else:
                current_seq += line
        if len(current_seq) > 1024:
             return(True)
        return(False)

def max_gs(IN_path):
    check_total = check_num(IN_path) or check_len(IN_path)
    if check_total:
        print("Файл не соотв. требованиям")
        return
    from Bio import SeqIO
    from Bio.SeqUtils import gc_fraction
    records = list(SeqIO.parse(IN_path, 'fasta'))
    gs = 0
    gs_id = 0
    for i in range(len(records)):
        gs_add = gc_fraction(records[i].seq)
        if gs_add > gs:
            gs = gs_add
            gs_id = i
    print(f"{records[gs_id].id}\n{gs*100:.6f}")

max_gs("D:\\УЧЁБА\\Python\\lab 2\\вариант 1\\IN test.txt")
max_gs("D:\\УЧЁБА\\Python\\lab 2\\вариант 1\\IN 0.txt")

#########################################################
from Bio import SeqIO

IN_path = "D:\УЧЁБА\Python\lab 2\вариант 1\IN 1.txt"
records = list(SeqIO.parse(IN_path, 'fasta'))

# from Bio.SeqUtils import gc_fraction  # функция для расчёта GC-состава
# gc_fraction(records[0].seq)

# for record in records:
#     print(f"{record.id}: {len(record.seq)} нуклеотидов")

from Bio.SeqUtils import gc_fraction

# gs = 0
# for record in records:
#     gs_add = gc_fraction(record.seq)
#     print(f"gs = {gs:.3f} and gs_add = {gs_add:.3f}")
#     if gs_add > gs:
#         gs = gs_add

gs = 0
gs_id = 0
for i in range(len(records)):
    gs_add = gc_fraction(records[i])
    if gs_add > gs:
        gs = gs_add
        gs_id = i
print(f"max gs ({gs}) in seq {gs_id}")
print(f"{records[gs_id].id}\n{gs*100:.6f}")
#########################################################
IN_path = "D:\\УЧЁБА\\Python\\lab 2\\вариант 1\\IN 0.txt"
with open(IN_path, 'r', encoding='utf-8') as f:
    count = 0
    for line in f:
        if line.startswith('>'):
            count += 1

with open(IN_path, 'r', encoding='utf-8') as f:
    current_seq = ""
    for line in f:
        line = line.strip()
        if line.startswith('>'):
            print(current_seq)
            print(len(current_seq))
            # if len(current_seq) > 1024:
            #     print(f"Слишком длинная seq: {len(current_seq)} букв")
            current_seq = ""
        else:
            current_seq += line
            # current_seq.append(line)
    print(current_seq)
    print(len(current_seq))
#########################################################
# def check_num(IN_path):
#     with open(IN_path, 'r', encoding='utf-8') as f:
#         count = 0
#         for line in f:
#             if line.startswith('>'):
#                 count += 1
#             if count > 10:
#                 #print("Cлишком много последовательностей")
#                 return(True)
#         return(False)
IN_path = "D:\\УЧЁБА\\Python\\lab 2\\вариант 1\\IN test.txt"
check_num(IN_path)

# def check_len(IN_path):
#     with open(IN_path, 'r', encoding='utf-8') as f:
#         current_seq = ""
#         for line in f:
#             line = line.strip()
#             if line.startswith('>'):
#                 if len(current_seq) > 1024:
#                      #print(f"Слишком длинная seq: {len(current_seq)}")
#                      return(True)
#                 current_seq = ""
#             else:
#                 current_seq += line
#         if len(current_seq) > 1024:
#              #print(f"Слишком длинная seq: {len(current_seq)}")
#              return(True)
#         return(False)
IN_path = "D:\\УЧЁБА\\Python\\lab 2\\вариант 1\\IN test.txt"
check_len(IN_path)

if check_num(IN_path):
    print("Error num")
if check_len(IN_path):
    print("Error len")