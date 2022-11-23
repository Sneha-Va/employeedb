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
        print("view employee")
        sql='SELECT * FROM `employees`' 
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i)
    elif(choice==3):
        print('search a employee')
        empcode=input("enter employee code:")
        sql='SELECT `id`, `empcode`, `empname`, `designation`, `salary`, `companyname`, `phoneno`, `emailid`, `password` FROM `employees` WHERE `empcode`='+empcode
        mycursor.execute(sql)
        result=mycursor.fetchall()
        print(result)
    elif(choice==4):
        print('update the employee')
        empcode=input('enter empcode:')
        empname=input("enter empname to be updated:")
        designation=input('enter designation to be updated:')
        salary=input("enter salary to be updated:")
        companyname=input("enter companyname to be updated:")
        phoneno=input("enter phoneno to be updated:")
        emailid=input("enter emailid to be updated:")
        password=input("enter password to be updated:")
        sql="UPDATE `employees` SET `empname`='"+empname+"',`designation`='"+designation+"',`salary`='"+salary+"',`companyname`='"+companyname+"',`phoneno`='"+phoneno+"',`emailid`='"+emailid+"',`password`='"+password+"' WHERE `empcode`= "+empcode
        mycursor.execute(sql)
        mydb.commit()
        print("data successfully updated")
    elif(choice==5):
        print('delete the employee')
        empcode=input("enter empcode:")
        sql='DELETE FROM `employees` WHERE `empcode`='+empcode
        mycursor.execute(sql)
        mydb.commit()
    elif(choice==6):
        break  