# Bit Manipulation: Lonely Integer HankerRank Challenge

This is a solution and explanation to one [This challenge](https://www.hackerrank.com/challenges/ctci-lonely-integer)

## The Challenge

The prompt is rather straightforward:

```
Consider an array of n integers, where all but one of the integers occur in pairs. In other words, every element in  occurs exactly twice except for one unique element.

Given an array, find and print the unique element.
```

So we know we will be given several tests each containing all pairs of elements, except for one lone element. How can we determine what that unique element is?

We are also given the start of a method:

```
#!/bin/python

import sys

def lonely_integer(a):
    

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
print lonely_integer(a)
```

## The Solution

We know that we want to traverse any array we are given, and then compare elements in order to find the one element that is unique.  The easiest way to do this is with a for, as in `for elements in the array` and one of the easiest comparisons we can employ is the XOR logical operator `^=` in which we return a value only when two elements are different. 

