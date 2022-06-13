# Python Variables
# Creating Variables
x = 8
y = "chandan"
print(x)
print(y)
print(" ") # this print new line
print(" ") # this print new line

x = 4       # x is of type int
x = "Mahanta" # x is now of type str
print(x) #Here x will print str
print(" ") # this print new line
print(" ") # this print new line



#                                         Casting
#If you want to specify the data type of a variable, this can be done with casting.
v1 =str(3)   # v1 will be print "3"
v2 =int(3)   # v2 will be 3
v3 =float(3) # v3 will be 3.0

print(v1)
print(v3)
print(v2)
print(" ") # this print new line
print(" ") # this print new line



#                                   Get the Type
#You can get the data type of a variable with the type() function.
v4 = 8
v5 = "Chandan"
print(type(v4))
print(type(v5))
print(" ") # this print new line
print(" ") # this print new line



#                              Single or Double Quotes?
#String variables can be declared either by using single or double quotes:
v6 = "ckm"
v7 ='ckm'
print(v6)
print(v7)
print(" ") # this print new line
print(" ") # this print new line


##                                 Case-Sensitive
##Variable names are case-sensitive.
v = " small latter"
V = " capital latter"
print(v)
print(V)
print(" ") # this print new line
print(" ") # this print new line




#                                    Variable Names
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

myVar = " love"
_myVar = "Family"
my_Var = "Bangladesh"
My1var = " 017"
myVar1 = "gofast"
myvar_1 = "End"

print(myVar)
print(_myVar)
print(my_Var)
print(My1var)
print(myVar1)
print(myvar_1)
print(" ") # this print new line
print(" ") # this print new line


#                             Multi Words Variable Names
# Variable names with more than one word can be difficult to read.
#
# There are several techniques you can use to make them more readable:

# Camel Case
# Each word, except the first, starts with a capital letter:
myVariableName = " Camel case  "

# Pascal Case
# Each word starts with a capital letter:

MyVariableName=" Pascal case"

# Snake Case
# Each word is separated by an underscore character:
my_Variable_name=" Snake case "
print(myVariableName)
print(MyVariableName)
print(my_Variable_name)
print(" ")
print(" ")


#                                  Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:
a , b = "10", "20"
print(a)
print(b)
print(" ")

m,n,o,p = "ab","cd","ef","gh"
print(m)
print(n)
print(o)
print(p)
print(" ")

#                            One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:
var1=var2 =var3 = "VarAll"
print(var1)
print(var2)
print(var3)
print(" ")

# Unpack a Collection
# If you have a collection of values in a list, tuple etc.
# Python allows you to extract the values into variables. This is called unpacking.

car =["Audi","BMW", "Mercedes"]
car1, car2, car3 = car
print(car1)
print(car2)
print(car3)
print(" ")

# Output Variables
# The Python print() function is often used to output variables.
# In the print() function, you output multiple variables, separated by a comma:
vAr1="I"
vAr2="LOVE"
vAr3="BANGLADESH"
print(vAr1,vAr2,vAr3)

# You can also use the + operator to output multiple variables:
print(vAr1 +" " + vAr2 + " " + vAr3)

#For numbers, the + character works as a mathematical operator:

num =8
num1 =8
print(num,num1)  # It will print 88
print(num+num1)  # print 16

# In the print() function,
# when you try to combine a string and a number with the + operator, Python will give you an error:
numb=8
str22="possetiveNumber"
# print(numb + str)  # not print

# The best way to output multiple variables in the print()
# function is to separate them with commas,
#  which even support different data types:
print(numb,str22)  # print
print(" ")

# Global Variables
# Variables that are created outside of a
# function (as in all of the examples above) are known as global variables.
#
# Global variables can be used by everyone, both inside of functions and outside.
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# If you create a variable with the same name inside a function, this variable will be local,
# and can only be used inside the function.
# The global variable with the same name will remain as it was, global and with the original value.
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)



