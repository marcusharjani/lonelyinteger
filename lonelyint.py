#!/bin/python

import sys

def lonely_integer(a):
    answer = 0
    for i in a:
        answer ^= i
    return answer

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
print lonely_integer(a)
