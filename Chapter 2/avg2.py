#A simple program that will average scores of an exam
#This is to illustrate the use of multiple input, simultaneous eval

def main():
    print("This program computes the average of two exam scores.")
    score_1, score_2 = eval(input("Enter two exam scores separated by a comma: "))
    average = (score_1+score_2)/2
    print("Your average is", average)
main()