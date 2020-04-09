from random import choice
from string import ascii_letters

user =[]

#  create a function for user detail and create a container for details..
def user_detail ():

    firstname= input("Enter Firstname: ")
    lastname = input("Enter lastname: ")
    email =input("Enter email: ")
    password = f' { firstname[:2] }{lastname[-2:] }{"".join(choice(ascii_letters) for x in range(5))}'
    print ("Your password is: ", password)
    
    details= {
         "firstname": firstname,
         "lastname":  lastname,
         "email":   email,
         
     }

#Printing out password

    feedback = input("Are you satisfied with password?, enter yes / no:  ")

    while True:

        if feedback.lower()=="yes":
            details["password"] = password
            print("Thank you for registering!")
            break
            
        elif feedback.lower()=="no":
            new=input("Enter desired password: ")

            while True:

                if len(new )<7or len(new) >9:
                    new= input("Password must be between 7 and 9 characters: ")

                else:
                    password= new
                    print("Your password is: ", password)
                    details ["password"]= password

                    break
            break
        else:
            feedback = input("Are you satisfied with password?, enter yes / no:  ")
    user.append(details)
    new_user()
    
# Define a function to contain detalis of multiple user
def new_user():
    users = input("Are you a new user?  yes or no: ")

    while True:
        if users=="yes":
            return user_detail()

        elif users.lower()=="no" and user==[]:
            print("oops no record")
            break

        elif users.lower()=="no" and user!=[]:
            for i in user:
                print(f"Welcome {i['firstname']}{i['lastname']}, your email address is {i['email']} and your password is {i['password']}")
            break

        else:
            new_user()
           
         
        
new_user()