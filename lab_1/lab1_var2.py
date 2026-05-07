# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 13:24:58 2026

@author: catko
"""
#лабораторная 1 вариант 2
def mortal_rabbits(n: int, m: int) -> int:
    """
    Возвращает количество пар кроликов на n-й месяц,
    если каждая пара живёт ровно m месяцев.
    Кролики достигают зрелости в возрасте 1 месяц и затем
    каждый месяц приносят одну пару потомства.
    """
    # Индексы списка: 0 — новорождённые, 1 — возраст 1 месяц, 
    # ..., m-1 — возраст m-1 (последний перед смертью)
    ages = [1] + [0] * (m - 1)
    for _ in range(1, n):
        newborns = sum(ages[1:])          
        # все взрослые (возраст >= 1) дают потомство
        ages = [newborns] + ages[:m-1]    
        # сдвиг возрастов, старейшие умирают
    return sum(ages)

###############################
# def rabbits2(n, m):
#     for_ages =  [0]*m
#     for_ages[0] = 1
#     for month in range(1, n):
#         update = sum(for_ages[1:])
#         for_ages = [update] + for_ages[:m-1]
#     return sum(for_ages)
# rabbits2(6, 3)