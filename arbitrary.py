def my_rice_style(*red_oils):
    '''Show your red_oil rice recipe'''
    print(red_oils)

my_rice_style('white_rice')
my_rice_style('smoked_fish', 'fresh_pepper', 'red_oil', 'cray_fish', 'etc')

def my_rice_style(size, *red_oils):
    '''
    Summarize the rice I'm about to cook for entire family
    '''
    print(f'\nCooking {size} inch pot red_oil rice with below ingredients: ')
    for red_oil in red_oils:
        print(f'- {red_oil}')

my_rice_style(18, 'white_rice')
my_rice_style(18, 'smoked_fish', 'fresh_pepper', 'red_oil', 'cray_fish', 'etc')

def build_profile(first, last, **user_info):
    '''
    Building a dictionary containing everything we know about a user
    '''
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('nwachi', 'felix', 
                            location='manitoba',
                            field='data_analysis')

print(user_profile)