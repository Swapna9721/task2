#variable & typecasting
#1. Assign three different values to three different variables and print them
val1=45
val2=59
val3=68
print(val1,val2,val3)

#2.Wap to demonstrate single and multiple assignment of values to a varibles
a=7
print(a)
a=b=c=8
print(a,b,c)
a,b,c=4,5,6
print(a,b,c)

#3.Wap to swap two variables
a=6
b=5
temp=a
a=b
b=temp
print(a,b)

#4.Wap to demonstrate that a single variable can store differernt type of values at different instance of time
a=8
print(a)
a=7.8
print(a)
a='Hii'
print(a)

#5.Wap to constrate two strings.
str1="Hello"
str2="Welcome"
print(str1+'  '+str2)

#6.Wap to assign different type of values to one variable at different instance of and print its type each time
val1=7
print(type(val1))
val2=9.6
print(type(val2))
val3="swapna"
print(type(val3))
val4=True
print(type(val4))

#7.Wap to calculate simple interest, accept values for user(si=pnr/100)
P=float(input("Enter value of  principle amount :"))
N=float(input("Enter the number of years :"))
R=float(input("Enter the rate of interest :"))
#calculate simple interest by using this formula
SI = (P * N * R)/100
print("Simple interest : {}" .format(SI))