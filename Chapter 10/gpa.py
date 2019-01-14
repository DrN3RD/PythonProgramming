#gpa.py

class Student:
    def __init__(self,name,hours,qpoints):

        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):

        return self.name

    def getHours(self):

        return self.hours

    def getQpoints(self):

        return self.qpoints

    def gpa(self):

        return self.qpoints/self.hours
