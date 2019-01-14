#A program to convert textual message into a sequence.


def main():
    print("This program converts a textual message into a sequence")

    message = input("Please enter the message to encode: ")
    print("\n Here are the Unicode codes")

    for i in message:
        print(ord(i), end=" ")

    print()

    input()

main()