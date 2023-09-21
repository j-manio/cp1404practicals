"""
A shop requires a small program
that would allow them to quickly work out
the total price for a number of items, each with different prices.

user enter items and price of each different items
Then the program computes and displays the total price of those items.
If the total price is over $100,
then a 10% discount is applied to that total before the amount is displayed on the screen.
"""
total_price = 0
number_of_items = int(input("Number of Items (QTY): "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of Items (QTY): "))

for i in range(0, number_of_items):
    item_price = float(input("Price of item $: "))
    total_price += item_price
if total_price > 100:
    discount = (total_price * 10) / 100  # calculate the discount
    discounted_price = total_price - discount
    print(f"Total price for {number_of_items} item is ${discounted_price:.2f}")
else:
    print(f"Total price for {number_of_items} item is ${total_price:.2f}")
