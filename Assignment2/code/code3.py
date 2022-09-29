
def grade_call(grades_in, to_drop):
	d = to_drop
	grades_in.sort()							# sort grades in ascending order
	print("Old grades : ")
	print(grades_in)												
	n = len(grades_in) - d 						#Getting the length of updated list
	for i in range(d-1):
		grades_in.pop(i)						#removing the lowest grades
	for i in range(d-1):
		grades_in.pop(i)			
	print("New grades : ")
	print(grades_in)
	total = 0
	avg = 0 									# initialize average to zero
	
	
	for i in range(len(grades_in)):
		total += grades_in[i]					# calculating total of grades 
		
		
	if n != 0:									#If condition to check the n is zero or not								
		avg = total/n
		print("Average : ")
		print(avg)

	if avg >= 90:								# return according to letter grade scale
		return 'A'
	elif avg < 90 and avg >= 80:
		return 'B'
	elif avg < 80 and avg >= 70:
		return 'C'
	elif avg < 70 and avg >= 60:
		return 'D'
	elif avg < 60:
		return 'F'


	# call the function and print result
grade = []
print("Enter the elements for list_in : ")
for i in range(5):
		grade.append(int(input())) 
print (grade_call(grade, 2))
