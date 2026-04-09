# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#вариант 1
def rabbits1(n, k):
    month = [0, 1]
    for i in range(1, n):
        update = month[i]+month[i-1]*k
        month.append(update)
    return(month[n])
rabbits1(6, 3)

#########################
#вариант 2

def rabbits2(n, m):
    for_ages =  [0]*m
    for_ages[0] = 1
    for month in range(1, n):
        update = sum(for_ages[1:])
        for_ages = [update] + for_ages[:m-1]
    return sum(for_ages)
rabbits2(6, 3)

# test = [i for i in range(11)]
# test[1:]
# test[:10]
###################################
#вариант 3
s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"

def how_many_diff(s, t):
    if len(s)>1025:
        return("длина последовательности больше допустимого")
    if len(s) != len(t):
        return("длина последовательности больше допустимого")
    s = str(s)
    t = str(t)
    s_list = list()
    for i in range(0, len(s)):
        add = s[i] + str(i)
        s_list.append(add)
    t_list = list()
    for i in range(0, len(s)):
        add = t[i] + str(i)
        t_list.append(add)
    return(len(set(s_list) - set(t_list)))
how_many_diff(s, t)
import random

def random_seq(lenght):
    seq = ""
    for i in range(0, lenght):
        seq = seq + random.choice(['A', 'C', 'G', 'T'])
    return(seq)
l = 100
a = random_seq(l)
b = random_seq(l)
how_many_diff(a, b)