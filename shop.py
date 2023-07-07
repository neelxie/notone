# declare a dictionary of shop_items and their prices. Also declare an integer of customer_money 100
shop_items = {"designer apple": 300.00, "designer crisps": 35.00, "designer water": 45.00, "designer sandwich": 60}
​
# Declare the customer's initial amount of money.
customer_money = 100
​
​
# this function provides a breakdown of all items available and their prices
def list_shop_items_and_prices():
    list_stock_options = ""
    option = 1
    for item, price in shop_items.items():
        list_stock_options += f'{option}={item}(£{str(price)}0).  '
        option += 1
    return list_stock_options
​
# this function welcomes the customer, allows them to exit and takes the item input from the user
def greeting():
    print(f"Welcome! Here are the items we have on sale:  {list_shop_items_and_prices()}")
    chosen_item = input("Enter the name of the item you would like to buy (or type 'exit' to exit the shop): ")
    if chosen_item == "exit":
        quit()
    return chosen_item
​
​
choice = greeting()
​
​
# this function checks the choice is a shop item and raises a ValueError if it isn't
def check_item_stocked(chosen_item):
    if chosen_item not in shop_items:
        raise ValueError(f'"{choice}" is not an item in the shop')
    else:
        find_my_item_price(choice)
#
#
# this function iterates through the expensive_items dictionary and returns the item name and item cost
def find_my_item_price(chosen_item):
    for item in shop_items:
        if item == chosen_item:
            item_price = shop_items[item]
            return item, item_price
​
​
item_name, item_cost = find_my_item_price(choice)
​
​
# this function checks if the amount of money is enough
def check_enough_money(money=customer_money, price_of_item=item_cost, extra_money=0):
    if money + extra_money >= price_of_item:
        return True
    else:
        return False
​
​
# this function requests more money
def request_more_money():
    tries = 0
    while tries < 3:
        extra_money_provided = int(input("Do you have any more money? Enter the amount or enter 0: "))
        if check_enough_money(extra_money=extra_money_provided):
            goodbye()
        else:
            tries += 1
    raise Exception("You don't have enough money, please leave")
​
​
# this function hands over the item and greets the customer out of the shop, then terminates
def goodbye():
    hand_over_item = f'Here\'s your "{choice}". It\'s so much better than having non-{choice}, taste the difference!'
    thanks = "Thank you for visiting! Take care!"
    print(hand_over_item, thanks)
    quit()
​
​
# here we run the shop program
def run_shop():
    check_item_stocked(choice)
    item_name, item_cost = find_my_item_price(choice)
    if check_enough_money(customer_money, item_cost):
        goodbye()
    else:
        request_more_money()
​
​
run_shop()
