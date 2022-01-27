import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    '''Tests for 'name_function.py'.'''

    def test_first_last_name(self):
        '''Do names like "Janis Joplin" work?'''
        formatted_name = get_formatted_name('janis', 'joplin')
    

    def test_first_last_middle_name(self):
        '''Do names like "Wolfgang Amadeus Mozart" work?'''
        formatted_name = get_formatted_name('wolfgand', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()