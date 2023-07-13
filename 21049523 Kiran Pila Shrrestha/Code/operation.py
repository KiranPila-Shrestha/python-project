import datetime


'''

yo function le file read garxa where costumes.txt contains all costumes available for renting purpose
'''
def get_file_content(): #reading file contents fuction
    file = open("costumes.txt", "r")
    data = file.readlines()
    file.close()
    return data


'''
making a dictionary and storing values and splliting it
'''

def dictionary(filecontent):# creating dictionary function
    dataindictionary = { } #empty list for making 2D lisy
    for index in range(len(filecontent)):
        dataindictionary[index+1] = filecontent[index].replace("\n", "").split(",");
#index + 1 means start from 1
    return dataindictionary



'''

this function is used to print all the costumes that are available
this function also makes heading for each costume name brand etc and align the items in a table form

'''
def costumes_available(costumedata): 
   
    print("----------------------------------------------------------------------------------------------")
    print()
    print("S.No",  "\t", "Costume Name", "\t", "Brand", "\t\t", "Price",  "Quantity")
    print()
    print("----------------------------------------------------------------------------------------------")
    for key, value in costumedata.items(): # list element of tesxt file
        print()
        print(key, "\t", value[0], "\t", value[1], "\t", value[2], "\t\t", value[3])
        print()
    return ""


'''
when user inputs serial number then if its invalid according to if statement then it shows error
'''
def valid_sno(costumedata): # valid intex i.e s.no
    Valid_Data = False
    while Valid_Data== False:
        print()
        '''
            try except is used to handle exception
        '''
        
        try:
            
            Sign = int(input("Enter the serial number: "))
             
            if Sign > 0 and Sign <= len(costumedata):
                
                quantity_num = int(costumedata[Sign][3])

                if quantity_num == 0:
                    print("Costume is out of stock")
                    Valid_Data = True
                    costumes_available(costumedata)
                    
                else:
                    Valid_Data = True
                    print("The costume is available")
                    return Sign
                
            else:
                
                print("Please provid valid serial number.")
                        
                 
        except:
            print()
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("\t\tInvalid serial number !!!!!!, Please re-enter the serial number.........")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
       

'''

when user inputs quantity while renting a costume and if its invalid it displays message accordingly
also when the costume is rented successfuly then the amount of quantity in table is decreasted
with rented costume quantity
'''

def quantity_is_valid(costumedata, Sign): # checking valid quantity of dictionary file

    continueLoop = False

    while continueLoop == False:
        try:
            print()
            quantity_num = int(input("Enter total number of costume you want: "))

            if quantity_num > 0  and quantity_num <= int(costumedata[Sign][3]):

                continueLoop = True
                
                costumedata[Sign][3] = str(int(costumedata[Sign][3]) - quantity_num) #decrease gareko
                print("Costume is rented")
                return quantity_num
            
            elif quantity_num > int(costumedata[Sign][3]):
                print("Quantity we have entered is greater than what we have in our stock !!!")
                
            else:
                print("Invalid input")
                
        except:
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Invalid input. please enter valid input")

'''
creating a function to ask user if they want to rent another costume or not
'''

'''

this fucntion is made to generate a bill
when user returnes or rents a costume this function is executed
in parameter there is cart name costumedata which is dictionary content and rentdays which is
for return process
'''
def bill_generate(cart, costumedata, rentdays, INVOICE):
    print()
    
    Date = Rent_Date()
    Time = Rent_Time()
    
    Name = input("Enter the name of customer :")
    Phone = input("Enter the contact number of customer: ")
    
    Grand_total = 0
    Total_Quant = 0
    fine = 0 #fine means penalty when the day exceeds this fine is generated
    
    print()
    print("***********************************************************************************")
    print(f"\t\t{INVOICE} INVOICE")
    print("***********************************************************************************")
    print()
    print("Customer Name :" + Name)
    print("Customer contact number :" + Phone)
    print(f"Date of {INVOICE.lower()}: " + Date + "\n")
    print()
    print(f"Date of {INVOICE.lower()}: " + Time + "\n")
    print()
    print("____________________________________________________________________________________________________________________________")
    print()
    print("\nS.no", "\t", "Custome Name", "\t", "Brand" ,"\t\t", "Price",  "Quantity")
    print()
    print("______________________________________________________________________________________________________________________________")


    for j in range(len(cart)):
        
        Sign = int(cart [ j ] [0])

        quantity_num = cart [ j ] [1]

        dress_name = costumedata[Sign] [0]
        
        Brand = costumedata[Sign][1]

        Price = float(costumedata [Sign] [2])

        
        Grand_total += (quantity_num * Price)
        Total_Quant += quantity_num


        print((j + 1), "\t", dress_name, "\t", Brand, "\t", Price, "\t", quantity_num)
        
        print("_____________________________________________________________________________________________________________________________________")
        print("\n")
    #fine generate
    if rentdays > 5:
        fine += ((rentdays - 5) * 5)

    if INVOICE.lower() == "RETURN":
        print("Total Fine: " + "$" + str(float(fine)))

    else:
        print("Total price: " + "$" + str(Grand_total))
    print("Total Fine: " + "$" + str(float(fine)))
    #this function is called after bill is generated and this function wll also create a textfile acoordingly
    generate_txt_bill(Name, Phone, Grand_total, Total_Quant, cart, costumedata, fine, INVOICE)
    




# making all the detail of rent to text file.
'''
this function creates a textfile for each transaction
'''
def generate_txt_bill(Name, Phone, Grand_total, Total_Quant, cart, costumedata, fine, INVOICE):

    Date = Rent_Date()
    Time = Rent_Time()
    
    file = open(Name + "-" + Date + Time + ".txt","w")
    file.write(f"** {INVOICE} INVOICE **\n")
    
    file.write("Customer Name :"+Name + "\n")
    file.write("Costumer contact number :"+Phone+"\n")
    file.write(f"Date of {INVOICE.lower()}: " + Date + "\n")
    file.write(f"Date of {INVOICE.lower()}: " + Time + "\n")
    
    
    file.write("\n")
    file.write("\n""---------------------------------------------------------------------------------------------------------------------------------------------------\n")
    file.write("\n""S.no" + "\t"+ "Costumer" + "\t" + "Brand" + "\t" "\t"+ "Price" + "\t\t"+ "Quantity" + "\n")
    file.write("\n""---------------------------------------------------------------------------------------------------------------------------------------------------\n")

    for j in range(len(cart)):
        
        Sign = int(cart [ j ] [0])

        quantity_num = cart [ j ] [1]

        dress_name = costumedata[Sign] [0]
    
        Brand = costumedata[Sign][1]

        Price = (costumedata [Sign] [2])
        

        file.write(str((j+1)) + "-" + "\t" + dress_name + "\t" + Brand + "\t" + Price + "\t" + str(quantity_num) + "\n" "\n")

    if INVOICE.lower() == "RETURN":
        file.write("Total Fine: " + "$" + str(float(fine)) + "\n")

    else:
        file.write("Total price: " + "$" + str(Grand_total) + "\n")
        
    file.write("Total quantity: " + str(Total_Quant) + "\n")
    file.write("Total Fine: " + str(float(fine)) + "\n")
    file.close()

#function for renting date n time.

def Rent_Date():
      year = str(datetime.datetime.now().year)
      month = str(datetime.datetime.now().month)
      Day = str(datetime.datetime.now().day)

      Date = str(year+"-"+month+"-"+Day)
      return Date
 

def Rent_Time():
    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
    time = str(hour+"-"+minute+"-"+second)
    return time



'''
quanitty  0 xa ki nai check garxa

'''

def zero_quantity(costumedata):
    
    Total_Quant = 0 # initially quantity is zero

    for Sign in range(len(costumedata)):
        Sign = Sign + 1

        Total_Quant += int(costumedata[Sign] [3])

    return Total_Quant


'''
this function updates the file that we are working with
after completion of transaction ths function is executed
'''
def fileUpdate(costumedata):
    file = open("costumes.txt", "w")
    for value in costumedata.values():
        newdata = value[0] + "," + value[1] + "," + value[2] + "," + value[3] + "\n"
        file.write(newdata)
    file.close()




####
#return process
####

'''

checks if sno number is valid or not while returnign a costume
'''
def sno_valid_return(costumedata):
    
    Valid_Data = False
    while Valid_Data== False:
        print()
        
        try:
            
            Sign = int(input("Enter the serial number: "))
             
            if Sign > 0 and Sign <= len(costumedata):

                Valid_Data = True
                print()
                return Sign
                
            else:
                print("==========================")
                print("\t\tInvalid input")
                print("===========================")
                 
        except:
            print()
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("\t\t\tInput not valid. Please re_enter data.")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    

'''

this function checks if the quantity is valid or not while returning a costume
'''
def quantity_valid_return(costumedata, Sign):

    continueLoop = False

    while continueLoop == False:
        try:
            print()
            quantity_num = int(input("Enter total number of costume you want to return: "))

            if quantity_num > 0:

                costumedata[Sign][3] = str(int(costumedata[Sign][3]) + quantity_num)

                return quantity_num
            
            else:
                print("Invalid input")
                
        except:
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Invalid input. please enter valid input")


'''
this function asks the number of renting days to the user
this funciton has try except too when user inputs not existing value message is displayed
'''
def number_days():
    continueLoop = True

    while continueLoop == True:
        try:
            days = int(input("Enter number of renting days?: "))

            if days > 0:
                return days

            else:
                print("Input is not valid")

        except:
            print("Invalid input")


'''

this funciton has feature of appending data in a list
double_costume means when the user rents or returnes same costume twice then
the same costume quantity is added with each other

'''
def double_costumes(cart, Sign, Total_Quant):

    double = False
    for returned in cart:
        if returned [0] == Sign:
            returned [1] += Total_Quant
            double = True
    if double == False:
        cart.append([Sign, Total_Quant])



'''

this function works with returning of costume
when the user enteres value "2" in the data display then this fucntion is executed
all the function needed while reutrning a costume is explained in this function.
'''
def costume_returned():

    cart = [ ]
    continueLoop = True

    while continueLoop == True:
        costumes_available(costumedata)
            
        Sign = sno_valid_return(costumedata)

            
        Total_Quant = quantity_valid_return(costumedata, Sign)

        fileUpdate(costumedata)

        double_costumes(cart, Sign, Total_Quant)

        multiple = True
        
        while multiple == True:
            print()
            user_input = input("Return another costume? ")
            print()
            INVOICE = "RETURN"
            
            if user_input == "no":
                
                rentdays = number_days()
                
                bill_generate(cart, costumedata, rentdays, INVOICE)

                cart.clear()

                multiple = False
                continueLoop = False
                
            elif user_input == "yes":
                multiple = False

            else:
                print("input is not valid")

                
    


####
#return end
####

'''

this funciton is while renting a costume, when the user clicks "!" in the data display then this fucntion
is executed.
all the function that are needed while renting the costume is explained in this function
'''
def costumerent(): #costume rent garna ko lagi banako function
    continueloop = True
    cart = [ ]

    while continueloop == True:
        
        Quantity = zero_quantity(costumedata)
        INVOICE = "RENT"
        if Quantity == 0:
            if len(cart) == 0:
                print("we are out of stock")
                print()
                break
            else:
                print()
                print("Sorry we are out of stock")
                rentdays = 0
                bill_generate(cart, costumedata, rentdays, INVOICE, 0)
                cart.clear()
    
            continueLoop = False
      
        else:
            
            costumes_available(costumedata)
            
            Sign = valid_sno(costumedata)

            
            Total_Quant = quantity_is_valid(costumedata, Sign)
            
            double_costumes(cart, Sign, Total_Quant)
            
            print()
            #cart.append([Sign, Total_Quant])

            fileUpdate(costumedata)

            
            loop = True
            while loop == True:

                input_user = input("Please enter yes if you want to rent another costume else please enter no: ")
                print()
                
                if input_user.lower() == "yes":
                    loop = False
                    
                elif input_user.lower() == "no":
                    rentdays = 0
                    bill_generate(cart, costumedata, rentdays, INVOICE)
                    
                    cart.clear()
                    
                    loop = False
                    continueloop = False
                    
                    
                else:
                    print("input is  not valid")
                   


filecontent = get_file_content() #reads the content of the file

costumedata = dictionary(filecontent) 
