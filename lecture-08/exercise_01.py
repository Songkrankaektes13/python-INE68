num_emps = int(input('How many employee records do you want to create? '))
with open('employees.txt', 'w') as emp_file:
    for count in range(3, num_emps + 3):
        print('Enter data for employee #', count)
        name = input('Name:')
        id_num = input('ID number:')
        dept = input('Department:')

        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')
        print()
print('Employee records written to employees.txt.')