def main():

    inString = input("Please input the unicode message")

    message = ""

    for j in inString.split():
        codeNum = int(j)
        message = message + chr(codeNum)

