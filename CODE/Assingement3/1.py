def wallets(wallet):                                        #Function to Calculate fatest , Skinnest, total value in wallet
    fattest_wallet = max(wallet)                #Gives maximum of the wallet
    skinniest_wallet = min(wallet)              #Gives minimum of the wallet
    Total_value = sum(wallet)                   #Gives total value of the wallet

    return fattest_wallet, skinniest_wallet, Total_value  #Return statement

wallet = []         #Empty list
n = int(input("How much wallets you want to add to the list"))  #Getting the user input for lenght
print("Enter the value to be added")
for i in range(n):
     value = int(input())                          #Getting the value for the wallet from the user
     wallet.append(value)                       #adding the wallets to the list
fattest_wallet, skinniest_wallet, Total_value = wallets(wallet)             #Function call of the wallets with attribute wallet

#Printing the values
print("The value of Fattest wallet is $",fattest_wallet)
print("The value of Fattest wallet is $",skinniest_wallet)
print("The value of all the wallet is $",Total_value)
print("There are",Total_value*10, "dimes in all the wallet" )


