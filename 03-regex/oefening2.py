#password 8 char, one upper, one lower, one digit 

def main():

    username = input("USername:  ")
    password = input("Password: ")

    result= bool(re.match("(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}", password))

    if result:
             print ("Succesfully registered")
    else: 
            print ("8 chars, 1 upp, 1 low, 1 digit")

main()