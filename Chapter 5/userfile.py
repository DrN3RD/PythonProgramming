#userfile.py

#Program to create a file of usernames in batch mode
from tkinter.filedialog import *

def main():

    print("This program creates a file of usernames from a file of names")

    #Get the file names

    infileName = askopenfilename()

    outfileName = asksaveasfilename()

    #Open the files

    infile = open(infileName,"r")
    outfile = open(outfileName,"w")

    #Process each line of the input file

    for line in infile:
        #Get first and last names from line
        first,last = line.split()

        #create username

        uname= (first[0]+last[:7]).lower

    #write it to output file
        print(uname, file = outfile)
    infile.close()
    outfile.close()

    print("usernames saved in file called",outfileName)
main()