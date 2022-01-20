# Reading an entire file from .txt

print(f'\n***Reading the entire file:\n ')
with open('learning_python.txt') as file_object:
    contents = file_object.read()
print(contents.strip())


# Looping the file object.
filename = 'learning_python.txt'

print(f'\n***Lopping over the file object:\n ')
with open(filename)as file_object:
    for line in file_object:
        print(line.strip())


print(f'\nStoring the lines in a list and then working with them outside the with block.\n ')

filename = 'learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

# Replacing Python with C.
filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    line = line.strip()
    print(line.replace('Python', 'C'))
