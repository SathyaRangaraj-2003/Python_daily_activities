#activity_06

employee = "Abi"
hours_worked = 45.75
hourly_rate = 350.50
bonus = 1500
target_hours = 40


print("{0:*^40}".format("Employee Report"))

print("{0:>20}{1:>20}".format("Employee Name:",employee))

print("{0:>20}{1:>20}".format("Hours Worked:",hours_worked))

print("{0:>20}{1:>20}".format("Target Hours:",target_hours))

overtime = abs(target_hours - hours_worked)
print("{0:>20}{1:>20.2f}".format("Overtime :",overtime))

total_pay = (hours_worked * hourly_rate) + bonus
print("{0:>22}{1:>010.2f}".format("Total Pay: $",total_pay))