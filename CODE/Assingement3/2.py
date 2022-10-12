import json             #Importing json

# Entering the periodic table elements in to a dictionary
periodic_table_elements = {"H":{"Row":1,"Column":1,"Atomic Number":1,"Name":"Hydrogen"}, "He":{"Row":1,"Column":18,"Atomic Number":2,"Name":"Helium"}, "Li":{"Row":2,"Column":1,"Atomic Number":3,"Name":"Lithium"}, "Be":{"Row":2,"Column":2,"Atomic Number":4,"Name":"Beryllium"}, "B":{"Row":2,"Column":13,"Atomic Number":5,"Name":"Boron"}, "C":{"Row":2,"Column":14,"Atomic Number":6,"Name":"Carbon"}, "N":{"Row":2,"Column":15,"Atomic Number":7,"Name":"Nitrogen"}, "O":{"Row":2,"Column":16,"Atomic Number":8,"Name":"Oxygen"}, "F":{"Row":2,"Column":17,"Atomic Number":9,"Name":"Fluorine"}, "Ne":{"Row":2,"Column":18,"Atomic Number":10,"Name":"Neon"}, "Na":{"Row":3,"Column":1,"Atomic Number":11,"Name":"Sodium"}, "Mg":{"Row":3,"Column":2,"Atomic Number":12,"Name":"Magnesium"}, "Al":{"Row":3,"Column":13,"Atomic Number":13,"Name":"Aluminum"}, "Si":{"Row":3,"Column":14,"Atomic Number":14,"Name":"Silicon"}, "P":{"Row":3,"Column":15,"Atomic Number":15,"Name":"Phosphorus"}, "S":{"Row":3,"Column":16,"Atomic Number":16,"Name":"Sulfur"}, "Cl":{"Row":3,"Column":17,"Atomic Number":17,"Name":"Chlorine"}, "Ar":{"Row":3,"Column":18,"Atomic Number":18,"Name":"Argon"}, "K":{"Row":4,"Column":1,"Atomic Number":19,"Name":"Potassium"}, "Ca":{"Row":4,"Column":2,"Atomic Number":20,"Name":"Calcium"}, "Sc":{"Row":4,"Column":3,"Atomic Number":21,"Name":"Scandium"}, "Ti":{"Row":4,"Column":4,"Atomic Number":22,"Name":"Titanium"}, "V":{"Row":4,"Column":5,"Atomic Number":23,"Name":"Vanadium"}, "Cr":{"Row":4,"Column":6,"Atomic Number":24,"Name":"Chromium"}, "Mn":{"Row":4,"Column":7,"Atomic Number":25,"Name":"Manganese"}, "Fe":{"Row":4,"Column":8,"Atomic Number":26,"Name":"Iron"}, "Co":{"Row":4,"Column":9,"Atomic Number":27,"Name":"Cobalt"}, "Ni":{"Row":4,"Column":10,"Atomic Number":28,"Name":"Nickel"}, "Cu":{"Row":4,"Column":11,"Atomic Number":29,"Name":"Copper"}, "Zn":{"Row":4,"Column":12,"Atomic Number":30,"Name":"Zinc"}, "Ga":{"Row":4,"Column":13,"Atomic Number":31,"Name":"Gallium"}, "Ge":{"Row":4,"Column":14,"Atomic Number":32,"Name":"Germanium"}, "As":{"Row":4,"Column":15,"Atomic Number":33,"Name":"Arsenic"}, "Se":{"Row":4,"Column":16,"Atomic Number":34,"Name":"Selenium"}, "Br":{"Row":4,"Column":17,"Atomic Number":35,"Name":"Bromine"}, "Kr":{"Row":4,"Column":18,"Atomic Number":36,"Name":"Krypton"}, "Rb":{"Row":5,"Column":1,"Atomic Number":37,"Name":"Rubidium"}, "Sr":{"Row":5,"Column":2,"Atomic Number":38,"Name":"Strontium"}, "Y":{"Row":5,"Column":3,"Atomic Number":39,"Name":"Yttrium"}, "Zr":{"Row":5,"Column":4,"Atomic Number":40,"Name":"Zirconium"}, "Nb":{"Row":5,"Column":5,"Atomic Number":41,"Name":"Niobium"}, "Mo":{"Row":5,"Column":6,"Atomic Number":42,"Name":"Molybdenum"}, "Tc":{"Row":5,"Column":7,"Atomic Number":43,"Name":"Technetium"}, "Ru":{"Row":5,"Column":8,"Atomic Number":44,"Name":"Ruthenium"}, "Rh":{"Row":5,"Column":9,"Atomic Number":45,"Name":"Rhodium"}, "Pd":{"Row":5,"Column":10,"Atomic Number":46,"Name":"Palladium"}, "Ag":{"Row":5,"Column":11,"Atomic Number":47,"Name":"Silver"}, "Cd":{"Row":5,"Column":12,"Atomic Number":48,"Name":"Cadmium"}, "In":{"Row":5,"Column":13,"Atomic Number":49,"Name":"Indium"}, "Sn":{"Row":5,"Column":14,"Atomic Number":50,"Name":"Tin"}, "Sb":{"Row":5,"Column":15,"Atomic Number":51,"Name":"Antimony"}, "Te":{"Row":5,"Column":16,"Atomic Number":52,"Name":"Tellurium"}, "I":{"Row":5,"Column":17,"Atomic Number":53,"Name":"Iodine"}, "Xe":{"Row":5,"Column":18,"Atomic Number":54,"Name":"Xenon"}, "Cs":{"Row":6,"Column":1,"Atomic Number":55,"Name":"Cesium"}, "Ba":{"Row":6,"Column":2,"Atomic Number":56,"Name":"Barium"}, "La":{"Row":8,"Column":3,"Atomic Number":57,"Name":"Lanthanum"}, "Ce":{"Row":8,"Column":4,"Atomic Number":58,"Name":"Cerium"}, "Pr":{"Row":8,"Column":5,"Atomic Number":59,"Name":"Praseodymium"}, "Nd":{"Row":8,"Column":6,"Atomic Number":60,"Name":"Neodymium"}, "Pm":{"Row":8,"Column":7,"Atomic Number":61,"Name":"Promethium"}, "Sm":{"Row":8,"Column":8,"Atomic Number":62,"Name":"Samarium"}, "Eu":{"Row":8,"Column":9,"Atomic Number":63,"Name":"Europium"}, "Gd":{"Row":8,"Column":10,"Atomic Number":64,"Name":"Gadolinium"}, "Tb":{"Row":8,"Column":11,"Atomic Number":65,"Name":"Terbium"}, "Dy":{"Row":8,"Column":12,"Atomic Number":66,"Name":"Dysprosium"}, "Ho":{"Row":8,"Column":13,"Atomic Number":67,"Name":"Holmium"}, "Er":{"Row":8,"Column":14,"Atomic Number":68,"Name":"Erbium"}, "Tm":{"Row":8,"Column":15,"Atomic Number":69,"Name":"Thulium"}, "Yb":{"Row":8,"Column":16,"Atomic Number":70,"Name":"Ytterbium"}, "Lu":{"Row":8,"Column":17,"Atomic Number":71,"Name":"Lutetium"}, "Hf":{"Row":6,"Column":4,"Atomic Number":72,"Name":"Hafnium"}, "Ta":{"Row":6,"Column":5,"Atomic Number":73,"Name":"Tantalum"}, "W":{"Row":6,"Column":6,"Atomic Number":74,"Name":"Wolfram"}, "Re":{"Row":6,"Column":7,"Atomic Number":75,"Name":"Rhenium"}, "Os":{"Row":6,"Column":8,"Atomic Number":76,"Name":"Osmium"}, "Ir":{"Row":6,"Column":9,"Atomic Number":77,"Name":"Iridium"}, "Pt":{"Row":6,"Column":10,"Atomic Number":78,"Name":"Platinum"}, "Au":{"Row":6,"Column":11,"Atomic Number":79,"Name":"Gold"}, "Hg":{"Row":6,"Column":12,"Atomic Number":80,"Name":"Mercury"}, "Tl":{"Row":6,"Column":13,"Atomic Number":81,"Name":"Thallium"}, "Pb":{"Row":6,"Column":14,"Atomic Number":82,"Name":"Lead"}, "Bi":{"Row":6,"Column":15,"Atomic Number":83,"Name":"Bismuth"}, "Po":{"Row":6,"Column":16,"Atomic Number":84,"Name":"Polonium"}, "At":{"Row":6,"Column":17,"Atomic Number":85,"Name":"Astatine"}, "Rn":{"Row":6,"Column":18,"Atomic Number":86,"Name":"Radon"}, "Fr":{"Row":7,"Column":1,"Atomic Number":87,"Name":"Francium"}, "Ra":{"Row":7,"Column":2,"Atomic Number":88,"Name":"Radium"}, "Ac":{"Row":9,"Column":3,"Atomic Number":89,"Name":"Actinium"}, "Th":{"Row":9,"Column":4,"Atomic Number":90,"Name":"Thorium"}, "Pa":{"Row":9,"Column":5,"Atomic Number":91,"Name":"Protactinium"}, "U":{"Row":9,"Column":6,"Atomic Number":92,"Name":"Uranium"}, "Np":{"Row":9,"Column":7,"Atomic Number":93,"Name":"Neptunium"}, "Pu":{"Row":9,"Column":8,"Atomic Number":94,"Name":"Plutonium"}, "Am":{"Row":9,"Column":9,"Atomic Number":95,"Name":"Americium"}, "Cm":{"Row":9,"Column":10,"Atomic Number":96,"Name":"Curium"}, "Bk":{"Row":9,"Column":11,"Atomic Number":97,"Name":"Berkelium"}, "Cf":{"Row":9,"Column":12,"Atomic Number":98,"Name":"Californium"}, "Es":{"Row":9,"Column":13,"Atomic Number":99,"Name":"Einsteinium"}, "Fm":{"Row":9,"Column":14,"Atomic Number":100,"Name":"Fermium"}, "Md":{"Row":9,"Column":15,"Atomic Number":101,"Name":"Mendelevium"}, "No":{"Row":9,"Column":16,"Atomic Number":102,"Name":"Nobelium"}, "Lr":{"Row":9,"Column":17,"Atomic Number":103,"Name":"Lawrencium"}, "Rf":{"Row":7,"Column":4,"Atomic Number":104,"Name":"Rutherfordium"}, "Db":{"Row":7,"Column":5,"Atomic Number":105,"Name":"Dubnium"}, "Sg":{"Row":7,"Column":6,"Atomic Number":106,"Name":"Seaborgium"}, "Bh":{"Row":7,"Column":7,"Atomic Number":107,"Name":"Bohrium"}, "Hs":{"Row":7,"Column":8,"Atomic Number":108,"Name":"Hassium"}, "Mt":{"Row":7,"Column":9,"Atomic Number":109,"Name":"Meitnerium"}, "Ds""":{"Row":7,"Column":10,"Atomic Number":110,"Name":"Darmstadtium"}, "Rg""":{"Row":7,"Column":11,"Atomic Number":111,"Name":"Roentgenium"}, "Cn""":{"Row":7,"Column":12,"Atomic Number":112,"Name":"Copernicium"}, "Uut""":{"Row":7,"Column":13,"Atomic Number":113,"Name":"Ununtrium"}, "Uuq""":{"Row":7,"Column":14,"Atomic Number":114,"Name":"Ununquadium"}, "Uup""":{"Row":7,"Column":15,"Atomic Number":115,"Name":"Ununpentium"}, "Uuh""":{"Row":7,"Column":16,"Atomic Number":116,"Name":"Ununhexium"}, "Uus""":{"Row":7,"Column":17,"Atomic Number":117,"Name":"Ununseptium"}, "Uuo""":{"Row":7,"Column":18,"Atomic Number":118,"Name":"Ununoctium"}}

def first_option():                                 #
    symbol = input("Enter the search element's symbol to view an element's information: ")          #Getting the symbol from the user
    if (symbol in periodic_table_elements):                                                         #If the symbol is in periodic table
        print("The information of " + symbol + " element is:")                                      #Printing the elements info
        print(periodic_table_elements.get(symbol))
    else:                                                                                               #Else printing the element is not present in periodic table
        print("The entered symbol is not available in periodic table. \n")
    choice = input("Enter y, If you want to go back to the main menu")                      #This choice is used to get the user wish of going back to th main menu
    if choice == 'y':
        main_menu()
    else:
        exit()

def second_option():
    property = int(input("Enter the property of the periodic table: \n 1. Row \n 2. Column \n 3. Atomic Number \n 4. Name \n"))         #Getting the property name from the user
    if property == 1:                                                           #If property is 1 that is Row
        for symbol, element_info in periodic_table_elements.items():                #Iterates through the periodic table
            print("\nSymbol:", symbol)                                          #Printing the Symbols
            for key in element_info:                                            #Now Iterating through the nested dictionary
                if key == "Row":                                                #If the key value in the nested dictionary is Row
                    print(key + ':', element_info[key])                         #Printing the corresponding row value to the Element

    elif property == 2:                                                         #If property is 2 that is Column
        for symbol, element_info in periodic_table_elements.items():                #Iterates through the periodic table
            print("\nSymbol:", symbol)                                          #Printing the Symbols
            for key in element_info:                                            #Now Iterating through the nested dictionary
                if key == "Column":                                             #If the key value in the nested dictionary is Column
                    print(key + ':', element_info[key])                         #Printing the corresponding Column value to the Element

    elif property == 3:                                                         #If property is 3 that is Atomic Number
        for symbol, element_info in periodic_table_elements.items():                #Iterates through the periodic table
            print("\nSymbol:", symbol)                                          #Printing the Symbols
            for key in element_info:                                            #Now Iterating through the nested dictionary
                if key == "Atomic Number":                                      #If the key value in the nested dictionary is Atomic Number
                    print(key + ':', element_info[key])                         #Printing the corresponding Atomic Number the Element

    elif property == 4:                                                         #If property is 4 that is Name
        for symbol, element_info in periodic_table_elements.items():                #Iterates through the periodic table
            print("\nSymbol:", symbol)                                          #Printing the Symbols
            for key in element_info:                                            #Now Iterating through the nested dictionary
                if key == "Name":                                               #If the key value in the nested dictionary is Name
                    print(key + ':', element_info[key])                         #Printing the corresponding Name the Element
    else:
        print("Not available. Try again.")                                      #If the property is not available for the element
    choice = input("If you want to go back to the main menu")                   #This choice is used to get the user wish of going back to th main menu
    if choice == 'y':
        main_menu()
    else:
        exit()

def third_option():
    add_symbol = input("Enter the Symbol for the element: ")                            #Getting the new element's symbol to add to the periodic table dictionary
    add_row = int(input("Enter the Row number for the element: "))                      #Getting the new element's row to add to the periodic table dictionary
    add_column = int(input("Enter the Column number for the element: "))                #Getting the new element's Column to add to the periodic table dictionary
    add_number = int(input("Enter the Atomic Number for the element: "))                #Getting the new element's Automic Number to add to the periodic table dictionary
    add_name = input("Enter the Name for the element: ")                                ##Getting the new element's Name to add to the periodic table dictionary

    if (add_symbol in periodic_table_elements):
        print("As element already exits updating it properties")
        periodic_table_elements[add_symbol] = {"Row": add_row, "Column": add_column, "Atomic Number": add_number, "Name": add_name}         #If the element already exists updating the properties of the element
    else:
        periodic_table_elements[add_symbol] = {"Row": add_row, "Column": add_column, "Atomic Number": add_number, "Name": add_name}         #If it is a new element adding it to the dictionary
    print(periodic_table_elements)
    choice = input("Enter y If you want to go back to the main menu")                                                                       #This choice is used to get the user wish of going back to th main menu
    if choice == 'y':
        main_menu()
    else:
        exit()

def fourth_option():
    Update_element = input("Type the symbol of the element you would like to change: ")                                                     #Getting the symbol which needds to updated
    Update_property = int(input("Type the property you would like to change: \n 1. Row \n 2. Column \n 3. Atomic Number \n 4. Name \n "))      #Getting the property name which needs to be updated
    if Update_property == 1:
        Update_Row = input("Enter the new row for the element: ")
        periodic_table_elements[Update_element]["Row"] = Update_Row                         #Updating the row value of the element
        print("Element details after update :", periodic_table_elements[Update_element])
    elif Update_property == 2:
        Update_Column = int(input("Enter the new column for the element: "))
        periodic_table_elements[Update_element]["Column"] = Update_Column                   #Updating the column value of the element
        print("Element details after update :", periodic_table_elements[Update_element])
    elif Update_property == 3:
        Update_Automic_Number = int(input("Enter the new automic number for the element: "))
        periodic_table_elements[Update_element]["Automic Number"] = Update_Automic_Number       #Updating the automic number value of the element
        print("Element details after update :", periodic_table_elements[Update_element])
    elif Update_property == 4:
        Update_Name = int(input("Type a new column number: "))
        periodic_table_elements[Update_element]["Automic Number"] = Update_Name                 #Updating the name of the element
        print("Element details after update :", periodic_table_elements[Update_element])
    else:
        print("The entered symbol is not available in periodic table.")                     #Prints If the element doesn't exist in the periodic table
    choice = input("If you want to go back to the main menu")                           #Choice of going back to th main menu
    if choice == 'y':
        main_menu()
    else:
        exit()

def fifth_option():
    jason_file = json.dumps(periodic_table_elements)                                #Creating variable named jason_file and dumping the dictionary into it
    with open('dict.json', 'w') as fp:                              #Opening a file named "dict.jason" in write mode as fp
        json.dump(jason_file, fp)                                                   #Writing from jason_file to fp
    fp.close()                                                                  #Closing the fp
    choice = input("If you want to go back to the main menu")                   #Choice to go back to the main menu
    if choice == 'y':
        main_menu()
    else:
        exit()
def sixth_option():
    file_name = input("Enter the name of the file with .jason extension: ")         #Getting the json file name from which we need to retrive
    file = open(file_name, "r")                                                     #Opening the file in read mode
    periodic_table = eval(file.read())                                              #Now storing the info retrived from the file to the periodic_table
    print(periodic_table)                                                           #Printing the periodic table
    file.close()                                                                     #Closing the file
    choice = input("If you want to go back to the main menu")                       #Choice to back to the main menu
    if choice == 'y':
        main_menu()
    else:
        exit()


def user_choice(choice):                    # User choice of menu selection using switch choice

        if choice == 1:
            first_option()
        elif choice == 2:
            second_option()
        elif choice == 3:
            third_option()
        elif choice == 4:
            fourth_option()
        elif choice == 5:
            fifth_option()
        elif choice == 6:
            sixth_option()
        elif choice == 7:
            exit()
        else:
            return "Invalid Input"
def main_menu():                                                        #Main menu to navigate between the user choices or operations
    print("1. Search the element by symbol (see all the details)")
    print("2. Search by a property (name, number, row, column) and see the values for that property for all the elements in the table")
    print("3. Enter a new element manually (type the information for each property)")
    print("4. Change the properties of an element (by symbol)")
    print("5. Export periodic table as a JSON file")
    print("6. Load periodic table from JSON file")
    print("7. Exit the program")
    choice = int(input("Enter the Choice\n"))
    user_choice(choice)                             #Calling the user_choice function with choice parameter.

main_menu()                 #Callling the main menu
