#1. Open, read, and write to files using `open()`, `read()`, `write()`, and `close()` functions.
f = open("myfile.txt", "x")
f = open("myfile.txt", "w") #This "w" command can also be used create a new file but unlike the the "x" command the "w" command will overwrite any existing file found with the same file name.
f.write("Hello There\n")
f.writelines(["Hello World ", "You are welcome to Fcc\n"])
f.close()

file = open("myfile.txt", "r") #('r’) opens the text files for reading only
print(file.read()) #The "f.read" prints out the data in the text file in the shell when run.
file.seek(0)
print(file.readline())
file.close()

#2. Use the `with` statement to automatically handle file closing.
#3. Import and use built-in modules like `random` or `datetime` to perform tasks such as generating random numbers or working with dates.
#4. Explore third-party modules and install them using package managers like `pip`.
#5. Utilize modules to create small projects or solve simple problems.