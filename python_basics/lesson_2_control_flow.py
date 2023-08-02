#1. Use `if` statements to check conditions and execute code blocks.
age = 23
if (age >= 16 and age <= 40):
    print("Puedes formar parte de la tripulación de Pyratilla")

#2. Add `else` statements to handle alternative cases.

age = 13
if (age >= 16 and age <= 40):
    print("Puedes formar parte de la tripulación de Pyratilla")
else:
    print("No satisfaces una necesidad básica para pertenecer a la tripulación del gran Pyratilla")

#3. Incorporate `elif` statements for multiple conditional branches.
age = 20

if age > 40:
    print("No puedes pertenecer a la tripulación, te pasas de la edad límite que ha puesto el gran capitán Pyratilla.")
elif age >= 16:
    print("Podrás optar a pertenecer la tripulación. Aún te queda superar la entrevista con el capitán.")
else:
    print("Eres muy pequeño todavía para la vida pirata!")

#4. Create loops with `for` and `while` statements to repeat code execution.
i = 10
print("Preparados para despegue. Empieza la cuenta atrás.")
while i >= 0:
  print(i)
  i -= 1
else:
  print("La cuenta atrás ha finalizado.")

#for
s = "Me gustan las matemáticas"

for c in s:
  print(c)

#La función range() tiene 3 posibles argumentos:start stop step
for i in range(1, 11, 1):
  print(i)

# imprimir los 10 primeros números naturales invirtiendo el orden
for i in range(10, 0, -1):
  print(i)

#5. Use control flow statements to solve simple problems, such as finding the largest number in a list.

def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, -8, 0]))