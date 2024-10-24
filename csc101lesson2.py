# -*- coding: utf-8 -*-
"""CSC101Lesson2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Bh9_OQxiCmZPFbFSGxjSFRiBDhdw89Xz

# $\textbf{Strings}$

# String Literals

In python to represent strings we surround them by either single quotation marks or double quotation marks.

'string' is same as "string"


If you want to display the string literal you can use print() command
"""

print("Hello")
print('Hello World')

"""# Multiline Strings
You can assign a multiline string to a variable by using three quotes:
"""

#Poem: Roses Are Red by Mother Goose


poem = """The rose is red,
The violet's blue,
Sugar is sweet,
And so are you."""
print(poem)



"""

```
# This is formatted as code
```

Or three single quotes:"""

poem='''The rose is red,
The violet's blue,
Sugar is sweet,
And so are you.'''
print(poem)

"""# More about strings

Using + operator we can link two or more distinct strings. It is called string concatenation


"""

print('a'+'b')
print('a'+' '+'b') # a blank space
print ('a', ' ', 'b')
print ('a', 'b')

print('Working'+'on'+'this'+'exercise.') #There is no space in between
print('Working'+' '+'on'+' '+'this'+' '+'exercise.')

"""# Exercise

Write a code following the directions:

- Assign a string "My favorite food is" into a variable named X
- Assign your favorite meal into a variable named Y
- Using string concatenation link X and Y and display it on the screen using print


If your favorite meal is fries after you concatenate it will appear as

My favorite food is fries.

"""

x = 'My favorite food is '
y = 'Rice'
print(x+y)

"""# Note

We can't combine strings and int or float data type with concetanation
"""

#We can't perform arithmetical operations between
#strings and integers, or strings and floats (decimal numbers).


print('4'+1)

"""# Exercise

In the given Python script what is the data type of var3?

var1="4"

var2="1"

var3=var1+var2

print(var3)

**<class 'int'>**

# $\textbf{Escape Character in String}$

In Python, strings are sequences of characters that represent textual data. They allow us to store and manipulate text, but sometimes, we encounter special characters that have a specific meaning in Python. To represent these special characters within a string, we use escape characters.

# Escape Character:

An escape character is a backslash (\) followed by another character that changes the meaning of the following character in a string. It is used to represent characters that are difficult to type or have special significance, such as newlines, tabs, or quotation marks.

Common Escape Sequences:

    \n: Represents a newline character. It is used to start a new line in the output.
    \t: Represents a tab character. It is used to create horizontal spacing.
    \\: Represents a literal backslash. It is used when you need to include an actual backslash in your string.
    \" or \': Represents a double quote or a single quote, respectively. It is used to include quotes within a string defined with the same type of quotes.

#Newline
"""

print("Hello\nWorld")

"""#Tab"""

print("Name:\tJohn")

"""#Literal Backslash"""

print("C:\\Users\\John")

"""#Quotation Marks"""

print("He said, \"Hello!\"")

"""# $\textbf{Reading Input From the Keyboard}$

- When you are programming usually you will require user to enter an input and program will read the input to perform operations
-  The data is read from the keyboard and it is stored in a variable to use later by the program



"""

# Get the user's first name
first_name= input('Enter your first name:')

# Get the user's last name
last_name = input ('Enter your last name:')

#Print a greeting to the user
print('Welcome', first_name, last_name)

"""# Reading Number with the input Function

-  The input function always returns the user's input as a string, even if the user enters numeric data
-  For example, suppose you call the input function and enter the number 100, and press ENTER key. The value returned from the input is '100'
-  If you want to do mathematical operations you can't because your output is a string
-  You can use built-in functions to convert a string to a numeric data type
-  After you convert a string to numeric data type you can perform arithmetic operations

"""

number= input("What is the number?")
print(type(number))

int(number)  # value converted to an int
float(number) #  value converted to a float

#First statement gets the number of hours and assign to a value as a string
#Second statement calls the int()function, passing string_value as an argument
#This is inefficient because it creates two varaiables

string_value= input('How many hours did you work?')

hours=int(string_value)
print(type(hours))

"""# Displaying Formatted Output with F-strings
-  F-strings are special type of string literal that allow you to format a variety of ways
-  With an f-string, you can create messages that contain the contents of variables, and you can format numbers in a variety of ways
-  An f-string is a string literal that is enclosed in quotation marks and prefixed with the letter f
"""

#f'Hello world'
print(f"Hello world")
print(f'Hello world')

name='Johny'
last_name= 'Dean'
print(f'Hello {name}') #{name} is a placeholder inside f-string
print(f"Hello {last_name}")
print(f"Hello {name} {last_name}")




# print("Hello "+name)
# print("Hello", name)
# print("Hello Johny")

#With f-string and without f-string

age = 20
name= "Mark"

print(f'{name} is currently {age} years old.')

print(name, "is currently", age, "years old")

"""# Exercise

Ask the user to enter his/her first name, last name and age and using f string display for example My name is Mark Jones and I am 20 years old
"""

name='Denielle'
last_name= 'Simmonds'
age = 20
print(f"I am {name} {last_name} and I am {age} years old.")

# Placeholders can contain any valid expression


print(f'The number is {10+2}.')

print(f'The number is 10+2.')

number=10
print(f'The number is {number+2}.')

"""# Formatting Values
## Rounding Floating-Point Numbers
-  Sometimes we want to format the decimal display
-  17 significant digits appear when float data type is used
"""

#how a floating-point number is displayed with no formatting

water_bill= 7000.0
monthly_water_bill = water_bill/12.0
print(monthly_water_bill)
print(f'The monthly payment is {monthly_water_bill}')

"""-  In the above examplemonthly payment is representing dollor value. When we are talking about money as you know we can have at most 2 decimal places
-  We can format monthly_water_bill value using .2f
"""

#Rounding floating-point number

water_bill= 7000.0
monthly_water_bill = water_bill/12.0

print(f'The monthly payment is {monthly_water_bill:.2f}')

number=123123.456
print(f'Here is my number {number:.1f}')

# You can also round it to 1 decimal place

a=2
b=3

print(f'{a/b:.3f}')

"""-  Sometimes it is better to read a number which consists of few digits with comma

-  We can format a number to have comma seperator
"""

# You can even combine comma seperators and rounding the number

value = 123456789.12345
print(f'{value:,.3f}')

x=10020030045.12345
print(f'{x:,.3f}')

"""## Formatting a Floating-Point Number as a Percentage

-  % can  be used to format floating numbers as a percentage

-  When you use % the number is multiplied by 100
"""

percent= 0.6

print(f'{percent:%}')

# Round output value to 0 decimal places
percent= 0.6
print(f'{percent:.0%}')

"""# Work on it Now Together

- Assign 971825.12334 to a variable called value_1 and using the print function and f-string display your output as rounded to 3 decimal places

- Assign 6734911444 to a variable called value_2 and using the print function and appropriate f-string display your output with comma.

"""

value_1 = 971825.12334
print(f"{value_1:.3f}")

value_2 = 6734911444
print(f"{value_2:,}")

"""# $\textbf{Lists}$

In Python we represent list with square bracket. List consists of items which can be changed and the list
items are ordered.

#Length of a List
"""

#Create a list
lst1 = ['kiwi', "banana", "orange"]
lst2=[1,2,3,4]

#len returns the number of items in the list

print(len(lst1))
print(len(lst2))

"""# Concatanate Two Lists"""

#Concatanate two lists

lst3=lst1+lst2
print(lst3)

"""#The Repitation Operator

As you might remember we used to multiply two numbers. We can also use as a repitation operator. When we use * and a list to repeat the items in the list.
"""

numbers=[0]*5
print(numbers)

lst4 = ['x', 'y'] * 5
print(lst4)

"""#Positive indexing, Negative indexing

First item: [0] (Note: List first index starts from 0 in python, this is called positive indexing)

Last item: [-1] (Note: List index from last starts from -1 in python, this is called negative indexing)
"""

list1 = ["a", 15, 2.9] #List can contain int, float, string at the same time

print(list1)
print(list1[0]) # Accessing First item in list1
print(list1[1]) # Accessing Second item in list1
print(list1[2]) # Accessing Third item in list1
print(list1[-1]) # Accessing Last item in list1
print(list1[-2]) # Accessing Second Last item in list1
print(list1[-3]) # Accessing Third Last item in list1