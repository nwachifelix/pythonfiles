'''Create a list of numbers and find the maximum number in it.'''
my_list = [1, 2, 7, 3]
# Set the maximum variable equal to 0: 
maximum = 0

for number in my_list:
    if number > maximum:
        maximum = number
# Check the result. 
print(maximum)

'''Implementing the Bubble Sort algorithm in python.'''
# Start with a list of numbers. 
list_1 = [5, 8, 1, 3, 2]

still_swapping = True
while still_swapping:
    still_swapping = False
    for i in range(len(list_1) - 1):
        if list_1[i] > list_1[i+1]:
            list_1[i], list_1[i+1] = list_1[i+1], list_1[i]
            still_swapping = True

# Check result: 
print(list_1)

'''Implementing the Linear Search Algorithm.'''
# Start with a list of numbers. 

list_2 = [5, 8, 1, 3, 2]
# Specify a value to search_for: 
search_for = 8
ressult = -1

# Loop through the list. If the value equals the search value, set the result, and exit the loop.
for i in range(len(list_2)):
    if search_for == list_2[i]:
        result = i 
        break
# Check the result:

print(result)

'''Implementing the Binary Search Algorithm in Python.'''
# Start with a list of numbers. 
list_3 = [2, 3, 5, 8, 11, 12, 18]
# Specify the value to search_for:
search_for = 11

slice_start = 0
slice_end = len(list_3) -1

# Add a variable to indicate whether the search was successful: 
found = False 

while slice_start <= slice_end and not found:
    location = (slice_start + slice_end) // 2
    if list_3[location] == search_for:
        found = True
    else:
        if search_for < list_3[location]:
            slice_end = location - 1
        else:
            slice_start = location + 1
# Check the results: 
print(found)
print(location)
