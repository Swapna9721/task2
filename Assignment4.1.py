#1.Wap to calculate x raised to the power n (x^n).Accept the value of x and n from the user.
import math
x= int(input("Enter the value of x: "))
n= int(input("Enter the value of n: "))
result  = math.pow(x,n)
print("The",x,"*",n,"is:",int(result))

#2.Wap to calculate average of three numbers. Accept numbers from user.
a =int(input("Enter the First Number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
average=(a+b+c)/3
print("The average of three number is",average)

#3.Wap to convert degree to radian
pi=22/7
degree = float(input("Input degrees: "))
radian = degree*(pi/180)
print(radian)

#4.Wap to convert radian to degree
def Convert(radian):
    pi=3.1415
    degree = radian * (180/pi)
    return degree
radian = 5
print("degree =",(Convert(radian)))

#5.Wap to calculate the area of trapezoid
base_1 = 6
base_2 = 7
height = float(input("Height of trapezoid: "))
base_1 = float(input('Base one value:'))
base_2 = float(input('Base two value:'))
area = ((base_1) + (base_2) / 2) * height
print("Area is:", area)

#6.Wap to calculate the area of parallelogram
base = float(input('Length of base: '))
height = float(input('Measurement of height: '))
area = base * height
print("Area is: ",area)

#7.Wap to calculate surface area and volume of cylinder
import math
r=float(input("Enter radius of a cylinder: "))
h=float(input("Enter the Height of a cylinder: "))
s_area=2*math.pi*pow(r,2)*h
volume=math.pi*pow(r,2)*h
print("surface area of a cylinder will be %.2f" %s_area)
print("volume of a cylinder will be %.2f" %volume)

#8.Wap to calculate surface area and volume of sphere
PI=3.14
radius=float(input('Please Enter the Radius of a Sphere: '))
sa = 4 * PI * radius * radius
Volume = (4/3)*PI*radius*radius*radius
print("\n The Surface area of a Sphere = %2.f" %sa)
print("\nThe Volume of a Sphere = %.2f" %Volume)