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


def max_numbers(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max_numbers


print(max_num_in_list([1, 2, -8, 0]))
