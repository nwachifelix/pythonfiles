import unittest
from city_functions import city_country

class test_city_country(unittest.TestCase):
    '''Test for city_functions.py'''
    
    def test_city_country(self):
        '''Do city country like "Lagos Nigeria" work?'''
        whole_place = city_country('lagos', 'nigeria')


    def test_city_country_population(self):
        '''Do city like "Lagos Nigeria, Population" work?'''
        whole_place = city_country('lagos nigeria', 'population: 1,000,000')
        self.assertEqual(whole_place, 'Lagos Nigeria, Population: 1,000,000')

if __name__ == '__main__':
    unittest.main()