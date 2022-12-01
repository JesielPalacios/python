# Homework
# Make a program where I can find the average of the expenses in the year.

expenses_of_the_year = 0

total_number_of_months = int(
    input(f"Enter the total number of months to average : "))

print()
print('Write the number 0 if you don\'t have any expenses in some month.')

for i in range(total_number_of_months):
    expenses = float(
        input(f'Now enter the expenses for the month number {i+1}: '))

    expenses_of_the_year += expenses/total_number_of_months

print()
print('The average of your expenses in the year was: $ ' +
      str(expenses_of_the_year))
