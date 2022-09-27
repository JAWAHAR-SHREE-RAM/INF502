def odd_even_filter(numbers):
    even_list = []                              #Empty even list
    odd_list = []                               #Empty odd list
    for i in numbers:
        if (i % 2 == 0):                        #Checking the list for even numbers
            even_list.append(i)                     #Adding the even numbers to the empty even numbers list
        else:
            odd_list.append(i)                     #Adding the even numbers to the empty even numbers list
    print("Even lists:", even_list)
    print("Odd lists:", odd_list)
  

numbers = [] 
n = int(input(print("How many number of elements :")))                                  #Empty numbers list
print("Enter the elements for list_in : ")
for i in range(n):                              #For loop to get the input from user
        numbers.append(int(input())) 
odd_even_filter(numbers)                        #Function call of odd_even_filter() 