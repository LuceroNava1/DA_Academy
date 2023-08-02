#Lab Activity 2: Functions and File Handling
#Objective: Introduce functions and basic file handling operations in Python.

# 1. Write a function that takes two parameters, `num1` and `num2`, and returns their sum.
def sum(num1, num2):
    return num1 + num2

sum(8,87)

# 2. Create a text file named "numbers.txt" and write a few numbers, each on a new line.
file = open("new.txt", "x")#crear
file.close()


def write_numbers(list, name_file):
    file = open(name_file, "a")  # append
    for i in list:
        file.write(i)

    file.close()
    return list


# 3. Write a function that reads the numbers from the file and calculates their average.

def average(name_file):
    file = open(name_file, "r")
    lines = file.readlines()
    sum = 0

    for line in lines:
        sum += int(line.strip())
    file.close()
    return sum/len(lines)


# 4. Implement a function that takes a string as input and writes it to the end of the "numbers.txt" file.
def add_string(word, name_file):
    file = open(name_file, "a")  # append
    file.write(word)
    file.close()
    return word


# 5. Call the functions and print the results.
write_numbers(["1", "4", "45", "78"], "new.txt")
average("new")
add_string("HEllo", "numbers.txt")

