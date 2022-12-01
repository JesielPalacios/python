# Homework
# Make a program where I can find the average of the expenses in the year.

months_with_name_and_number = [
    {"month_number": 1, "month_name": 'January'},
    {"month_number": 2, "month_name": 'February'},
    {"month_number": 3, "month_name": 'March'},
    {"month_number": 4, "month_name": 'April'},
    {"month_number": 5, "month_name": 'May'},
    {"month_number": 6, "month_name": 'June'},
    {"month_number": 7, "month_name": 'July'},
    {"month_number": 8, "month_name": 'August'},
    {"month_number": 9, "month_name": 'September'},
    {"month_number": 10, "month_name": 'October'},
    {"month_number": 11, "month_name": 'November'},
    {"month_number": 12, "month_name": 'December'},
]

expenses_of_the_year = []
average_expenses = 0
counter_expenses = 0

print('Write the number 0 if you don\'t have any expenses in some month.')
for month in months_with_name_and_number:
    month_expenses = float(
        input(f"Now enter the expenses for the month of {month['month_name']}: "))

    expenses_of_the_year.append(month_expenses)

for expense in expenses_of_the_year:
    counter_expenses += expense

average_expenses = counter_expenses/len(expenses_of_the_year)

print()
print('The average of your expenses in the year was: $ ' + str(average_expenses))
