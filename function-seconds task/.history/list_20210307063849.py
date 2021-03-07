# First Excercise
# Write a Python program to sum all the items in a list


def list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers


print(list([1, 2, -8]))
