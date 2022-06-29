# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 6/26/2022
# Description: Creates a Lemonade Stand and tracks menu items including cost and price, sales, and returns totals for
#              sales per item, profit per item, and total profit.

class InvalidSalesItemError(Exception):
    pass


class MenuItem:
    """Represents a menu item with a name, cost, and price."""

    def __init__(self, name, cost, price):
        """Creates a menu object with a name, cost, and price."""
        self._name = name
        self._wholesale_cost = cost
        self._selling_price = price

    def get_name(self):
        """Returns the item name."""
        return self._name

    def get_cost(self):
        """Returns the item cost."""
        return self._wholesale_cost

    def get_price(self):
        """Returns the item price."""
        return self._selling_price


class SalesForDay:
    """Represents sales for a day with the day number and a dictionary of sales of menu items."""

    def __init__(self, day, salesdict):
        """Creates an object that holds sales for a day with the day number and a dictionary of sales of menu items."""
        self._day = day
        self._sales_dict = salesdict

    def get_day(self):
        """Returns the day number."""
        return self._day

    def get_sales_dict(self):
        """Returns the sales dictionary for a given day."""
        return self._sales_dict


class LemonadeStand:
    """Represents a Lemonade Stand with a name, the current day, a menu dictionary, and a sales record list."""

    def __init__(self, standname):
        """Creates a Lemonade Stand object with a name, the current day, a menu dictionary, and a sales record list."""
        self._standname = standname
        self._currentday = 0
        self._menu = {}
        self._salesrecord = []

    def get_standname(self):
        """Returns the stand name."""
        return self._standname

    def add_menu_item(self, MenuItem):
        """Adds a menu item to the menu dictionary."""
        self._menu[MenuItem.get_name()] = MenuItem

    def enter_sales_for_today(self, dictionary):
        """Adds a given day's sales to the sales record list. Raises error if item sold is not in menu dictionary."""
        for key in dictionary:

            if key not in self._menu:
                raise InvalidSalesItemError

        self._salesrecord.append(SalesForDay(self._currentday, dictionary))

        self._currentday += 1

    def sales_of_menu_item_for_day(self, num, item):
        """Returns the number of a given item sold on a given day."""
        salesperday = self._salesrecord[num].get_sales_dict()

        salesnum = 0

        if item in salesperday:
            salesnum = salesperday[item]

        return salesnum

    def total_sales_for_menu_item(self, item):
        """Returns the total sales of a menu item."""
        totalsales = 0
        i = 0

        while i < self._currentday:
            totalsales += self.sales_of_menu_item_for_day(i, item)

            i += 1

        return totalsales

    def total_profit_for_menu_item(self, item):
        """Returns the total profit for a menu item."""
        menuitem = self._menu[item]

        totalcost = menuitem.get_cost()

        totalprice = menuitem.get_price()

        totalsold = self.total_sales_for_menu_item(item)

        return (totalprice - totalcost) * totalsold

    def total_profit_for_stand(self):
        """Returns the total profit for the stand."""
        totalprofit = 0

        for item in self._menu:
            totalprofit += self.total_profit_for_menu_item(item)

        return totalprofit


if __name__ == '__main__':
    stand = LemonadeStand("Life's Lemons")
    item1 = MenuItem("lemonade", 5, 7)
    stand.add_menu_item(item1)
    item2 = MenuItem("limeade", 6, 9)
    stand.add_menu_item(item2)
    sales = {"lemonade": 10, "limeade": 5, "ice": 2}
    try:
        day1 = LemonadeStand.enter_sales_for_today(stand, sales)
    except InvalidSalesItemError:
        print("One or more items sold is not on the menu.")
    else:
        print(stand.sales_of_menu_item_for_day(0, "lemonade"))