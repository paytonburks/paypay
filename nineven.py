user_name = input("what is your name? ")
print("hi, " + user_name)

#for a numeric input, typecast to int() or float()

user_number = input (int("what is your favorite number? "))
print(type(user_number))


#print formatting of decimal (floating) numbers
#c style

import math

print("%.2f" %(math.pi))

#python style
#print ("{:.2f)}".format(math.pi))

#how to round a decimal number
pi_rounded = round(math.pi, 2)
print(pi_rounded)

#conditionals
# if a boolean condition is true, then execute some code

x = 5
if x == 5:
    print("x is 5")
else:
    print("x is not 5")

#loops
#while loop in python is just like in C/C++/Java

