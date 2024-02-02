# # 7.Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.

# # Perform the following tasks now:
# # Now add items to the menu.
# # Make table reservations.
# # Take customer orders.
# # Print the menu.
# # Print table reservations.
# # Print customer orders.
# # Note: Use dictionaries and lists to store the data.

# class Restaurant :
    
#     menu = [] 
#     booked_table = {} 
#     customer_orders = []
#     def __init__(self):
#         pass
#     @classmethod
#     def add_order(cls, order):
#         if order in cls.menu:

#             cls.customer_orders.append(order)
#         else:
#             print("Sorry! Item not available.")
#     @classmethod
#     def add_item_to_menu(cls, item):

#         if item not in cls.menu:
#             cls.menu.append(item)
#     @classmethod
#     def add_reservation(cls, table_number, reservation_status):
#             if cls.booked_table[table_number] == True:
#                  print("table not available")
#             else:
#                 cls.booked_table[table_number] = reservation_status
    

    
# myrestaurant = Restaurant()
# myrestaurant.add_item_to_menu("bread")
# myrestaurant.add_order("water")
# myrestaurant.add_order("bread")
# myrestaurant.add_reservation(1, True)
# myrestaurant.add_reservation(1, True)

# print(myrestaurant.menu)



class Restaurant:
    menu = []
    booked_table = {key: False for key in range(1, 11)}
    customer_orders = []

    @classmethod
    def add_order(cls, order):
        if order in cls.menu:
            cls.customer_orders.append(order)
            print("order_placed")
        else:
            print("Sorry! Item not available.")

    @classmethod
    def add_item_to_menu(cls, item):
        if item not in cls.menu:
            cls.menu.append(item)

    @classmethod
    def add_reservation(cls, table_number, reservation_status):
        if table_number in cls.booked_table:
            if cls.booked_table[table_number] == False:  # Check if the table is available
                cls.booked_table[table_number] = reservation_status
            else:
                print("Table not available.")
        else:
            print("Table does not exist.")

myrestaurant = Restaurant()
myrestaurant.add_item_to_menu("bread")
myrestaurant.add_order("water")
myrestaurant.add_order("bread")
myrestaurant.add_reservation(1, True)
myrestaurant.add_reservation(1, True)
print(myrestaurant.menu)