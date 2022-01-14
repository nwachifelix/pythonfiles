# class Restaurant:
#     '''A class that describes a restaurant and its cuisine.'''
    
#     def __init__(self, name, cuisine):
#         '''Activate name and cuisine'''
#         self.name = name
#         self.cuisine = cuisine

#     def describe_restaurant(self):
#         '''Tells the type of restaurant and the cuisine offered.'''
#         print(f'{self.name} is a local reataurant that specializes in Nigerian cuisines. ')
        

#     def open_restaurant(self):
#         '''Tells the public that we re open for business.'''
#         print(f'{self.name} is now open to the public. ')

# my_fav_restaurant = Restaurant('Abi\'s Bukka', 'Palm oil rice')
# print(f'\nThe name of the bukka where I have lunch is: {my_fav_restaurant.name}. ')
# print(f'My favourite meal there is: {my_fav_restaurant.cuisine}. ')


# print('..........................................................')
# my_fav_restaurant.open_restaurant()
# my_fav_restaurant.describe_restaurant()

# my_wife_restaurant = Restaurant('Mega Chicken', 'fried rice and gizard')
# print(f'\nMy wife\'s favouriye restaurant is: {my_wife_restaurant.name}. ')
# print(f'And her best meal there is: {my_wife_restaurant.cuisine} ')
# print('..........................................................')
# my_wife_restaurant.describe_restaurant()
# my_wife_restaurant.open_restaurant()


class User:
    '''Holds information about a user.'''

    def __init__(self, first_name, last_name, country, location, age):
        '''Initialize user.'''
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.country = country.title()
        self.location = location.title()
        self.age = age

    def describe_user(self):
        '''Tells about about a junior dev from Nigeria'''
        print(f'{self.first_name} {self.last_name} is a junior Python dev who specializes in data analysis and wed development. ')
        print(f'From southeast part of {self.country}.')
        print(f'whose location is {self.location}. ')
        print(f'and is {self.age} years old. ')

    def greet_user(self):
        '''Sends a personalized greeting to the user.'''
        print(f'Hello {self.first_name} {self.last_name}, how re you today? ')


user = User('nwachi', 'felix', 'nigeria', 'canada', 33)
user.describe_user()
user.greet_user()
    