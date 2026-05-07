# -*- coding: utf-8 -*-
"""
Created on Thu May  7 18:57:16 2026

@author: catko
"""

"""
Поиск реверсивных палиндромов в строке ДНК.
Вариант 9 лабораторной работы 2.
"""

from read_n_check_fasta import check_and_read_fasta #функция проверки fasta

# Таблица комплементарности ДНК
COMPLEMENT = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

# Ограничения по условию
MIN_PALINDROME_LEN = 4
MAX_PALINDROME_LEN = 12
MAX_SEQ_LENGTH = 1000


def is_reverse_palindrome(seq: str) -> bool:
    """
    Проверяет, является ли строка ДНК реверсивным палиндромом).
    """
    rev_comp = ''.join(COMPLEMENT[base] for base in reversed(seq))
    return seq == rev_comp


def find_reverse_palindromes(sequence: str) -> list[tuple[int, int]]:
    """
    Находит все реверсивные палиндромы заданной длины (от MIN до MAX).
    Возвращает список кортежей (позиция, длина).
    """
    results = []
    for i in range(len(sequence)):
        #проверяем подстроки
        for length in range(MIN_PALINDROME_LEN, MAX_PALINDROME_LEN + 1):
            if i + length <= len(sequence):
                sub = sequence[i: i + length]
                if is_reverse_palindrome(sub):
                    results.append((i + 1, length))   # позиция в условии – 1-based
    return results

if __name__ == "__main__":
    filepath = "D:\\УЧЁБА\\Python\\lab 2\\вариант 9\\IN 1.txt"
    records = check_and_read_fasta(filepath,
                                   MAX_SEQUENCES=1,
                                   MAX_LENGTH_PER_SEQUENCE=MAX_SEQ_LENGTH)
    record = records[0]
    sequence = str(record.seq).upper()
    palindromes = find_reverse_palindromes(sequence)
    for pos, length in palindromes:
        print(pos, length)