'''
 Ask for:
     Employee Name
     Social Security Number
     Percentage of Salary Contributed to Retirement
     Annual Salary 
 for UP TO 5 LOCAL TRAINERS

  >IF user enters retirement # outside of normal range (0% to 40%):
    Give the user a second chance to input appropraite number

 Display the relevant info on-screen. Including:
    After-retirement-reduction salary for each of the 3 people and total the salary
    Retirement contributions
    After-retirement-reduction salary

 Each line begins with Employee Code (Last Name and Last 4 digits of SSN)
 Display totals for the:
     Salary
     Retirement
     Net Salary

 At the bottom, note the Person with the highest salary
     If statement and 2 variables: maxSalary and maxName
'''

# Get employee name from user
def getName():
    empName = input("Employee "+ str(i) + ": What is the employee's name? ")

# Get social security number from user
def getSSN():
    SSNum = input("Employee "+ str(i) + ": What is the social security number? ")
    while len(SSNum) != 9:
        print("The social security number must be nine digits (no dashes). Try again...")
        SSNum = input("Employee "+ str(i) + ": What is the social security number? ")

# Get retirement percentage from user
def getPer(): 
    retPer = input("Employee "+ str(i) + ": What percentage of the salary is contributed to retirement? ")
    while "%" in retPer:
        print("Please do not include a percent sign (%) with your response...")
        retPer = input("Employee "+ str(i) + ": What percentage of the salary is contributed to retirement? ")
    intPer = int(retPer)
    while intPer < 0 and intPer > 41:
        print("Response is not between '0%' and 41%, try again...")
        retPer = input("Employee "+ str(i) + ": What percentage of the salary is contributed to retirement? ")

# Get annual salary from user
def getSalary():
    annSal = input("Employee "+ str(i) + ": What is the annual salary? ")
    while annSal.isdigit() == False:
        print("Salary must be a number. Try again...")
        annSal = input("Employee "+ str(i) + ": What is the annual salary? ")

# Main
i = 1
while i < 6:
    getName()
    getSSN()
    getPer()
    getSalary()
    again = input("Is there another employee (y/n)? ")
    if (again == "y" or again == "Y" or again == "yes" or again == "Yes"):
        i = i + 1
    elif (again == "n" or again == "N" or again == "no" or again == "No"):
        break
