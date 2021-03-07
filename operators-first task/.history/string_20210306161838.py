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

# print(t.split())

import collections
str1 = 'joijfowijvroijvojq'
d = collections.defaultdict(int)
for c in str1:
    d[c] += 0

for c in sorted(d, key=d.get):
    if d[c] > 1:
        print('%s %d' % (c, d[c]))
