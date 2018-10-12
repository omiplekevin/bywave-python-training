# -*- coding: utf-8 -*-
"""
Write a program that accepts an input value (range: 60-100)
and prints a message based on the following range of values:

RANGE                   MESSAGE
60 to 74                Derp!
75 to 84                Good
85 to 94                Very Good
95 to 100               Level Asian!
any other value         Invalid Value
"""

# your name and email address here
__author__ = 'xXLXx <kevin@bywave.com.au>'


if __name__ == '__main__':
	x = input()
	if x < 60 or x > 100:
		print "Invalid Value"
	elif x in range(60, 75):
		print "Derp!"
	elif x in range(75, 85):
		print "Good"
	elif x in range(85, 95):
		print "Very Good"
	elif x in range(95, 101):
		print "Level Asian!"