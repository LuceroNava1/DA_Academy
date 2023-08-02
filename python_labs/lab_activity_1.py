#Lab Activity 1: Variables and Control Flow
#Objective: Introduce variables, data types, and control flow statements in Python.

#1. Declare two variables, `num1` and `num2`, and assign them with integer values.
num1 = 4
num2 = 9

#2. Write a program that checks if `num1` is greater than `num2` and prints the result.
def is_greater(num1, num2):
    return num1>num2

#3. Use an `if-else` statement to determine if the values of `num1` and `num2` are equal or not, and print an appropriate message.
def are_equal(num1, num2):
    if num1 == num2:
        message = "Number 1 and number2 are equal"
    else:
        message = "Number 1 and number 2 are not equal"
    return print(message)

#4. Prompt the user to enter a number and store it in a variable.
number = int(input("Enter a number: "))

#5. Use a loop to print all the numbers from 1 to the user-input number.
for i in range(1, number, 1):
  print(i)