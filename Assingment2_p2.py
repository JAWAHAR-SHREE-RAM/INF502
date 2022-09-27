def list_mangler(list_in):						#Definition of the funciton list_mangler
		new_list = []							#Empty list to store new values
		for i in list_in:
			if i % 2 == 0:						#Checking for even numbers
				i = i * 2 						#Performing square of even numbers
				new_list.append(i)				#Adding it to the new list
				
			else: 	
				i = i * 3						#Performing cube of odd numbers
				new_list.append(i)				#Adding it to the new list
	
		return new_list							#Returning the new list with updated values

list_in = []
print("Enter the elements for list_in : ")
for i in range(4):
		list_in.append(int(input())) 			#Getting the values for the list from the user
print(list_mangler(list_in))					#Function call of list_mangler and pasing the list (list_in) as argument