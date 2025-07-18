keep_going = 'y'

while keep_going == 'y':
    sales = float(input('Enter the amount of sales:'))
    comm_rate = float(input('Enter the commission rate:'))

    commission = sales * comm_rate

    print(f'The commmimssion is ${commission:.2f}')

    keep_going = input('Do you went to calculeate another' + \ 'commission (Enter y for yes'))