import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='employeedb')
mycursor = mydb.cursor()
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
        empcode=input('enter empcode:')
        empname=input("enter empname:")
        designation=input('enter designation:')
        salary=input("enter salary:")
        companyname=input("enter companyname:")
        phoneno=input("enter phoneno:")
        emailid=input("enter emailid:")
        password=input("enter password:")
        sql='INSERT INTO `employees`(`empcode`, `empname`, `designation`, `salary`, `companyname`, `phoneno`, `emailid`, `password`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
        data=(empcode,empname,designation,salary,companyname,phoneno,emailid,password)
        mycursor.execute(sql,data)
        mydb.commit()
        print("view employee")
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