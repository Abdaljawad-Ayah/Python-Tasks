# Excercise One
# Write a Python program to sum all the items in a list

# def list(items):
#     sum_numbers = 0
#     for x in items:
#         sum_numbers += x
#     return sum_numbers

# print(list([5, 10, -8]))

# Excercise Two
# Write a Python program to multiply all the items in a list

# def multiply(items):
#     numbers_multplied = 2
#     for b in items:
#         numbers_multplied *= b
#     return numbers_multplied

# print(multiply([2, 2, 2]))

# Excercise Three
# Write a Python program to get the largest number from a list

# def max_numbers(list):
#     max = list[0]
#     for c in list:
#         if c > max:
#             max = c
#     return max

# print(max_numbers([-1, -2, -5, 0]))

# Excercise Four
# Write a Python program to get the smallest number from a list

# def smallest(list):
#     min = list[0]
#     for d in list:
#         if d < min:
#             min = d
#     return min

# print(smallest([1, 2, 5, 0]))

# Excercise Five
# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are the same from a given list of strings.


def match(words):
    counter = 0

    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            counter += 1
    return counter


print(match(['abc', 'xyz', 'aba', 'abc']))
