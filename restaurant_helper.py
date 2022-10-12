# User Stories
# 1 - AS a User I want to be able to see the menu in a formatted way, so that I can order my meal.

# 2 - AS a User I want to be able to order 3 times, and have my responses added to a list, so they aren't forgotten

# 3 - As a user, I want to have my order read back to me in formatted way, so I know what I ordered.

item_list = ["Burger", "Pizza", "Fish and Chips", "Pasta", "Biryani", "Enchiladas", "Sandwich", "Noodles", "Sushi"]

order_list = []

print("XYZ Restaurant")
print("Select an item from the list:")
for i in range(len(item_list)):
    print(i + 1, ".", item_list[i])

# Taking user order
item_order = 0 # Keep track of user order

while item_order < 3:
    order_item = input("Enter the No. of the item you want: ")
    if order_item.isdigit():
        order_list.append(item_list[int(order_item)])
    item_order += 1


print("Ordered Items:")
for i in range(len(order_list)):
    print(i + 1, ".", order_list[i])

#print(order_list)

