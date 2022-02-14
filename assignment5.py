#1.Wap to determine input number is even or odd
num= int(input("Enter any number to test whether it is odd or even: "))
if (num % 2)==0:
    print("The number is even")
else:
    print("The number is odd ")

#2.Find out if a given year is a leap year or not.
def CheckLeap(Year):
 if((Year%400==0) or
    (Year%100!=0) and
    (Year%4==0)):
    print("Given year is a leap Year")
 else:
    print("Given year is not a leap Year")
Year=int(input("Enter the number: "))
CheckLeap(Year)

#3.Wap to check if a triangle is valid or not(input-3 angles of triangle)
def is_valid_triangle(a,b,c):
    if a+b+c==180 and a!=0 and b!=0 and c!=0:
        return True
    else:
        return False
angle_a = float(input('Enter angle a: '))
angle_b = float(input('Enter angle b: '))
angle_c = float(input('Enter angle c: '))
if is_valid_triangle(angle_a,angle_b,angle_c):
        print('Triangle is valid.')
else:
        print('Triangle is Invalid.')

#4.Wap to determine if the seller has made profit or loss. Display amount of profit/loss.
#(input:cost price and selling price)
actual_cost = float(input("Please Enter the Actual Product Price: "))
sale_amount = float(input("please Enter the sales Amount: "))
if(actual_cost>sale_amount):
    amount=actual_cost - sale_amount
    print("Total Loss Amount= {0}".format(amount))
elif(sale_amount>actual_cost):
    amount =sale_amount - actual_cost
    print("Total Profit={0}".format(amount))
else:
    print("No Profit No Loss!!!")