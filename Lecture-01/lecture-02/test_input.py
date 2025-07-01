first_name = input('Enter your first name: ')

last_name = input('Enter your last name: ')

print('hello' , first_name , last_name)


1 #get the user's name , age , and income.
name = input('what is your name? ')
age = int(input('what is your age? '))
income = float(input('what is your income? '))

# Display the data.
print('Here is the data you entered: ')
print('Name:' , name)
print('Age:' , age)
print('Income: ' , format(income, '12,.2f'))
