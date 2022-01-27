def city_country(city, country, population=''):
    '''returns a single string of city country and her population.'''
    if population:
        whole_place = f'{city} {country} {population:} '
    else:
        whole_place = f'\n{city} {country}'
    return whole_place.title()