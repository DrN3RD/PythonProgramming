#Month2.py
#Program uses a list to retrieve month abbreviation


def main():
    #Months is a list used as a lookup table

    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]


    n = int(input("Enter month number: \n"))

    print("The Month requested is : ", months[n-1])

    input()

main()