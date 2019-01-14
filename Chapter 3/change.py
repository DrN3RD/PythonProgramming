#Program to calculate the value of some change in dollars

def main():
    print("Change Counters")
    print()
    print("Please enter the count of each coin type.")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickles: "))
    pennies = int(input("pennies: "))
    total = quarters *0.25 + dimes * 0.1 + nickles*0.05 +pennies*0.01
    print()
    print("The total value of your change is", total)

main()