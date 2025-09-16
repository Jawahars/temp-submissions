import unittest


class TestCalculateFinalPrice(unittest.TestCase):


    def test_loyalty_level_1(self):

        base_price = 100

        quantity = 10

        loyalty_level = 1

        expected_price = 950

        self.assertEqual(calculate_final_price(base_price, quantity, loyalty_level), expected_price)


    def test_loyalty_level_2(self):

        base_price = 100

        quantity = 10

        loyalty_level = 2

        expected_price = 900

        self.assertEqual(calculate_final_price(base_price, quantity, loyalty_level), expected_price)


    def test_loyalty_level_3(self):

        base_price = 100

        quantity = 10

        loyalty_level = 3

        expected_price = 800

        self.assertEqual(calculate_final_price(base_price, quantity, loyalty_level), expected_price)


    def test_bulk_discount(self):

        base_price = 100

        quantity = 25

        loyalty_level = 1

        expected_price = 2250

        self.assertEqual(calculate_final_price(base_price, quantity, loyalty_level), expected_price)


    def test_bulk_discount_loyalty_level_2(self):

        base_price = 100

        quantity = 25

        loyalty_level = 2

        expected_price = 2000

        self.assertEqual(calculate_final_price(base_price, quantity, loyalty_level), expected_price)


    def test_bulk_discount_loyalty_level_3(self):

        base_price = 100

        quantity = 25

        loyalty_level = 3

        expected_price = 1500

        self.assertEqual(calculate_final_price(base_price, quantity, loyalty_level), expected_price)


    def test_zero_quantity(self):

        base_price = 100

        quantity = 0

        loyalty_level = 1

        expected_price = 0

        self.assertEqual(calculate_final_price(base_price, quantity, loyalty_level), expected_price)


    def test_negative_price(self):

        base_price = -100

        quantity = 10

        loyalty_level = 1

        expected_price = -950

        self.assertEqual(calculate_final_price(base_price, quantity, loyalty_level), expected_price)


if __name__ == '__main__':

    unittest.main()