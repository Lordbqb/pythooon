# -*- coding: utf-8 -*-
"""
Created on Thu May  7 12:32:13 2026

@author: catko
"""

def hamming_distance(s: str, t: str) -> int:
    """
    Возвращает расстояние Хэмминга между двумя строками ДНК (равной длины).
    Длина каждой строки не должна превышать одной килобазы.
    """
    max_len = 1000
    if len(s) > max_len or len(t) > max_len:
        raise ValueError("длина последовательности больше допустимого")
    if len(s) != len(t):
        raise ValueError("строки должны быть равной длины")
    
    # Кол-во позиций, где символы различаются
    return sum(1 for a, b in zip(s, t) if a != b)


def random_dna(length: int) -> str:
    """Генерирует случайную строку ДНК заданной длины."""
    import random
    return ''.join(random.choices('ACGT', k=length))


if __name__ == "__main__":
    # Пример из задания
    s = "GAGCCTACTAACGGGAT"
    t = "CATCGTAATGACGGCCT"
    print(hamming_distance(s, t))
    s = random_dna(100)
    t = random_dna(100)
    print(hamming_distance(s, t))