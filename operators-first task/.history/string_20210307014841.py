# PYTHON STRING
# Excercise One
# Initialize a variable containing the string “Triceratops”. Using string operators

# 1
# t = 'triceratops'

# print(t.upper())
# # 2
# t = 'TRICERATOPS'

# print(t.lower())

# 3

# t = 'triceratops'
# sub = 't'
# # sub = 'p'
# print(t.count(sub))

# 4

# t = 'triceratops'
# print(t.find('a'))

# Excercise Two
# Write a program that asks the user for their name and country of residence

# print("Enter your name")
# name = input().upper()
# print("Enter your Country")
# country = input().upper()
# print(f"Hey !! {name}, from {country} welcome")

# Excercise Three
# Write a program that accepts an arbitrary user input and then lists the number of each vowel (a, e, i, o, u) in the string.

# t = 'joijfowijvroijvojq'

# print(t.split())  # im trying to solve this task

def char_frequency(str1):
  dict = {}
  for n in str1:
    keys = dict.keys()
    if n in keys:
      dict[n] += 1 
    else:
      dict[n] = 1 
  return dict
 print (char_frequency('joijfowi'))
    
# Excercise Four
# Write a program that asks the user for their first and last name (use two separate commands for this

# print("Enter first name")
# a = str(input())
# print("Enter last name")
# b = str(input())

# print(a.capitalize() + b.capitalize(), 'az'.upper().split("[]"))

# print(f"sum of {a} and {b} is {a+b}".split("[]")) # dont use that

# Excercise Five
# Initialize a variable containing the string {\code{"Allosaurus"}}. Using character indices

# import random
# string = ['A', 'l', 'l', 'o', 's', 'a', 'u', 'r', 'u', 's']
# random.shuffle(string)
# print(''.join(string))