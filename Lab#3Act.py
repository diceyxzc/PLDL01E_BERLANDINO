#Start.

#Initialize constant variables.
pagibigContribution = 100

#Input all required variables.
print("|--Employee Personal Data--|")
companyName = str(input("Enter Company Name: "))
employeeDepartment = str(input("Enter Department: "))
employeeCode = str(input("Employee Code: "))
employeeName = str(input("Employee Name: "))
cutOffPeriod = str(input("Cut-Off Period: "))

print("")
print("|--Employee Sumnmary Statement--|")
ratePerHour = float(input("Rate Per Hour: "))
hoursPerPayday = float(input("Hours Per Payday: "))
hoursOvertimed = float(input("Hours Overtimed: "))
hoursAbsent = float(input("Hours of Absence: "))
hoursTardiness = float(input("Hours of Tardiness: "))
givenHonorarium = float(input("Honorarium: "))

#Compute for all expected computed outcomes.
payPeriod = cutOffPeriod
basicPay = ratePerHour * hoursPerPayday
overtimePay = hoursOvertimed * ratePerHour
absences = hoursAbsent * ratePerHour
tardiness = hoursTardiness * ratePerHour
grossEarnings = basicPay + overtimePay + givenHonorarium

#SSScontribution [Based: Date as of January 2023]
if grossEarnings > 19750:
    sssContribution = 900.00
elif 16750 <= grossEarnings <= 17249.99:
    sssContribution = 765.00
elif 16250 <= grossEarnings <= 16749.99:
    sssContribution = 742.50
elif 15750 <= grossEarnings <= 16249.99:
    sssContribution = 720.00
elif 15250 <= grossEarnings <= 15749.99:
    sssContribution = 697.50
elif 14750 <= grossEarnings <= 15249.99:
    sssContribution = 675.00
elif 14250 <= grossEarnings <= 14749.99:
    sssContribution = 652.50
elif 13750 <= grossEarnings <= 14249.99:
    sssContribution = 630.00
elif 13250 <= grossEarnings <= 13749.99:
    sssContribution = 607.50
elif 12750 <= grossEarnings <= 13249.99:
    sssContribution = 585.00
elif 12250 <= grossEarnings <= 12749.99:
    sssContribution = 562.50
elif 11750 <= grossEarnings <= 12249.99:
    sssContribution = 540.00
elif 11250 <= grossEarnings <= 11749.99:
    sssContribution = 517.50
elif 10750 <= grossEarnings <= 11249.99:
    sssContribution = 495.00
elif 10250 <= grossEarnings <= 10749.99:
    sssContribution = 472.50
elif 9750 <= grossEarnings <= 10249.99:
    sssContribution = 450.00
elif 9250 <= grossEarnings <= 9749.99:
    sssContribution = 427.50
elif 8750 <= grossEarnings <= 9249.99:
    sssContribution = 405.00
elif 8250 <= grossEarnings <= 8749.99:
    sssContribution = 382.50
elif 7750 <= grossEarnings <= 8249.99:
    sssContribution = 360.00
elif 7250 <= grossEarnings <= 7749.99:
    sssContribution = 337.50
elif 6750 <= grossEarnings <= 7249.99:
    sssContribution = 315.00
elif 6250 <= grossEarnings <= 6749.99:
    sssContribution = 292.50
elif 5750 <= grossEarnings <= 6249.99:
    sssContribution = 270.00
elif 5250 <= grossEarnings <= 5749.99:
    sssContribution = 247.50
elif 4750 <= grossEarnings <= 5249.99:
    sssContribution = 225.00
elif 4250 <= grossEarnings <= 4749.99:
    sssContribution = 202.50
elif grossEarnings < 4250:
    sssContribution = 180.00

#PhilHealth Contribution [Based: Date as of 2024]
if grossEarnings < 10000:
    philHealthContribution = 0.03 * grossEarnings
elif 10000 <= grossEarnings <= 69999:
    philHealthContribution = 0.035 * grossEarnings
elif grossEarnings > 70000:
    philHealthContribution = 0.05 * grossEarnings

#Withholding Tax [Based: Date as of January 1, 2023]
if grossEarnings < 20833:
    withHoldingTax = 0.00
elif 20833 <= grossEarnings <= 33332:
    withHoldingTax = 0.15 * 20833
elif 33333 <= grossEarnings <= 66666:
    withHoldingTax = 8541 + 0.20 * 33333
elif 66667 <= grossEarnings <= 166666:
    withHoldingTax = 8541.80 + 0.25 * 66667
elif 166667 <= grossEarnings <= 666666:
    withHoldingTax = 33541.80 + 0.30 * 166667
elif grossEarnings > 666667:
    withHoldingTax = 183541.80 + 0.35 * 666667

totalDeductions = absences + tardiness + withHoldingTax + sssContribution + philHealthContribution + pagibigContribution
netPay = grossEarnings - totalDeductions

#Display Employee Data.
print("")
print("[--]Employee Personal Data Sheet[--]")
print(" | Company Name:", companyName)
print(" | Department:", employeeDepartment)
print(" | Employee Code:", employeeCode)
print(" | Cut-off Period:", cutOffPeriod)
print(" | Pay Period:", payPeriod)
print(" | Basic Pay: {:.2f}".format(basicPay))
print(" | Overtime Pay: {:.2f}".format(overtimePay))
print(" | Absences: {:.2f}".format(hoursAbsent))
print(" | Honorarium: {:.2f}".format(givenHonorarium))
print(" | Tardy: {:.2f}".format(tardiness))
print(" | Withholding Tax: {:.2f}".format(withHoldingTax))
print(" | SSS Contribution: {:.2f}".format(sssContribution))
print(" | Pagibig Contribution: {:.2f}".format(pagibigContribution))
print(" | Philhealth Contribution: {:.2f}".format(philHealthContribution))
print(" | Gross Earnings: {:.2f}".format(grossEarnings))
print(" | Deductions: {:.2f}".format(totalDeductions))
print(" | Net Pay: {:.2f}".format(netPay))