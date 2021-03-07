# # Logical Operators

# # Consider the variables #Exercise One

num1 = 5
num2 = 6
num3 = -10
num4 = 50
num5 = 2
# False or True = False
print(num1 > num2) or (num3 > num4)

# True and False = True
print(num1 != num3) and (num4 < num5)

# True or True  = True
print((num4 + num5) > 0) or (num2 < num3)

# True
print(not (num2 == num4))

print('===================')

# Simplify the following logical expressions for an arbitrary Boolean bol #Exercise Two

a = (1 > 5)
print({False and (a)})

a = (0 != 0)
print({False or (a)})

a = (10 > 10)
print({True or (a)})

a = (10 < 5)
print({not (a)})

print('===================')

# Starting with the following variable definitions Determine the value of #Exercise Three

bol1 = 5.2
bol2 = 15
bol3 = 5
bol4 = 6
bol5 = 20.5

print(bol4 == bol1 or bol2 and not bol3)

print(bol5 == (not bol1 and bol3) or bol2)
