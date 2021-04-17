import datetime
 
now = datetime.datetime.now()
 
def init():
    
    print('Welcome to Big Bank')
 
        
    haveAccount = int(input("Do you have an account with us: 1 (yes) 2 (no) \n"))
        
    if(haveAccount == 1):
       
        login()
    elif(haveAccount == 2):
        
        print(register())
    else:
        print('you have selected invalid option')
        init()
    
 
import datetime
 
now = datetime.datetime.now()
 
 
 
def login():
    name = input ("What is your name? \n")

    allowedUsers = ['jah','ike','jim']

    allowedPassword = ['jahjah','ikeike','jimjim']
    
    if name in allowedUsers:
    
        password = input ("What is your password? \n")
    
        userId = allowedUsers.index(name)
    
        if(password == allowedPassword[userId]):
            bankOperation()
 
def bankOperation():
 
    print('Welcome %s' % name)
 
    print ("Current date and time: ")
 
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
    
    selectedOption = input("What would you like to do? (1) Deposit (2) Withdraw (3) Logout (4) Exit \n")
 
    if(selectedOption == 1):
        
        depositOperation()
    elif(selectedOption == 2):
        
        withdrawalOperation()
    elif(selectedOption == 3):
       
        login()
    elif(selectedOption == 4):
        
        exit()
    else: 
        print ('Invalid Option')
        bankOperation()
 
def register():
    print("***** Register *****")
    email = input('What is your email address? \n')
    first_name = input('What is your first name? \n')
    last_name = input('What is your last name? \n')
    password = input('Please create a password \n')
 
    accountNumber = generateAccountNumber()
 
    database[accountNumber] = [first_name, last_name, email, password]
 
    print('Your Account Has Been Created')
    print('== === === === ==')
    print('Your account number is: %d' % accountNumber)
    print('Make Sure To Keep It Safe')
    print('== === === === ==')
    
    login()
 
def withdrawalOperation():
    print ('1. How much cash would you like?')

    print ('2. Press 0 to Return to Main Menu')

    value = input ('Please Choose: \n')

    value = int(value)

    if value > 0:
        print('Please Take Your Cash')
        
    else:
        print('Invalid Selection')
        withdrawalOperation()

def depositOperation():
    print ('1. How much cash would you like to deposit?')
    print ('2. Press 0 to Return to Main Menu')

    value1 = input ('Please Choose: \n')

    value1 = int(value1)

    if(value1 > 0):
        print('Please enter your cash into the machine')
    else: 
        print('Invalid Amount')
        depositOperation()

        
def complaintOperation():
    print ('1. What is your complaint?')

    print ('2. Press F to Return to Main Menu')

    value2 = input ('Please Choose: \n')

    if(value2 == ""):

        print('Thank you for contacting us')

    elif(value2 == F):
        bankOperation()


def generateAccountNumber():
    return random.randrange(1111111111,9999999999)
 
 
