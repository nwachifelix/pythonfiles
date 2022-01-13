class Restaurant:
    '''A class that describes a restaurant and its cuisine.'''
    
    def __init__(self, name, cuisine):
        '''Activate name and cuisine'''
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        '''Tells the type of restaurant and the cuisine offered.'''
        print(f'{self.name} is a local reataurant that specializes in Nigerian cuisines. ')
        

    def open_restaurant(self):
        '''Tells the public that we re open for business.'''
        print(f'{self.name} is now open to the public. ')

my_fav_restaurant = Restaurant('Abi\'s Bukka', 'Palm oil rice')
print(f'\nThe name of the bukka where I have lunch is: {my_fav_restaurant.name}. ')
print(f'My favourite meal there is: {my_fav_restaurant.cuisine}. ')
