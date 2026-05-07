# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 13:09:09 2026

@author: catko
"""
#лабораторная 1 вариант 1
#вариант 1
def rabbits(n: int, k: int) -> int:
    """
    Вычисляет количество пар кроликов на n-й месяц.
    Каждая взрослая пара приносит k пар ежемесячно.
    """
    if n <= 2:
        return 1
    pairs = [0, 1]    # кол-во пар кроликов в месяц 0 и месяц 1
    for i in range(1, n):
        update = pairs[i] + pairs[i-1] * k
        pairs.append(update)
    return pairs[n]
rabbits(6, 3)

###############################
# def rabbits1(n, k):
#     month = [0, 1]
#     for i in range(1, n):
#         update = month[i]+month[i-1]*k
#         month.append(update)
#     return(month[n])
# rabbits1(6, 3)