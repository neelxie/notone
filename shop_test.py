from unittest import TestCase, mock
import shop
from shop import list_shop_items_and_prices, greeting, check_item_stocked, find_my_item_price, check_enough_money
​
class TestCheckEnoughMoney(TestCase):
# test to see dictionary is output correctly for the customer - this test works fine
    def test_list_shop_items_and_prices(self):
        self.assertEqual(list_shop_items_and_prices(), ("1=designer apple(£300.00).  2=designer crisps(£35.00).  3=designer water(£45.00).  4=designer sandwich(£600).  "))
​
class TestGreetingInputRecognisedCorrectly(TestCase):
    @mock.patch('builtins.input', side_effect='designer apple')
    def test_greeting(self, param):
        self.assertEqual(greeting(), 'designer apple')
​
class TestCheckItemStocked(TestCase):
    @mock.patch.object(shop, 'find_my_item_price')
    @mock.patch('builtins.input', side_effect='designer apple')
    def test_check_item_stocked_correct(self):
        mock_find_my_item_price.return_value = 'designer apple', 300
        self.assertEqual(check_item_stocked('designer apple'), 'designer apple', 300)
​
class TestCheckFindMyItemPrice(TestCase):
    @mock.patch.object(shop, 'greeting')
    @mock.patch('builtins.input', side_effect='designer apple')
    def test_find_my_item_price(self):
        self.assertEqual(find_my_item_price('designer apple'), ('designer apple', 300.00))
​
​class TestCheckEnoughMoneyYES(TestCase):
    def test_enough_money_yes(self):
        self.assertTrue(check_enough_money(money=100, price_of_item=35, extra_money=0))
​
    def test_enough_money_no(self):
        self.assertFalse(check_enough_money(money=100, price_of_item=300, extra_money=0))
​
    def test_enough_money_yes_with_extra(self):
        self.assertTrue(check_enough_money(money=100, price_of_item=300, extra_money=250))
​
    def test_enough_money_no_with_extra(self):
        self.assertFalse(check_enough_money(money=100, price_of_item=300, extra_money=100))
​
if __name__ == '__main__':
    unittest.main()
​
