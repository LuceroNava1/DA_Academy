#Lab Activity 3: Lists and Basic Algorithms
#Objective: Introduce lists, basic algorithms, and list manipulation in Python.

# 1. Create a list of integers containing at least 10 elements.
list = [3, 2, 4, 5, 6, 7, 8, 1, 2, 9]

# 2. Write a function that takes the list as input and returns the maximum and minimum values.
def max_min_a(list):
    max = max(list)
    min = min(list)
    result = "Maximo: %d, minimo: %d", max, min
    return result


def max_min_b(list):
    for l in list:
        maximo = l
        if l > maximo:
            maximo = l

    for l in list:
        minimo = l
        if l < minimo:
            minimo = l
    return "Maximo: %d, minimo: %d", maximo, minimo

def max_min_c(list):
    list.sort()
    return "Maximo: %d, minimo: %d", list[0], list[-1]


# 3. Implement a function that reverses the order of the elements in the list.
def reverse_a(list):
    return list.reverse()


def reverse_b(list):
    return list[::-1]


def reverse_c(original_list):
    reversed_list = []
    for value in original_list:
        reversed_list = [value] + reversed_list
    return reversed_list


# 4. Write a function that searches for a given value in the list and returns its index.
def index_a(list, list_value):
    return list.index(list_value)


# 5. Implement a function that takes a list of numbers and returns a new list with only the even numbers.

def even_numbers(list):
    new_list = []
    for i in list:
        if (2 % i == 0) & (i != 1):
            new_list.append(i)
    return new_list
