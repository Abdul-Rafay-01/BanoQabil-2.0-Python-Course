#  Abdul Rafay 
# midterm exam 
# Q1 - Write a Python program to do arithmetical operations addition and division.
num1=int(input ("the first number is :") )
num2=int(input ("the second number is: ") )
sum= num1+num2 
print( "the sum are :", sum)

# the devision
num1=int(input ("the first number is :") )
num2=int(input ("the second number is: ") )
division=num1/num2
print( "the division of the num is :", division)



# Q2 - Write a Python program to find the area of a triangle
base= int(input("base :  ", ))
height= int(input("height:  ", ))
area=0.5*(base*height)
print("the area of the triangle is :" , area)


# Q3 - Write a Python program to convert Celsius to Fahrenheit.
celcius=float(input("the tenperature in celcius "))
fahrenheit= ((9/5*celcius)+32 )
print("the temperature in fahrenhiet ", fahrenheit)

# Q4 - Write a Python program that return all datatypes that we discussed in the class.
name= input("name : " )
print("the datetype of this " , type(name))

num=int(input ("the number is :" ))
print("the datetype of this " , type(num))

fl=float(input ("the float number is : "))
print("the datetype of this " , type(fl))

bo=bool(input("the bo is : ") )
print("the datetype of this " , type(bo))         