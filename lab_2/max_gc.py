# -*- coding: utf-8 -*-
"""
Created on Thu May  7 17:53:13 2026

@author: catko
"""

"""
Определение последовательности с максимальным процентом GC нуклеотидов.
(вариант 1 лабораторной работы 2)
"""

from Bio.SeqUtils import gc_fraction
from read_n_check_fasta import check_and_read_fasta

def find_highest_gc(records) -> tuple[str, float]:
    """
    Находит последовательность с максимальным GC-составом.
    """
    max_gc = -1.0
    max_gc_id = ""

    for record in records:
        gc = gc_fraction(record.seq)
        if gc > max_gc:
            max_gc = gc
            max_gc_id = record.id

    return max_gc_id, max_gc * 100


if __name__ == "__main__":
    input_path = "D:\\УЧЁБА\\Python\\lab 2\\вариант 1\\IN 1.txt"
    records = check_and_read_fasta(input_path)
    best_id, gc_percent = find_highest_gc(records)
    print(f"{best_id}\n{gc_percent:.6f}") 
    #обрезаем до 6 знаков после запятой, как в примере