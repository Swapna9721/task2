#1.Wap to check type of data accepted using input()function
number1 = input("Enter number and hit enter")
print("printing type of input value")
print("type of number ", type(number1))

#2.Wap to accept name fun user and display
 #  Hello Username
def hello():
    name=str(input("enter the name : "))
    print("hello "+ str(name))
    return
hello()

#3.Accept first name middle name and surname from user (Use 3 input().) Display the user input as
# surname firstname middlename
str1=input("Enter first name : ")
str2=input("Enter Middle name : ")
str3=input("Enter surname : ")
print(str3,str2,str1)

#4.Accept name,age and address form user and display it as(you are allowed to use only 1 print())
#Name:Username
#Age:Userage
#Address:UserAddress
def personal_details():
    name,age = "swapna",21
    address = "Pune, Maharashtra, India"
    print("Name: {}\nAge: {}\nAddress: {}" .format(name,age,address))
personal_details()
#5.Accept student details-rollno,Name,percent and display as (use 2 print())
# Roll no  Name  Percentage
# UserRoll Username Userpercent
def student_details():
    Rollno, name, percentage = 45 ,"Swapna Tarade",80
    UserRoll, Username, Userpercent = 50 ,"Neha Desai", 70
    print("Roll no: {},name: {}, percentage: {}" .format(Rollno,name,percentage))
    print("UserRoll: {}, Username:{}, Userpercent: {}" .format(UserRoll, Username, Userpercent))
student_details()

