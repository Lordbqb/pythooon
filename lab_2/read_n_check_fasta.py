# -*- coding: utf-8 -*-
"""
Created on Thu May  7 19:13:56 2026

@author: catko
"""

from Bio import SeqIO
import warnings


def check_and_read_fasta(filepath: str, 
                         MAX_SEQUENCES: int = 10, 
                         MAX_LENGTH_PER_SEQUENCE: int = 1000):
    """
    Проверяет файл FASTA на соответствие ограничениям.
    Возвращает последовательности.
    """
    records = []
    with open(filepath, 'r', encoding='utf-8') as f:
        seq_len = 0
        seq_count = 0

        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if seq_count >= MAX_SEQUENCES:
                    raise ValueError(
                        f"Количество последовательностей превышает {MAX_SEQUENCES}"
                    )
                if seq_count > 0 and seq_len == 0:
                    #последовательность закончилась, но она была длины 0
                    warnings.warn("Пустая последовательность (будет пропущена)")
                seq_len = 0
                seq_count += 1
            else:
                if seq_count == 0: #если файл начался не с ">"
                    raise ValueError(
                        "Файл не соответствует формату FASTA"
                    )
                seq_len += len(line)
                if seq_len > MAX_LENGTH_PER_SEQUENCE:
                    raise ValueError(
                        f"Последовательность длиннее {MAX_LENGTH_PER_SEQUENCE} символов"
                    )

        #для последней последовательности
        if seq_len > MAX_LENGTH_PER_SEQUENCE:
            raise ValueError(
                f"Последовательность длиннее {MAX_LENGTH_PER_SEQUENCE} символов"
            )

    #если проверки пройдены, читаем через SeqIO
    records = list(SeqIO.parse(filepath, "fasta"))
    if not records:
        raise ValueError("Файл не содержит ни одной последовательности")
    return records