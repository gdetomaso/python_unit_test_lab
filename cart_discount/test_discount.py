import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    
    # TODO more unit tests here. Each test should test one scenario
    def test_list_of_two_prices(self):
        prices = [10, 4]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_list_null_prices(self):
        prices = []
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_list_one_price(self):
        prices = [10]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_list_same_price(self):
        prices = [10, 10, 10, 10]
        expected_discount = 10
        self.assertEqual(expected_discount, discount(prices))

    def test_list_negative_price(self):
        prices = [-10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    def test_list_string_input(self):
        prices = ['10', '4', '20']
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    def test_list_float_input(self):
        prices = [10.0, 4.0, 20.0]
        expected_discount = 4.0
        self.assertEqual(expected_discount, discount(prices))
    

if __name__ == '__main__':
    unittest.main()