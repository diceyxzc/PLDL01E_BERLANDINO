#Start.

#Intialize total deduction, gross income, and net income.
totalDeduction = 0
grossIncome = 0
netIncome = 0

#Input the required employee data.
employeeName = str(input("Employee's Name:"))
employeeDepartment = str(input("Employee's Department:"))
ratePerHour = float(input("Rate per Hour:"))
workingHoursPerDay = float(input("Working Hors per Day:"))
daysPerWeek = float(input("Days per Week:"))
weeksPerMonth = float(input("Weeks per Month:"))

#Compute gross income.
grossIncome = ratePerHour * workingHoursPerDay * daysPerWeek * weeksPerMonth

#Convert the gross income equivalence of Philhealth and SSS contribution.
if 0 <= grossIncome <= 20000:
    philHealthContribution = 125.75
    sssContribution = 100
elif 20001 <= grossIncome <= 50000:
    philHealthContribution = 2200.50
    sssContribution = 1200
elif 50001 <= grossIncome <= 75000:
    philHealthContribution = 4800
    sssContribution = 6800
elif grossIncome > 75001:
    philHealthContribution = 5800
    sssContribution = 8800

#Initialize Pagibig contribution.
pagibigContribution = 100

#Compute total deduction and net income.
totalDeduction = philHealthContribution + sssContribution + pagibigContribution
netIncome = grossIncome - totalDeduction

#Display the employee's data.
print("---Employee Data---")
print("Employee's Name:", employeeName)
print("Department:", employeeDepartment)
print("Gross Income:", grossIncome)
print("Net Income:", netIncome)
print("Total Deduction:", totalDeduction)

#End.