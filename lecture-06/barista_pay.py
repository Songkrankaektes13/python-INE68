NUM_EMPLOYEES = 6

def main():
    hours = [0] * NUM_EMPLOYEES

    for index in range(NUM_EMPLOYEES):
        print('enter the hours worked by emplooyee',index + 1, ':', sep=', end='' ')
        hours[index] = float(input())

    pay_rate = float(input('enter the hourly papy rate: '))

    for index in range(NUM_EMPLOYEES):
        gross_pay = hours[index] * pay_rate
        print('gross pay for employee', index + 1, ': $', format(gross_pay, ',.2f'), sep='')
    
main()