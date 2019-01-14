#Username.py

#simple program that processes a users name, and creates a username form it

def main():
    print("This Program generates computer usernames. \n")

    #Get the first and last names

    first = input("Please enter your first name: \n")
    last = input(" Please enter your last name : \n")

    uname = first[0] + last[:7]

    print(" Your username is ", uname)

    input("Press to quit")

main()