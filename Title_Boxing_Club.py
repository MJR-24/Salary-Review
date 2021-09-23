'''
 Ask for:
     Employee Name
     Social Security Number
     Percentage of Salary Contributed to Retirement
     Annual Salary 
 for UP TO 5 LOCAL TRAINERS

 IF user enters retirement # outside of normal range (0% to 40%):
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

# Print table function
def printTable():
    headingList =["Employee Code\t", "Salary\t", "Retirement\t", "Net Salary"]
    
    print(*headingList)
    for code, sal, ret, net in zip(codeList,salList, retList, netList):
        print(str(code).ljust(14) + '$'+str(sal).ljust(11)+ '$'+str(ret).ljust(15)+ '$'+str(net)) 

# Finds the employee with the highest salary
def getMaxSalary():
    maxSalary = max(salList)
    maxFirstName = salList.index(maxSalary)
    maxLastName = salList.index(maxSalary)
    print(f"\nNOTE: {fn[maxFirstName]} {ln[maxLastName]} has the highest salary with ${maxSalary}\n")

# Main
i = 1
codeList = []
salList = []
retList = []
netList = []
fn = []
ln = []

while i < 6:
    
# Get employee name from user
    empName = input("Employee "+ str(i) + ": What is the employee's first and last name? ")
    firstName = empName.split()[0]
    lastName = empName.split()[1]
    fn.append(firstName)
    ln.append(lastName)
    
# Get social security number from user
    SSNum = input("Employee "+ str(i) + ": What is the social security number? ")
    while len(SSNum) != 9:
        print("The social security number must be nine digits (no dashes). Try again...")
        SSNum = input("Employee "+ str(i) + ": What is the social security number? ")
    lastFour = SSNum[5:9]
    empCode = lastName+lastFour
    codeList.append(empCode)

# Get annual salary from user
    annSal = input("Employee "+ str(i) + ": What is the annual salary? ")
    while annSal.isdigit() == False:
        print("Salary must be a number(int). Try again...")
        annSal = input("Employee "+ str(i) + ": What is the annual salary? ")
    annSal = '{:.2f}'.format(float(annSal))
    salList.append(annSal)
    
# Get retirement percentage from user
    retPer = input("Employee "+ str(i) + ": What percentage of the salary is contributed to retirement? ")
    while "%" in retPer:
        print("Please do not include a percent sign (%) with your response...")
        retPer = input("Employee "+ str(i) + ": What percentage of the salary is contributed to retirement? ")
    
    intPer = int(retPer)
    
    if (intPer < 0) or (intPer > 40):
        notInRange = 0
    elif (intPer >= 0) or (intPer <= 40):
        notInRange = 1

    while notInRange == 0:
        if (intPer < 0) or (intPer > 40): 
            print("Response is not between '0%' and 40%, try again...")
            retPer = input("Employee "+ str(i) + ": What percentage of the salary is contributed to retirement? ")
            while "%" in retPer:
                print("Please do not include a percent sign (%) with your response...")
                retPer = input("Employee "+ str(i) + ": What percentage of the salary is contributed to retirement? ")
            intPer = int(retPer)
            notInRange = 0
        elif (intPer >= 0) or (intPer <= 40):
            notInRange = 1
    retire = '{:.2f}'.format((intPer/100)*float(annSal))
    retList.append(retire)

# Calculate net salary
    netSalary = '{:.2f}'.format(float(annSal) - float(retire))
    netList.append(netSalary)

#End or repeat loop
    again = input("Is there another employee (y/n)? ")

    if (again == "y" or again == "Y" or again == "yes" or again == "Yes"):
        i = i + 1
    elif (again == "n" or again == "N" or again == "no" or again == "No"):
        break


printTable()

#Print totals
print("------------------------------------------------------")
salList = [float(t) for t in salList]
retList = [float(t) for t in retList]
netList = [float(t) for t in netList]
print(f"{'Total'.ljust(13)} ${str((sum(salList))).ljust(10)} ${str((sum(retList))).ljust(14)} ${(sum(netList))}") 

getMaxSalary()