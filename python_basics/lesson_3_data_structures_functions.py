#1. Explore lists and perform operations like indexing, slicing, and appending.
l = ["Juan", 31, 172.32, True]
print(l)
l[1]
l[-2]

fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
['apple', 'banana', 'cherry', 'orange']

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
['apple', 'banana', 'cherry', ['Ford', 'BMW', 'Volvo']]

a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
a[2:5]
a[-5:-2]
a[-5:-2] == a[1:4]

#Omitting the first index a[:n] starts the slice at the beginning of the list.
a[:4]
['spam', 'egg', 'bacon', 'tomato']
#Omitting the last index a[m:] extends the slice from the first index m to the end of the list.
a[2:]
['bacon', 'tomato', 'ham', 'lobster']
#Omitting both indexes a[:] returns a copy of the entire list, but unlike with a string, it’s a copy, not a reference to the same object.
a[:]
['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']

a == a[:]
True

#2. Understand strings and their manipulation (concatenation, uppercase/lowercase conversion).
#Using + operator
s1 = 'Apple'
s2 = 'Pie'
s3 = 'Sauce'
s4 = s1 + s2 + s3

print(s4)


#Using join() method
s1 = 'Hello'
s2 = 'World'

print('Concatenated String using join() =', "".join([s1, s2]))

print('Concatenated String using join() and whitespaces =', " ".join([s1, s2]))

#Using % operator
s1 = 'Hello'
s2 = 'World'

s3 = "%s %s" % (s1, s2)
print('String Concatenation using % Operator =', s3)
#String Concatenation using % Operator = Hello World

#Using format() function
s1 = 'Hello'
s2 = 'World'

s3 = "{}-{}".format(s1, s2)
print('String Concatenation using format() =', s3)
#String Concatenation using format() = Hello-World

s3 = "{in1} {in2}".format(in1=s1, in2=s2)
print('String Concatenation using format() =', s3)
#String Concatenation using format() = Hello World

#Using f - string(Literal String Interpolation)
s1 = 'Hello'
s2 = 'World'

s3 = f'{s1} {s2}'
print('String Concatenation using f-string =', s3)
#String Concatenation using f-string = Hello World

name = 'Pankaj'
age = 34
d = 10

print(f'{name} age is {age} and d={d}')
#Pankaj age is 34 and d=10

#3. Create functions with parameters and return values.
def multiplica(val1, val2):
  return val1 * val2

multiplica(3, 5)

#4. Practice calling functions with different arguments.

#5. Apply functions to solve specific tasks, like calculating the factorial of a number.
def factorial(numero):
    if numero <= 0:
        return 1
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    return factorial


def factorial_recursivo(numero):
    if numero <= 1:
        return 1
    return numero * factorial(numero-1)


valor = 5
f = factorial(valor)
print(f"El factorial de {valor} es {f}")
f = factorial(valor)
print(f"El factorial (calculado de manera recursiva) de {valor} es {f}")