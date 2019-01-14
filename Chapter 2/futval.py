#Future Value
#This program calculates the value increase of an interested sum of money
#User input gives both interest rates, and future value

print("This program will calculate the resulting value of an investment."
      "Calculation is  based on amount invested, i.e the principal, and"
      "the apr, Annual Percentage Rate ")

def main():
    principal= eval(input("Input the principal of the investment:"))

    apr = eval(input("Input the annual percentage rate in decimal form: "))

    reinvest = eval(input("Specify how much extra cash you will add to the account each year:"))

    for i in range(10):
        principal = principal*(1+apr)
        print("calculating year", i+1)
        principal = principal + reinvest
        print("New value of investment", principal)
    print("The value of the investment after 10 years is:  ", principal)

main()