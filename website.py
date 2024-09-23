

def website():
    company = []
    path = 'python_final/Company.txt'
    path2 = 'python_final/Income.txt'
    path3 = 'python_final/Report.txt'
    path4 = 'python_final/Expense.txt'
    # for i in range(0,100):
    while True:
        h1 = ['owner', 'admin', 'user']
        print(h1)
        role = input("Enter role: ")
        if role == 'owner':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if username == 'owner' and password == password:
                print('Logged in \nWhat do you want: ')
                for j in range(0,100):
                    h2 = {
                        '1': 'Create Company',
                        '2': 'View Company',
                        '3': 'GO back'
                        }
                    print(h2)
                    num = input('Enter number: ')
                    if num == '1':
                        
                        n = input('Write Company Name: ')
                        company.append(n)
                        print('Company Created')
                        with open(path, 'w') as obj:
                            try:
                                obj.write(n)
                            finally:
                                obj.close()
                    if num == '2':
                        with open(path, 'r') as obj:
                            try:
                                try:
                                    data = obj.read()
                                    print(str(data))
                                finally:
                                    obj.close()
                            except Exception as e:
                                print(f"Company not found: {e}")

                        n2 = input('Write company name: ')
                        print(company)
                        if n2 == str(data):
                            print("Company Opened")
                        else:
                            print("Company not found")
                    # if num == '3':

            else:
                print('Incorrect username or password')


        if role == 'admin':
            username = input("Enter username: ")
            password = input("Enter password: ")

            if username == 'admin' and password == password:
                print('Logged in \n What do you want: ')
                for j in range(0,100):
                    h2 = {
                        '1': 'Add income',
                        '2': 'Open Reports',
                        '3': 'Add or View Expenses',
                        '4': 'Log out'
                    }
                    print(h2)
                    income = 0
                    num2 = input('Enter number: ')
                    if num2 == '1':
                        add = int(input('Enter amount: '))
                        # with open(path2, 'w') as obj1:
                        #     try:
                        #         obj1.write(f'the new income is {add}')
                        #     finally:
                        #         obj1.close()
                        income += add
                        print('Income Added')
                    if num2 == '2':
                        with open(path3, 'r') as obj2:
                            try:
                                data2 = obj2.read().splitlines()
                                print(data2)
                            finally:
                                obj2.close()
                        print("Reports Opened")
                    if num2 == '3':
                        e = input('Add or View Expense: ')
                        if e == 'Add':
                            text = input('Enter Expenses: ')
                            with open (path4, 'w')as obj3:
                                try:
                                    obj3.write(f'Expense = {text}')
                                finally:
                                    obj3.close()
                            print('Expenses Added')
                        if e == 'View':
                            with open (path4, 'r')as obj3:
                                try:
                                    obj3.read().splitlines()
                                finally:
                                    obj3.close()
                            print('Expenses Opened')
                    if num2 == '4':
                        exit()
            else:
                print('Incorrect username or password')


        if role == 'user':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if username == 'user' and password == password:
                print('Logged in \nWhat do you want: ')
                for j in range(0,100):
                    h2 = {
                        '1': 'View Income',
                        '2': 'Add or View Expenses',
                        '3': 'Add Report'
                        }
                    print(h2)
                    num3 = input('Enter number: ')
                    if num3 == '1':
                        with open(path2, 'r') as obj1:
                            try:
                                data3 = obj1.read().splitlines()
                                print(data3)
                            finally:
                                obj1.close()
                        print('Income Shown')
                    if num3 == '2':
                        exp = input('Add or View Expense: ')
                        if exp == 'Add':
                            text2 = input("Enter Expenses: ")
                            with open (path4, 'w')as obj3:
                                try:
                                    obj3.write(f'Expense = {text2}')
                                finally:
                                    obj3.close()
                            print('Expenses Added')
                        if exp == 'View':
                            with open (path4, 'r')as obj3:
                                try:
                                    obj3.read().splitlines()
                                finally:
                                    obj3.close()
                            print('Expenses Added')
                    if num3 == '3':
                        add2 = input('Enter Report: ')
                        with open(path3, 'w') as obj2:
                            try:
                                obj1.write(f'the new income is {add2}')
                            finally:
                                obj1.close()
                        print('Reports Added')
            else:
                print('Incorrect username or password')
website()