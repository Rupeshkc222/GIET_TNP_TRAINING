### A University wants to automate their admission process. Students are admitted based on marks according to a qualifying exams.

# A Student is identified by studentid, age and marks in qualifying exam
#
# Data is valid, if:
#   * Age is greater than 20
#   * Marks is between 0 and 100
#
# A Student qualifies for the admission if:
#   * Age and Marks are Valid
#   * Marks is greater than 65
#
# Rules to Follow:
# Class Name: Student
# -- Attributes: (private)
#    * student_id
#    * marks
#    * age
#
# Methods:
# (public)
# * init()
# * validate_marks()
# * validate_age()
# * check_qualification()

class data:
    def _init_(self):
        self.__ID = None
        self.__age = None
        self.__marks = None
        self.__cal = None

    def setID(self, ID):
        self.__ID = ID

    def setage(self, age):
        self.__age = age

    def setmarks(self, marks):
        self.__marks = marks

    def calculate(self):
        if self.getage() > 20 and self.getmarks() > 0 and self.getmarks() < 100:
            if (self.getmarks()>=85):
                a=self.getmarks()-self.getmarks()*0.25
                print(self.getID(),a)
            elif (self.getmarks() > 65):
                print("Eligible for Admission")
            else:
                print("Not Eligible")
        else:
            print("Not eligible")

    def getID(self):
        return self.__ID

    def getage(self):
        return self.__age

    def getmarks(self):
        return self.__marks


obj = data()
obj.setID(1991)
obj.setage(21)
obj.setmarks(95)
obj.calculate()