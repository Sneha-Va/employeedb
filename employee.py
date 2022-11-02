while True:
    print("select an option from the menu")
    print('1 add employee')
    print('2 view employee')
    print('3 search  employee')
    print('4 update employee')
    print('5 delete employee')
    print('6 exit')
    
    choice=int(input('enter the option:'))
    if(choice==1):
        print("add employee")
    if(choice==2):
        print("view employee")
    elif(choice==3):
        print('search a employee')
    elif(choice==4):
        print('update the employee')
    elif(choice==5):
        print('delete the employee')
    elif(choice==6):
        break  