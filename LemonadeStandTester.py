# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 6/28/2022
# Description: Tests the LemonadeStand function with 5 tests designed to test a variety of classes and methods.

import unittest
from LemonadeStand import MenuItem, SalesForDay, LemonadeStand

class TestLemonadeStand(unittest.TestCase):
    """Contains unit tests for the LemonadeStand function."""

    def test_1(self):
        """Tests the get method for the stand name in the LemonadeStand class."""
        stand = LemonadeStand("Life's Lemons Tester")
        self.assertEqual(stand.get_standname(), "Life's Lemons Tester")

    def test_2(self):
        """Tests the get price method in the MenuItem class."""
        item1 = MenuItem('lemonade', 2, 5)
        self.assertAlmostEqual(item1.get_price(), 5)

    def test_3(self):
        """Tests the get_sales_dict method in the SalesForDay class."""
        sales = {"lemonade": 2, "limeade": 5}
        day0 = SalesForDay(0, sales)
        self.assertDictEqual(day0.get_sales_dict(), sales)

    def test_4(self):
        """Tests the total_profit_for_stand return in the LemonadeStand class for the included inputs."""
        stand = LemonadeStand("Life's Lemons")
        item1 = MenuItem("lemonade", 5, 7)
        stand.add_menu_item(item1)
        item2 = MenuItem("limeade", 6, 9)
        stand.add_menu_item(item2)
        salesday1 = {"lemonade": 10, "limeade": 5}
        stand.enter_sales_for_today(salesday1)
        salesday2 = {"lemonade": 5, "limeade": 17}
        stand.enter_sales_for_today(salesday2)
        profit = stand.total_profit_for_stand()
        self.assertAlmostEqual(profit, 96)

    def test_5(self):
        """Tests the currentday tracker in the LemonadeStand class."""
        stand = LemonadeStand("Life's Lemons")
        item1 = MenuItem("lemonade", 5, 7)
        stand.add_menu_item(item1)
        item2 = MenuItem("limeade", 6, 9)
        stand.add_menu_item(item2)
        salesday1 = {"lemonade": 10, "limeade": 5}
        stand.enter_sales_for_today(salesday1)
        salesday2 = {"lemonade": 5, "limeade": 17}
        stand.enter_sales_for_today(salesday2)
        self.assertAlmostEqual(stand._currentday, 2)

if __name__ == '__main__':
    unittest.main(exit=False)