def city_country(c_name1, country='canada'):
    '''Returns the name of a city and country neatly formatted'''
    formatted_name = f'My japa city and country is: {c_name1.title()}, {country.title()}.'
    return formatted_name

japa_country_1 = city_country('manitoba')
japa_country_2 = city_country('ontario')
japa_country_3 = city_country('toronto')
print(japa_country_1)
print(japa_country_2)
print(japa_country_3)


def make_album(first_name, last_name, album):
    '''Returns a dictionary of information about an artist'''
    artist = {'first': first_name.title(), 'last': last_name.title(), 'album': album.title()}
    return artist

creator = make_album('tupac', 'shakur', 'do for love')
print(creator)

def make_album(album, first_name='tupac', last_name='shakur'):
    '''Returns a dictionary of information about an artist'''
    artist = {'album': album.title()}
    return artist

chef = make_album('black_jesus')
print(chef)

# An optional parameter 'None' introduced. 
def make_album(first_name, last_name, album, numberOfsongs=None):
    '''Returns a dictionary of information about an artist'''
    artist = {'first': first_name.title(), 'last': last_name.title(), 'album': album.title()}
    if numberOfsongs:
        artist['numberOfsongs'] = numberOfsongs
    return artist

creator = make_album('tupac', 'shakur', 'do for love')
print(creator)

# Another parameter 'numberofsongs' is included. 
def make_album(first_name, last_name, album, numberOfsongs):
    '''Returns a dictionary of information about an artist including number of songs'''
    artist = {'first': first_name.title(), 'last': last_name.title(), 'album': album.title(), 'numberOfsongs': 15}
    return artist

creator = make_album('tupac', 'shakur', 'do for love', 15)
print(creator)

# The last section allows users to input artist name and album title and outputs a dictionary.
def make_album(first_name, last_name, album):
    '''Returns a dictionary of information about an artist including number of songs'''
    artist = {'first': first_name.title(), 'last': last_name.title(), 'album': album.title()}
    return artist

while True:
    print('\nPlease tell us Artist name and album:')
    print('(Enter "e" anytime to exit)')
    
    first = input('first_name: ')
    if first == 'e':
        break
   
    last = input('last_name: ')
    if last == 'e':
        break
    
    album = input('album: ')

    k_v_pairs = make_album(first, last, album)
    print(k_v_pairs)   


    