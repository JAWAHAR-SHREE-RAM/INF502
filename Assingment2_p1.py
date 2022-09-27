from math import hypot
#import math


def pythagoreanTheorem(a, b):
	c = hypot(a, b)
	print(c)


a = int(input("Enter the length a : "))
b = int(input("Enter the length b : "))
pythagoreanTheorem(a, b)


