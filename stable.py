cars = ['mercedes benz', 'subaru', 'bmw', 'toyota']
for car in cars:
      if car == 'bmw':
          print(car.upper())
      else:
         print(car.title())

requested_toppings = 'mushroom'
if requested_toppings != 'achivous':
     print('Hold the achivous')
answer = 17
if answer != 42:
    print("That is not the current answer, try again!")

banned_users = ["andrew", "carolina", "david"]
user = "marie"
if user not in banned_users:
    print(f"{user.title()},you can't post a response if you wish.")

game_active = True
can_edit = False

maersk_cadiz = 'maersk shipping'
print("Is maersk_cadiz == 'maersk shipping'? I guess it's True!")
print(maersk_cadiz == 'maersk shipping')

age = 17
if age >= 18:
    print("You re old enough to vote! ")
    print("Have you registered to vote yet? ")
else:
    print("Sorry you re too young to vote. ")
    print("Please register to vote as soon as you turn 18! ")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"\nYou adimssion cost is ${price}. ")

requested_toppings = ["mushrooms", "extra cheese"]
if "mushrooms" in requested_toppings:
    print("Adding mushrooms. ")
if "pepperoni" in requested_toppings:
    print("adding pepperoni. ")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese. ")

print("\nFinished making your pizza! ")
