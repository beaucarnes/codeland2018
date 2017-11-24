'''
CODELAND 2018
Project 2: Recursion
---
Just like in project 1, you have to create a selection sort algorithm that sorts an array. This time,
however, you must use recursion. In the iterative approach from project 1, there were two loops.
That means there are two places you can use recursion. However, it is only required that you use
recursion once to pass this challenge. The function should sort the people array from 'contactapp.py'. The
algorithm should sort by 'name' or 'age', depending on what is passed in. To check, run 'contactapp.py'
and verify that when you print contacts, the program accurately sorts list based on the given parameter.
'''

def sort(list, sort_by):