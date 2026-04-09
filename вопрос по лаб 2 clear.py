# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
lines = []
with open("DNA codon table.txt") as DNA_table:
    for line in DNA_table:
        lines.append(line.strip())

all_codons = []
all_aminos = []
for line in lines:
    parts = line.split()
    all_codons.extend(parts[0::2])   # extend добавляет все элементы списка
    all_aminos.extend(parts[1::2])

codon_table = {all_codons[i]: all_aminos[i] for i in range(len(all_codons))}

dna = ("AGACGGGGGTGGTGCGCAGCCCCTTCGAGTCCCCGCAGTACTACCTGG"
       "CTGAGCCGTGGCAGTTCTCCAT")

if len(dna) % 3 != 0:
    print("изначальный dna повреждён, обрезаем до кратной 3 длины")
    dna = dna[:len(dna) - len(dna) % 3]

protein = []
codon = None
for i in range(0, len(dna), 3):
    codon = dna[i: i+3]
    protein.append(codon_table[codon])

protein_as_string = ''.join(protein)

#print("DNA:", dna, "\n", "PROTEIN:", protein_as_string)
print(f"DNA: {dna}\nPROTEIN: {protein_as_string}")
