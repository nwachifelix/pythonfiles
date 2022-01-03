def make_akara(*beans):
    '''Builds the ingredients for the type of akara we are making'''
    print(beans)

# make_akara('beans')
make_akara('meat', 'egg', 'groundnut oil', 'pepper')

def build_profile(first, last, **user_info):
    '''Making the authors profile'''
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

authors_profile = build_profile('nwachi', 'felix', field='data analysis', location='canada', nationality='nigeria')
print(authors_profile)

def choice_cars(manufacturer, model, **mercedes_benz):
    mercedes_benz['mercedes_benz'] = manufacturer
    mercedes_benz['mercedes_benz'] = model
    return mercedes_benz

my_car = choice_cars('mercedes_benz', '2021 4matic', colour='black', special='custom plate',)
print(my_car)