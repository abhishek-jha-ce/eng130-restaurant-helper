# Lists - Restaurant Waiter Helper Program

## User Stories

1. As a User I want to be able to see the menu in a formatted way, so that I can order my meal.

2. As a User I want to be able to order 3 times, and have my responses added to a list, so they aren't forgotten

3. As a user, I want to have my order read back to me in formatted way, so I know what I ordered.

### Showing the user menu items:

```commandline
item_list = ["Burger", "Pizza", "Fish and Chips", "Pasta", "Biryani", "Enchiladas", "Sandwich", "Noodles", "Sushi"]

order_list = []

print("XYZ Restaurant")
print("Select an item from the list:")
for i in range(len(item_list)):
    print(i + 1, ".", item_list[i])

Output:
XYZ Restaurant
Select an item from the list:
1 . Burger
2 . Pizza
3 . Fish and Chips
4 . Pasta
5 . Biryani
6 . Enchiladas
7 . Sandwich
8 . Noodles
9 . Sushi
```

### Getting the order from the user:

```commandline
item_order = 0 # Keep track of user order

while item_order < 3:
    order_item = input("Enter the No. of the item you want: ")
    if order_item.isdigit():
        order_list.append(item_list[int(order_item)])
    item_order += 1

Output:
Enter the No. of the item you want: 8
Enter the No. of the item you want: 4
Enter the No. of the item you want: 2
['Sushi', 'Biryani', 'Fish and Chips']
```

### Displaying the order back to the customer
```commandline
print("Ordered Items:")
for i in range(len(order_list)):
    print(i + 1, ".", order_list[i])

Ordered Items:
1 . Biryani
2 . Enchiladas
3 . Fish and Chips
```