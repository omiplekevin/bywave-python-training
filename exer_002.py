# -*- coding: utf-8 -*-
"""
Exercise #2
Write a program that prints all multiples of 7 that are below 100.

Hints:
check python’s range Function
"""

# your name and email address here
__author__ = 'xXLXx <kevin@bywave.com.au>'


if __name__ == '__main__':
	mods = [x for x in range(0,100) if x % 7 == 0]
	print(mods)
    # for x in range(0,100,7):
    # 		print x