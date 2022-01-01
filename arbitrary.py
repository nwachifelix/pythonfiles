def my_rice_style(*red_oils):
    '''Show your red_oil rice recipe'''
    print(red_oils)

my_rice_style('white_rice')
my_rice_style('smoked_fish', 'fresh_pepper', 'red_oil', 'cray_fish', 'etc')

def my_rice_style(*red_oils):
    '''
    Summarize the rice I'm about to cook
    '''
    print('\nCooking red_oil rice with below ingredients: ')
    for red_oil in red_oils:
        print(f'- {red_oil}')

my_rice_style('white_rice')
my_rice_style('smoked_fish', 'fresh_pepper', 'red_oil', 'cray_fish', 'etc')