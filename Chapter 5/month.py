#monthy.py
#This program returns the month when asked for


def main():
    print("Chose a month based on its numerical value ")

    month = "JanFebMarAprMayJunJulAugSepOctNovDec"

    n = int(input("Enter the month number you want to know: "))


    #Compute starting pos

    pos = (n-1)*3

    monthAbbrev = month[pos:pos+3]

    print("The month requested is : ", monthAbbrev + ".")
    input()

main()
