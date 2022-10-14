def engine(A, B, op):  # Function for finding hightest number of matches between the to two list.
    s = int(input(
        "Enter the number shifts to be performed"))  # Using s variable to get the shift value which to used to perform the no of shift on the list.
    A1, B1, M1, count1, shift1 = seq_A(A, B, s,
                                       op)  # Getting the return values in the variable A1,M1,B1 from the seq_A(A, B) and this the function call.
    A2, B2, M2, count2, shift2 = seq_B(A, B, s,
                                       op)  # Getting the return values in the variable A2,M2,B2 from the seq_A(A, B) and this the function call.
    if count1 > count2:  # If statement to test the condition count11>count2.
        if op == 1:
            print("The sequence matches with greatest score are :")
        elif op == 2:
            print("The sequence with greatest continues matches are :")
        # printing the sequences with most number of matches.
        print("Sequence A -> ", end=" ")
        for i in A1:
            print(i, end=" ")  # printing sequence A.
        print()
        print("              ", end=" ")
        for i in M1:
            print(i, end=" ")  # printing '|' to show the matches between the lists.
        print()
        print("Sequence B -> ", end=" ")
        for i in B1:
            print(i, end=" ")  # printing sequence B.
        print()
        if op == 1:
            print("we obtain this maximum number matches by shifting sequence A by", shift1, "positions")
            print("The score is", count1)  # printing the score value.
        elif op == 2:
            print("we obtain this maximum continues matches by shifting sequence A by", shift1, "positions")
            print("There are", count1, "continues characters in both the sequence")
        print()
        option = input("Do you want to go back to options menu 'Y' or 'N' \n")  # Option of the user to start again.
        if option.upper() == 'Y':  # checking the user option yes or no and upper() is used to convert lower to upper case.
            options(A, B)  # calling the options function.
        else:
            exit()  # if not y then exiting the program
    else:
        print("The sequence matches with greatest score are :")
        # printing the sequences with most number of matches.
        print("Sequence A -> ", end=" ")
        for i in A2:
            print(i, end=" ")  # printing sequence A.
        print()
        print("              ", end=" ")
        for i in M2:
            print(i, end=" ")  # printing '|' to show the matches between the lists.
        print()
        print("Sequence B -> ", end=" ")
        for i in B2:
            print(i, end=" ")  # printing sequence B.
        print()
        print("we obtain this maximum number matches by shifting sequence B by", shift2, "positions")
        print("The score is", count2)  # printing the score value.
        print()
        option = input("Do you want to go back to options menu 'Y' or 'N' \n")
        if option.upper() == 'Y':  # checking the user option yes or no and upper() is used to convert lower to upper case.
            options(A, B)  # calling the options function.
        else:
            exit()  # exiitng the program


def seq_A(A, B, s, op):  # seq_A function is used to compare the lists with more matches when seq_A is shifted.
    compare_list1 = []  # Three empty lists
    compare_list2 = []
    M = []
    count = 0  # count varaible for counting the number of matches.
    n = 1  # N is used to shift the variables
    for i in range(s):  # for loop with range s.
        list1, list2, shift = sequence1_shift(A, B,
                                              n)  # Function call of sequence1_shift(). Which return the shifted sequence of A
        C, D, matches, Score = sequence_compare(list1,
                                                list2)  # Function call of sequence_compare. Which returns the matches of the both A and B shifted sequence.
        if op == 1:  # When op is 1. It returns the highest number of matches.
            if Score > count:  # When score is greaterthan count it enters the if.
                compare_list1.clear()  # Clearing all the three lists uisng clear() to add new values.
                compare_list2.clear()
                M.clear()
                shifts = shift  # Initializing shifts with shift value as a copy.
                count = Score  # Initializing count with Score value as a copy.
                compare_list1.extend(C)  # Now updating the compare_list1 with new values which has more score.
                compare_list2.extend(D)  # Now updating the compare_list2 with new values which has more score.
                M.extend(matches)  # Now updating the M with new values which has the matches value denoted by '|'.
            n += 1  # Incrementing the n value.
        if op == 2:  # When op is 2. It returns the highest number of continues matches.
            con = compare_continous(
                matches)  # con is a variable used to call the compare_continues() function which returns the highest number of continues matches.
            if con > count:  # When con is greater than count entering if condition.
                compare_list1.clear()  # Clearing all the three lists uisng clear() to add new values.
                compare_list2.clear()
                M.clear()
                shifts = shift  # Initializing shifts with shift value as a copy.
                count = con  # Initializing count with con value as a copy.
                compare_list1.extend(C)  # Now updating the compare_list1 with new values which has more score.
                compare_list2.extend(D)  # Now updating the compare_list2 with new values which has more score.
                M.extend(matches)  # Now updating the M with new values which has the matches value denoted by '|'.
            n += 1  # Incrementing the n value.
    return compare_list1, compare_list2, M, count, shifts  # Returning the list 1 and 2 with highest no of continous matches, list with the '|' characters to denote the matches, Count has value of score or continues matches and shifts.


def seq_B(A, B, s, op):  # seq_B function is used to compare the lists with more matches when seq_B is shifted.
    compare_list1 = []  # Three empty lists
    compare_list2 = []
    M = []
    count = 0  # count varaible for counting the number of matches.
    n = 1  # N is used to shift the variables
    for i in range(s):  # for loop with range s.
        list1, list2, shift = sequence2_shift(A, B,
                                              n)  # Function call of sequence1_shift(). Which return the shifted sequence of A
        C, D, matches, Score = sequence_compare(list1,
                                                list2)  # Function call of sequence_compare. Which returns the matches of the both A and B shifted sequence.
        if op == 1:  # When op is 1. It returns the highest number of matches.
            if Score > count:  # When score is greaterthan count it enters the if.
                compare_list1.clear()  # Clearing all the three lists uisng clear() to add new values.
                compare_list2.clear()
                M.clear()
                shifts = shift  # Initializing shifts with shift value as a copy.
                count = Score  # Initializing count with Score value as a copy.
                compare_list1.extend(C)  # Now updating the compare_list1 with new values which has more score.
                compare_list2.extend(D)  # Now updating the compare_list2 with new values which has more score.
                M.extend(matches)  # Now updating the M with new values which has the matches value denoted by '|'.
            n += 1  # Incrementing the n value.
        if op == 2:  # When op is 2. It returns the highest number of continues matches.
            con = compare_continous(
                matches)  # con is a variable used to call the compare_continues() function which returns the highest number of continues matches.
            if con > count:  # When con is greater than count entering if condition.
                compare_list1.clear()  # Clearing all the three lists uisng clear() to add new values.
                compare_list2.clear()
                M.clear()
                shifts = shift  # Initializing shifts with shift value as a copy.
                count = con  # Initializing shifts with shift value as a copy.
                compare_list1.extend(C)  # Now updating the compare_list1 with new values which has more score.
                compare_list2.extend(D)  # Now updating the compare_list2 with new values which has more score.
                M.extend(matches)  # Now updating the M with new values which has the matches value denoted by '|'.
            n += 1  # Incrementing the n value.
    return compare_list1, compare_list2, M, count, shifts  # Returning the list 1 and 2 with highest no of continous matches, list with the '|' characters to denote the matches, Count has value of score or continues matches and shifts.


def sequence1_shift(seq_a, seq_b, n):  # Function definition of sequence1 shift.
    new_list1 = []  # Initializing two new lists.
    new_list2 = []
    new_list2.extend(seq_b)  # Adding the seq_b values directly into new_list2 using extend().
    for i in range(n):  # Now Adding the '-'to the lists to denote the no of shifts.
        new_list1.append("-")
        new_list2.append("-")
    for i in range(1):  # Now adding the seq A to the new_list1 using extend().
        new_list1.extend(seq_a)
    return new_list1, new_list2, n  # Returning the two shifted sequence A, B and no fo shifts with variable n.


def sequence2_shift(seq_a, seq_b, n):  # Function definition of sequence1 shift.
    new_list1 = []  # Initializing two new lists.
    new_list2 = []
    new_list1.extend(seq_a)  # Adding the seq_a values directly into new_list1 using extend().
    for i in range(n):
        new_list1.append("-")  # Now Adding the '-'to the lists to denote the no of shifts.
        new_list2.append("-")
    for i in range(1):  # Now adding the seq A to the new_list1 using extend().
        new_list2.extend(seq_b)
    return new_list1, new_list2, n  # Returning the two shifted sequence A, B and no fo shifts with variable n.


def compare_continous(
        M):  # Function definition for compare_continues). Which returns the higest number of continues matches count.
    count = 1  # Initializing Count with 1.
    con = 0  # Initializing Count with 1.
    for i in range(len(M) - 1):  # for loop to iterrate through the M list.
        if M[i] == '|' and M[i + 1] == '|':  # Checks if M[i] is equal to the M[i+1]. Where both as '|'.
            count += 1  # If true incrementing the value of count.
            con = count  # Making a copy of count in con for later use.
        else:
            count = 1  # If it is flase initializing count again with 1.
            continue  # Continuing the process until the list is completed.
    if con > count:  # If con is greater than the count.
        count = con  # Then replacing the count with con.
    return (count)  # Retuen Count value.


def sequence_compare(seq_a, seq_b):  # Function definition of sequence_compare.
    len1 = len(seq_a)  # getting length of seq_a in len1
    len2 = len(seq_b)  # getting length of seq_b in len2
    matches = []  # Initializing a list called matches
    count = 0  # Count variable to calculate the matches count
    for i in range(0, min(len1, len2)):  # for loop to iterate both the lists.
        if seq_a[i] != "-" and seq_b[i] != "-":  # Loop enters if the seq element is not the shifted or '-' character.
            if seq_a[i] == seq_b[i]:  # when the elements in the seq_a is equal to elements in seq_b.
                matches.append('|')  # We add '|' to the matches list.
                count += 1  # Increasing the count value.
            else:
                matches.append(' ')  # Adding an empty space to the matches list.
        else:
            matches.append(' ')  # Adding an empty space to the matches list.
    return seq_a, seq_b, matches, count  # Returning the values to the function call.


def options(A, B):  # Function call for the options(). Which peforms the task according to the user.
    print("\n*******SELECT AN OPTION*******")
    op = int(input("1. Number of matches\n2. Maximum chain\n"))  # variable op is used to get the user option.
    if op == 1 or op == 2:  # If op is not 1 or 2. It shows error and agian repeats.
        engine(A, B, op)  # Calling the function engine.
    else:
        print("Not a valid Input. Try again!!!")
        options(A, B)


def main():  # Function definition for the main.
    file_name1 = input("Enter the filename of the sequences \n")  # variable file_name1 is used to get the filename for the sequence A from the user.
    try:
        file1 = open(file_name1)  # open the file name 1.txt.
    except FileNotFoundError:  # Exceptional handling FileNotFoundError
        print("File not found!")
        return
    content1 = file1.readlines()  # read the file opened line by line and storing in variable content1.

    file_name2 = input("Enter the filename of the sequences \n")  # variable file_name2 is used to get the filename for the sequence B from the user.
    try:
        file2 = open(file_name2)  # open the file name 1.txt.
    except FileNotFoundError as e:  # Exceptional handling FileNotFoundError
        print(e)
        return

    content2 = file2.readlines()  # read the file opened line by line and storing in variable content2.

    A = list(content1[0])  # list A to store first line of file in list format.
    B = list(content2[0])  # list B to store second line of file in list format.
    C = []  # list C and D is used to store the character from A and B without the space respectively.
    D = []

    for i in A:
        if (i == " "):  # This IF statement skips the space character.
            continue
        elif i == "\n":  # This elif ends the loop when a \n character comes.
            break
        C.append(i)  # Here we store the value in to the new list C.
    for i in B:
        if i == " ":  # This IF statement skips the space character.
            continue
        elif i == "\n":  # This elif ends the loop when a \n character comes.
            break
        D.append(i)  # Here we store the value in to the new list D.

    A.clear()  # A.clear() is used to clear the data persent in the list A.
    B.clear()  # B.clear() is used to clear the data persent in the list B.
    A.extend(C)  # extend() function is used to extend the list A with values in list C.
    B.extend(D)  # extend() function is used to extend the list B with values in list D.
    C.clear()  # C.clear() is used to clear the data persent in the list C.
    D.clear()  # D.clear() is used to clear the data persent in the list D.
    len_A = len(A)  # Getting the length of A and B in len_A or len_B.
    len_B = len(B)

    if len_A == len_B:  # If length of both seq A and B is equal. Then the program has to run orelse it has to through error.
        print("The sequences present in the file are :")
        for i in A:  # Printing Sequence A.
            print(i, end=" ")
        print()
        for i in B:  # Printing Sequence B.
            print(i, end=" ")
        options(A, B)  # Calling the function option().
    else:
        raise Exception("Sorry, The length of both the sequence has to be same.")  # Exceptional Handling.


main()  # Calling the main function.





