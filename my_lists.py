# This is a program that outputs even and odd numbers.

my_list = [1, 2, 3, 4, 5, 6, 7, 21, 33, 32, 2, 4]
print(f'\nThese are the even numbers below. ')
for num in my_list:
    if num % 2 == 0:
        print(num)
print(f'\nThe values below are all odd numbers.')
#Testing for even numbers.

for num in my_list:
    if num % 2 != 0:
        print(num)

    