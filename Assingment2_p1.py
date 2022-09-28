from math import hypot  #importing hypot fucntion from math library

def pythagoreanTheorem(a, b): #pythagorean theorem function used to calcualte hypotenues
	c = hypot(a, b)
	print(c)


a = int(input("Enter the length a : "))  #Getting lenght of side A from user
b = int(input("Enter the length b : "))  #Getting lenght of side B from user
pythagoreanTheorem(a, b)				 #Calling the function to perform the calculation


