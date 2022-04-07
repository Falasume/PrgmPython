###########################################
# Desc: Lab 15 Unit Test
# Author: Hannah Noftall W0424894
###########################################
import unittest
from average import average

class TestStringMethods(unittest.TestCase):

    def test_average(self):
        myList = [45,30,7,13,25,678]
        self.assertEqual(average(myList), 133.0)

    def value_error_test(self):
        with self.assertRaises(TypeError):
            average()

# Program starts here
if __name__ == '__main__':
    unittest.main()