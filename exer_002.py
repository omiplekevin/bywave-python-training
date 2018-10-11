# -*- coding: utf-8 -*-
"""
Exercise #2
Write a program that prints all multiples of 7 that are below 100.

Hints:
check python’s range Function
"""

# your name and email address here
__author__ = 'xXLXx <leo@bywave.com.au>'


if __name__ == '__main__':
    def print_multiples(multiple, limit):
        for x in range(1, limit//multiple + 1):
            print(x*multiple)


    print_multiples(7, 100)
