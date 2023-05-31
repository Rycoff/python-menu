print('''Welcome to this simple menu. To start, type help.''')

while True:
    command = input('Option: ')
    if command == 'help':
        print('''
        Help Section:
        -------------
        help    -->    Show the help section
        menu    -->    Open menu
        exit    -->    Exit the program
        ''')
    elif command == 'menu':
        print('''
        Menu:
        -----
        1. Option 1
        2. Option 2
        3. Option 3
        4. Option 4
        5. Back
        ''')
        while True:
            ans = input('Select an number: ')
            if ans == '1':
                print('Execute option 1')
            elif ans == '2':
                print('Execute option 2')
            elif ans == '3':
                print('Execute option 3')
            elif ans == '4':
                print('Execute option 4')
            elif ans == '5':
                print('Returning')
                break
            else:
                print('This number does not exist')
    elif command == 'exit':
        print('Good bye')
        exit()
    else:
        print('This option does not exist, type help to get more info.')
