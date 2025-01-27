# # numbers
# print(50 / 10) # float division(decimal)
# print(50 // 10) # integer division(whole #)
# print(50 // 50.5) # integer division - output with decimal 0.0 bc of float
# print(int(50 // 50.5)) # result is always an int -  type casting/ specify the data type, output 0
# print(10 % 2) # modulo - the remainder is the output

# # strings
# # print('it's monday) # syntax error
# print("it's monday") # 1. to rectify syntax error
# print('it\'s monday') # or prefix with a back slash 2 # escaping
# print(type('Hello'))

# # concatentation # plus symbol is polymorphic(does multiple things depending on context)
# print('Hello ' + 'World') # explicitly provide a space in string concatenation otherwise 
# a = 'Learn' = merge var a with var b into var c
# b = 'Python'
# c = a + b 
# print(c) # add a space c = a + '' + b
# # you can use a f-strings str.format()) or join() methods
# some modify string methods upper(), strip() to remove whitespace, replace(), split()
# # F-strings provide a concise and convenient way to 
# # embed Python expressions inside string literals for formatting

# # String methods
# print('Hello'.upper()) # dot notation => methods is a function that/ only works on strings - operate only on certain data types => a string then method, reverse of above where 
# # we call function first then  above print(type('Hello'))


# # Boolean
# # True
# # False
# print(type(True))

# # Falsy values => are values that are considered False when used in a condition, like in an if statement or bool expression
# # if we evaluate them in a boolean expression
# if not []:
#     print("Empty list is falsy")

# main falsy values
# 1. None: Represents "nothing." print(bool(None)) => used when we need to express the absence of a value 
# e.g if a variable contains nothing we have to be explicit using none since a var has to contain a value
# 2. False: The Boolean False.
# 3. Zero values: Any numeric zero, like 0, 0.0, or 0j (complex number). print(bool(0))
# 4. Empty sequences or collections:
# 5. Empty string: "" print(bool(""))
# 6. Empty list: [] print(bool[])
# 7. Empty tuple: () print(bool())
# 8. Empty dictionary: {} print(bool{})

# Comparison operators
# >, <, <=, >=, == # Equals always last

# Logical operators => and, or, not => used to combine conditional statements
# 1. and operator => returns True if both conditions are true; otherwise, it returns False.
# x = 5
# y = 10 # Both conditions must be true

# if x > 2 and y > 5:
#     print("Both conditions are true")  # Output: Both conditions are true
# else:
#     print("At least one condition is false")

# # 2. or operator =>returns True if at least one condition is true; it only returns False if both conditions are false
# x = 5
# y = 10 # At least one condition must be true


# if x > 7 or y > 5:
#     print("At least one condition is true")  # Output: At least one condition is true
# else:
#     print("Both conditions are false")

# 3. not Operator => inverts a boolean value
# If a condition is True, not makes it False, and vice versa
# x = 5

# if not x > 10: # Invert the result of the condition
#     print("x is not greater than 10")  # Output: x is not greater than 10
# else:
#     print("x is greater than 10")

# # variables =>  containers for storing data values - case-sensitive, no spaces
# num1 = 5
# num2 = 4
# print(num1 + num2)

# slicing - retrun a range of characters by using the slice syntax
# b = 'welcome'
# print(b[3:5]) # co

# Remove whitespace before/after text with strip method
# a = ' Hello, World'
# print(a.strip()) # 'Hello, World!'

# String format - # string interpolation
# we cant combine strings w numbers
# like this
# age = 36
# txt = 'hello, I am' + age
# print(txt) instead we use f-strings, the preferred way of formatting strings
# age = 36
# txt = f'hello, I am Jane + {age}'
# print(txt)

# # modifier and placeholders
# price = 20
# txt = f'The price is {price:.2f} dollars' # displays price with 2 decimals
# print(txt)

# # perform a math operation in the placeholder
# txt = f'The price is {20 * 20} dollars'
# print(txt)

# Escape character - to insert characters that are illegal in a string 
# txt = "Introduction to "Python" for beginners' is fun" # error 
# to fix this problem
# txt = "Introduction to \"Python\" for beginners' is fun" # * plus other escape characters
# print(txt)

