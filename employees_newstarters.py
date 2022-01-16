# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd

old_website_names = pd.read_csv("/Users/henry.wall/Documents/DESKTOP/employees data/website_employees.csv")

new_employees_names = pd.read_csv("/Users/henry.wall/Documents/DESKTOP/employees data/new_employees.csv")

list1 = old_website_names['NAME'].tolist()
list2 = new_employees_names['NAME'].tolist()

#print(list1)
#print(list2)

def diff(list1, list2):
    a = set(list1)
    b = set(list2)
    c = set(list1).union(set(list2))  
    d = set(list1).intersection(set(list2))
    return list(c - d)


def new(list1, list2):
    c = set(list1).union(set(list2))  
    a = set(list1)
    return list(c - a)

def old(list1, list2):
    c = set(list1).union(set(list2))  
    b = set(list2)
    return list(c - b)

print("THE DIFFERNCE BETWEEN THESE LISTS IS", diff(list1, list2))

print("THE NEW STARTERS ARE", new(list1, list2))

print("THE LEAVERS ARE", old(list1, list2))


