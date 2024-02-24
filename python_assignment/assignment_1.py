# Q1)Declare two variables with num1 and num 2
num1= int(input("enter number 1 :" ))
num2= int(input("enter number 2:"  ))
# now the sum of the number
add = num1+num2
print("the sum of num1 and num2 is ", add )

# task_1_end

# Q2) display msg with the world
message = input("enter you message:" )
adittional_string = "world!"
print(message+adittional_string)

# task_2_end

#  Q3)Declare a variable is_python_fun and assign it a boolean value
is_python_fun = True  

# Print a statement based on whether Python is considered fun
if is_python_fun:
    print("Python is considered fun!")
else:
    print("Python may not be considered fun by everyone.")

# task_3_end

# Q4)Create a list called fruits with at least three different fruit names
fruits = ["Apple", "Banana", "cherry"]

# Print the initial list
print("Initial list of fruits:", fruits)

# Add a new fruit to the list 
new_fruit = "mango"
fruits = fruits + [new_fruit]

# Print the updated list
print("Updated list of fruits:", fruits)

# task_4_end

# Q5) convert float value into integer value

# Declareing a variable called price with a floating-point value
price = 76.75

# Convert the floating-point value to an integer
price_integer = int(price)

# Print both the original and converted values
print("Original price (float):", price)
print("Converted price (integer):", price_integer)
 
#  task_5_end

# Q6)creating dictioary

student_info = {'name': 'Abdul Rafay', 'age': 20, 'grade': 'A'}
print("Student Information:", "Name:", student_info['name'], "Age:", student_info['age'], "Grade:", student_info['grade'])

# task_6_end

# combining 2 strings using concatenation 

string1= "programming is all" 
string2= " about problem solving "

combined_string= string1 + "" + string2
# string interpolation to include the length of the resulting string in a print statement , f function is used with {} to display string interpolation and its length together 

print(f"the combined string is : '{combined_string}' and its length is :{len(combined_string)} ")

# task_9_end

# creatinga a tuple named days_of_weeks

days_of_weeks=("monday" , "tuesday" , "wednesday" ,"thursday" , "friday" )

# acces and print the third day of the week
third_day= days_of_weeks[2] 
print("the third day of the weeks is :" ,third_day)

# task_10_end

result= True + False
print("the result is :", result)

a = 5
b = 10

result = a == b  # This is a comparison using the == operator
print(result)    # This will print False, as 5 is not equal to 10


num1 = 5
num2 = 2

sol=num1//num2 
print("the solution to this is :" , sol)

num3= 5
num4= 2
sol=(num3%num4)
print("the final answere to the solution is :", sol)

a=34
b=35
add=a+b
print(f"please print the following value {add} this a test run plese be succesfull")

