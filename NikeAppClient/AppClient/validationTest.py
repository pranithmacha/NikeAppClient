'''
Created on Mar 20, 2013

@author: ferrari
'''
import unittest
from validations import Validations


validation = Validations()

class Test(unittest.TestCase):

    def test_check_valid_userId_emptyName(self):
        result = validation.check_valid_userId("")
        self.assertFalse(result)

    def test_check_valid_userId_starts_with_special_char(self):
        result = validation.check_valid_userId("@adsda")
        self.assertFalse(result)

    def test_check_valid_userId_starts_with_number(self):
        result = validation.check_valid_userId("7adsda")
        self.assertFalse(result)

    def test_check_valid_userId_length_greaterThan_nine(self):
        result = validation.check_valid_userId("aaaaaaaaaadsda")
        self.assertFalse(result)
    def test_check_valid_userId_None(self):
        result = validation.check_valid_userId(None)
        self.assertFalse(result)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_check_valid_userId']
    unittest.main()