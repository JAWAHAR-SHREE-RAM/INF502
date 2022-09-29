1. Write a function with the following signature: pythagoreanTheorem(length_a, length_b).The function returns the length of the hypotenuse assuming that length_a and length_b are the lengths of the two legs of a right triangle (the legs that form the triangle's right angle). Hint: the math module might have useful functions to use.

CODE :
```python
from math import hypot  		    #importing hypot fucntion from math library

def pythagoreanTheorem(a, b): 	#pythagorean theorem function used to calcualte hypotenues
	c = hypot(a, b)               #hypot function is a default function to calculate hypotenues and storing it in c variable
	print(c)                      #printing the value stored in c

a = int(input("Enter the length a : "))     #Getting lenght of side A from user
b = int(input("Enter the length b : "))     #Getting lenght of side B from user
pythagoreanTheorem(a, b)		    #Calling the function to perform the calculation

```
EXPLANATION:

Getting the length of the two sides in the triangle a and b from the user and calculating the thrid side of the triangle which is hypotenues. I used hypot a predefined function in python under math library to find the hypotenuse.


CODE LINK:

[Program1](https://github.com/JAWAHAR-SHREE-RAM/INF502/blob/main/CODE/Assingment2/1.py)

OUTPUT :
```
ram@Jawahars-MBP python % python3 Assingment2_p1.py     #compiling the code
Enter the length a : 3                                  #Input of length A
Enter the length b : 4                                  #Input of length B
5.0                                                     #printing the hypotenues value
ram@Jawahars-MBP python % python3 Assingment2_p1.py     #compiling the code
Enter the length a : 6                                  #Input of length A
Enter the length b : 7                                  #Input of length B
9.219544457292887                                       #printing the hypotenues value
ram@Jawahars-MBP python % python3 Assingment2_p1.py     #compiling the code
Enter the length a : 8                                  #Input of length A
Enter the length b : 2                                  #Input of length B
8.246211251235321                                       #printing the hypotenues value
ram@Jawahars-MBP python % python3 Assingment2_p1.py     #compiling the code
Enter the length a : 6                                  #Input of length A
Enter the length b : 7                                  #Input of length B
9.219544457292887                                       #printing the hypotenues value
ram@Jawahars-MBP python % python3 Assingment2_p1.py     #compiling the code
Enter the length a : 13                                 #Input of length A
Enter the length b : 18                                 #Input of length B
22.203603311174515                                      #printing the hypotenues value
ram@Jawahars-MBP python % 

```

2. Write a function with the following signature: list_mangler(list_in).The function assumes that list_in is a list of integers, and returns a new list containing transformed elements of list_in. If the element is even, it's doubled. If the element is odd, it's tripled.

CODE :
```python
def list_mangler(list_in):			        			#Definition of the funciton list_mangler
		new_list = []							                #Empty list to store new values
		for i in list_in:
			if i % 2 == 0:						              #Checking for even numbers
				i = i * 2					                    #Performing twice of even numbers
				new_list.append(i)				            #Adding it to the new list
				
			else: 	
				i = i * 3					                    #Performing thrice of odd numbers
				new_list.append(i)				            #Adding it to the new list
	
		return new_list							              #Returning the new list with updated values

list_in = []                                  #Intializing empty list named list_in 
print("Enter the elements for list_in : ")    #print statement to get input from the user
for i in range(4):                            #for loop to get the user input
		list_in.append(int(input())) 			       	#Getting the values for the list from the user
print(list_mangler(list_in))					        #Function call of list_mangler and pasing the list (list_in) as argument

```

EXPLANATION:

Getting the user input for the list and performing the calculation inside the function. The calculation performs twice of even numbers and thrice of odd numbers and return the new update list.

CODE LINK:

[Program2](https://github.com/JAWAHAR-SHREE-RAM/INF502/blob/main/CODE/Assingment2/2.py)

OUTPUT :

```
ram@Jawahars-MacBook-Pro python % python3 Assingment2_p2.py     #Compiling the python file using python3 command
Enter the elements for list_in :                                #Getting the user input in the list
1
2
3
4
[3, 4, 9, 8]                                                    #Printing the new list
ram@Jawahars-MacBook-Pro python % python3 Assingment2_p2.py     #Compiling the python file using python3 command
Enter the elements for list_in :                                #Getting the user input in the list
2
1
5
8
[4, 3, 15, 16]                                                  #Printing the new list
ram@Jawahars-MacBook-Pro python % python3 Assingment2_p2.py     #Compiling the python file using python3 command
Enter the elements for list_in :                                #Getting the user input in the list
9
3
6
4
[27, 9, 12, 8]                                                  #Printing the new list
ram@Jawahars-MacBook-Pro python % python3 Assingment2_p2.py     #Compiling the python file using python3 command
Enter the elements for list_in :                                #Getting the user input in the list
12
76
34
99
[24, 152, 68, 297]                                              #Printing the new list


```
3. Write a function with the following signature: grade_calc(grades_in, to_drop).The function accepts a list grades_in containing integer grades, drops the to_drop lowest grades (so, for to_drop equal to 2, the function should drop the 2 lowest grades), calculates the average of the grades left, and returns the letter grade this average corresponds to according to the letter grade scale for this course.

CODE :
```python
def grade_call(grades_in, to_drop):
	d = to_drop
	grades_in.sort()							      	# sort grades in ascending order
	#print(grades_in)												
	n = len(grades_in) - d 						  	#Getting the length of updated list
	for i in range(d-1):
		grades_in.pop(i)						      	#removing the lowest grades
	for i in range(d-1):
		grades_in.pop(i)			
	#print(grades_in)
	total = 0                          		# initialize total to zero
  avg = 0 									            # initialize average to zero
	
	
	for i in range(len(grades_in)):
		total += grades_in[i]					      # calculating total of grades 
		
		
	if n != 0:									          #If condition to check the n is zero or not								
		avg = total/n
		#print(avg)

	if avg >= 90:								          # return according to letter grade scale
		return 'A'
	elif avg < 90 and avg >= 80:
		return 'B'
	elif avg < 80 and avg >= 70:
		return 'C'
	elif avg < 70 and avg >= 60:
		return 'D'
	elif avg < 60:
		return 'F'


	
grade = []                              #list named grade as been initialized
print("Enter the elements for list_in : ")
for i in range(5):                      #for loop to get the user input
		grade.append(int(input()))          #Appending the values to the list    
print (grade_call(grade, 2))            # call the function and print result

```

EXPLANATION:

Getting a grade list from the user and dropping two least grades and then calculating the average of the grades. After returning the equivalent letter grade of that average.
 
CODE LINK:

[Program3](https://github.com/JAWAHAR-SHREE-RAM/INF502/blob/main/CODE/Assingment2/3.py)


OUTPUT:
```
ram@Jawahars-MBP python % python3 Assingment2_p3.py
Enter the elements for list_in :                      #Entering the input for the list
100
87
76
58
92
Old grades :                                        #Printing the old grades that is the original grades given user in the list
[58, 76, 87, 92, 100]
New grades :                                        #Printing the updated list of grades
[87, 92, 100]
Average :                                            #Printing the average
93.0
A                                                   #Printing the grade
ram@Jawahars-MBP python % python3 Assingment2_p3.py
Enter the elements for list_in :                    #Entering the input for the list
78
89
86
90
68
Old grades :                                         #Printing the old grades that is the original grades given user in the list
[68, 78, 86, 89, 90]
New grades :                                         #Printing the updated list of grades
[86, 89, 90]
Average :                                            #Printing the average
88.33333333333333
B                                                   #Printing the grade
ram@Jawahars-MBP python % python3 Assingment2_p3.py
Enter the elements for list_in :                    #Entering the input for the list
99
89
79
85
75
Old grades :                                      #Printing the old grades that is the original grades given user in the list
[75, 79, 85, 89, 99]
New grades :                                      #Printing the updated list of grades
[85, 89, 99]
Average :                                         #Printing the average
91.0
A                                                 #Printing the grade
ram@Jawahars-MBP python % python3 Assingment2_p3.py
Enter the elements for list_in :                  #Entering the input for the list
67
78
75
80
65
Old grades :                                      #Printing the old grades that is the original grades given user in the list
[65, 67, 75, 78, 80]
New grades :                                      #Printing the updated list of grades 
[75, 78, 80]
Average :                                         #Printing the average
77.66666666666667
C                                                 #Printing the grade
ram@Jawahars-MBP python % 
```

4. Write a function with the following signature: odd_even_filter(numbers).The function accepts an input list of integers and returns a list with two sublists. The first sublist contains all even numbers in the input list and the second sublist contains all odd numbers.

CODE :
```python
def odd_even_filter(numbers):
    even_list = []                              #Empty even list
    odd_list = []                               #Empty odd list
    for i in numbers:
        if (i % 2 == 0):                        #Checking the list for even numbers
            even_list.append(i)                 #Adding the even numbers to the empty even numbers list
        else:
            odd_list.append(i)                  #Adding the even numbers to the empty even numbers list
    print("Even lists:", even_list)
    print("Odd lists:", odd_list)
  

numbers = []                                    #Empty numbers list
print("Enter the elements for list_in : ")
for i in range(4):                              #For loop to get the input from user
        numbers.append(int(input())) 
odd_even_filter(numbers)                        #Function call of odd_even_filter() 

```

EXPLANATION:

Getting a list of even and odd numbers mixed from the user and then print the even numbers in a separate list and odd numbers in separate list.


CODE LINK:

[Program4](https://github.com/JAWAHAR-SHREE-RAM/INF502/blob/main/CODE/Assingment2/4.py)

OUTPUT:
```
ram@Jawahars-MBP python % python3 Assingment2_p4.py    #compiling the code in the terminal
How many number of elements :                          #Asking the user about the no of elements in the list 
None7
Enter the elements for list_in :                      #Entering the input for the list
4
8
1
9
45
62
37
Even lists: [4, 8, 62]
Odd lists: [1, 9, 45, 37]
ram@Jawahars-MBP python % python3 Assingment2_p4.py   #compiling the code in the terminal
How many number of elements :                         #Asking the user about the no of elements in the list 
None10
Enter the elements for list_in :                      #Entering the input for the list
1
2
3
4
5
6
7
8
9
10
Even lists: [2, 4, 6, 8, 10]
Odd lists: [1, 3, 5, 7, 9]
ram@Jawahars-MBP python % python3 Assingment2_p4.py   #compiling the code in the terminal
How many number of elements :                         #Asking the user about the no of elements in the list 
None6
Enter the elements for list_in :                      #Entering the input for the list 
12
45
72
19
39
66
Even lists: [12, 72, 66]
Odd lists: [45, 19, 39]
ram@Jawahars-MBP python % 
```
