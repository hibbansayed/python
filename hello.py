#ask the user to input their username and password twice.if the password is less than 8 characters or 
# does not match, ask the user to re-enter their username and passwords. 

username = input("Enter Your Username: ")
password = input("Enter your password(must be 8 characters long): ")
pass_comfirmation = input("Comfirm your Password : ")


if len(password) < 8 :
    print("password must be 8 characters long")
elif pass_comfirmation < password: 
        print("password does not match")
else:
    print("An Account has been made")    


