#---->  Create empty dictionary  <----

dictionary= {'fly': 'animal'}

print("Dictionary")

while(True):
    print("\n1 - Add new definition.")
    print("2 - Search for existing definition.")
    print("3 - Show available definitions.")
    print("4 - Delete selected definitions.")
    print("5 - Shutdown the program.\n")

    choise =input("Type in your option")

    if (choise == "1"):
        print("Add new word to our dictionary.\n")
        key = input("Add a key(word) to define:")
        definition = input("\nType in definition:")
        dictionary[key] = definition
        print("Word and definition added succesfully .\n")


    elif (choise == "2"):
        key = input("Type in word:")
        if key in dictionary:
            print("The definition of :", key,":", dictionary[key], "\n")
        else:
            print('Chosen word does not exist.\n')

    elif (choise == "3"):

        print(dictionary)


    elif (choise == "4"):
        key = input("\nWhat word would you want to delete?")
        if key in dictionary:
            del dictionary[key]
            print("Word", key, "has been deleted.")
        else:
            print("Chosen word does not exist.\n")


    elif (choise == "5"):
        print("\nThanks for activity.\nClosing...")
        break
    else:
        print("\nWrong option!!\n")

