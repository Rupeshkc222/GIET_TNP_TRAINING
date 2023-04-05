'''Softsytems Ltd is a private firm that provides software solutions to its customers.
The management wants to calculate salary for the employees. There are two types of employees namely graduates
who are in probation period and laterals who are experienced joiners in the company.
Write a python program based on the class diagram given below.

RULES TO FOLLOW
===================
Class Description:
Employee class:
validate_basic_salary(): Basic salary of an employee is always more than 3000
If basic salary is valid, return true. Else return false
validate_qualification(): Employee should posses either a "Bachelors" or "Masters" degree
If qualification is valid, return true. Else return false
Graduate class:
validate_job_band(): Graduates can be in "A", "B" or "C" job band
If job band is valid, return true. Else return false
calculate_gross_salary(): Calculate gross salary
Validate basic salary, qualification and job band
If valid,
Compute gross salary as basic salary + PF+ TPI amount + incentive
    PF is 12% of basic salary
    Identify TPI amount based on cgpa
    Identify incentive based on job band. Incentive should be applied on basic
    salary (Refer tables given)
Return gross salary
Else return -1
Job Band	A	B	C	D	E	F
Incentive %	4	6	10	13	16	20

CGPA	4 to 4.25	4.26 to 4.5	    4.51 to 4.75	4.76 to 5
TPI Amount	1000	1700	        3200	            5000
Lateral class:
validate_job_band(): Laterals can be in "D", "E" or "F" job band
If job band is valid, return true. Else return false
calculate_gross_salary(): Calculate gross salary
Validate basic salary, qualification and job band
If valid,
Compute gross salary as basic salary + PF + SME bonus + incentive
    PF is 12% of basic salary
    Identify SME bonus based on skill set
    Identify incentive based on job band. Incentive should be applied on basic salary (Refer
    tables given)
Return gross salary
Skill Set	SME Bonus
AGP	        6500
AGPT	    8200
AGDEV	    11500
Else return -1
Perform case sensitive string comparison.
For testing:
Create objects of Graduate and Lateral classes
Invoke calculate_gross_salary() on Graduate and Lateral objects
Display the details'''


class Employee:
    def __init__(self,id, amount, degree):
        self.id=id
        self.amount = amount
        self.degree = degree

    def validate_basic_salary(self):
        if self.amount >= 3000:
            return True
        else:
            return False

    def validate_qualification(self):
        if self.degree == "Masters" or self.degree == "Bachelors":
            return True
        else:
            return False
class Graduate(Employee):
    def __init__(self,id,amount,degree, band,cgpa):
        super().__init__(id,amount,degree)
        self.band = band
        self.cgpa=cgpa

    def validate_job_band(self):
        if self.band == 'A' or self.band == 'B' or self.band == 'C':
            return True
        else:
            return False

    def calculate_gross_salary(self):
        if self.validate_basic_salary() and self.validate_qualification() and self.validate_job_band():
            pf = self.amount * 0.12
            if self.cgpa >= 4 and self.cgpa <= 4.25:
                tpi_amount = 1000
            elif self.cgpa > 4.25 and self.cgpa <= 4.5:
                tpi_amount = 1700
            elif self.cgpa > 4.5 and self.cgpa <= 4.75:
                tpi_amount = 3200
            else:
                tpi_amount = 5000
            if self.band == "A":
                incentive = self.amount * 0.04
            elif self.band == "B":
                incentive = self.amount * 0.06
            else:
                incentive = self.amount * 0.1
            gross_salary = self.amount + pf + tpi_amount + incentive
            return gross_salary
        else:
            return -1

    def printthis(self):
        print("id",self.id)
        print("qualification",self.validate_qualification())
        print("band",self.band)
        print("gross salary",self.calculate_gross_salary())

class Lateral(Employee):
    def __init__(self, id,amount,degree,skill_set, job_band):
        super().__init__(id, amount,degree)
        self.skill_set = skill_set
        self.job_band = job_band

    def validate_job_band(self):
        if self.job_band == "D" or self.job_band == "E" or self.job_band == "F":
            return True
        else:
            return False

    def calculate_gross_salary(self):
        if self.validate_basic_salary()  and self.validate_qualification() and self.validate_job_band():
            pf = 0.12 * self.amount

            if self.skill_set == "AGP":
                sme_bonus = 6500
            elif self.skill_set == "AGPT":
                sme_bonus = 8200
            elif self.skill_set=="AGDEV":
                sme_bonus = 11500
            else:
                sme_bonus=0
            if self.job_band == "D":
                incentive = 0.13 * self.amount
            elif self.job_band == "E":
                incentive = 0.16 * self.amount
            else:
                incentive = 0.2 * self.amount
            gross_salary = self.amount + pf + sme_bonus + incentive
            return gross_salary
        else:
            return -1

print("for graduation====")
g=Graduate('1',45000,"Masters",'A',4.14)
g.printthis()
l=Lateral('1',45000,'Masters','AGPT','D')
gross_salary = l.calculate_gross_salary()
print()
print("for lateral class emplyoee====")
if gross_salary==-1:
    print("not valid")
else:
    print("id",l.id)
    print("gross salary",gross_salary)
