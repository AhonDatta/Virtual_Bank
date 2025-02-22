import random 

class data() :
    
    global name
    global uid
    global balance
    global n
    global u
    

    name = ["Ahon"]
    uid = [2008]
    balance = [0]
    
    q = input("Do you have a account ? (Y/N) :   ")
    if ( q == "Y"):
        n = input("Enter your first name :  ")
        u = input("Enter your 4 digit uid  ")
        print("Your account has been created and signed in...")
        
    elif (q == "N"):
        n = input("Enter your first name :  ")
        u = int(random.randint(1111,9999))
        print("Your new uid is ", u)
        name.append(n)
        uid.append(u)
        balance.append(0)
        print("You have successfully logged in...")
    else :
        print("Sorry !")
        print("You have to enter only 'Y' or 'N' ")

    

        

    
    
    
    


    