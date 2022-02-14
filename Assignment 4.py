#1.Wap to demonstrate use of arithmetic operation(numeric as well as str object)
num1= input("enter first number: ")
num2= input("enter second number: ")
sum=float(num1)+float(num2)
min=float(num1)-float(num2)
print('The sum of {0} and {1} is{2}'.format(num1,num2,sum))
print('The subtraction of {0} and {1} is {2}'.format(num1,num2,min))

#2.Wap to demonstrate use of assignment operators(numeric as well as str object)
a=3
b=4
c=a+b
a-=b
print(c)
print(a)

#3.Wap to demonstrate use of comparison operators(numeric as well as str object)
a=2
b=4
print(a==b)

#4.Wap to demonstrate use of logical operators(numeric as well as object)
a=10
b=10
c=-10
if a>0 and b>0:
    print("The number are greater than 0")
else:
    print("Atleast one number is not greater than 0")
