import operation

#when the program runs this function is executed firstly to ask user to choose the desried option
def Data_display( ):#Data_display function
    Data_contents = True
    while Data_contents:
        print()
        print("Select one of the options")
        print("1)", "--->", "Press 1 to rent a custome.")
        print("2)", "--->", "Press 2 to return a custome.")
        print("3)", "--->", "Press 3 to exit.")
        print()
        
        variable = input("Enter a number: ")
        
        if variable == "1":
            print()
            print("Let's rent a costume.")
            operation.costumerent()
            
        elif variable == "2":
            print()
            print("\t\t\t\t Lets return a costume:")
            operation.costume_returned()
        elif variable == "3":
            print()
            print("---------------------------------------------------------------------------")
            print("Thank you for using our application!")
            print("---------------------------------------------------------------------------")
            break
            Data_contents = False
        

        else:
            print()
            print("-------------------------------------------------------------------------------")
            print("\t\tinput is not valid")
            print("-------------------------------------------------------------------------------")
            print()




print()
print("-------------------------------------------------1------------------------------")
print("\t\t\tWelcome To Our Costume Retal Store")
print("-------------------------------------------------------------------------------")



Data_display() #calling the function
