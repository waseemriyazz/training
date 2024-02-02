class Inventory:
    def __init__(self):
        self.item_details = {}

    def add_item(self, item_id, item_name, stock_count, price):
        if item_id not in self.item_details:
            self.item_details[item_id] = {
                'item_name': item_name,
                'stock_count': stock_count,
                'price': price
            }
        else:
            self.item_details[item_id]['stock_count'] += stock_count


    def update_item(self, item_id, stock_count, price):
        if item_id in self.item_details:
            self.item_details[item_id]['stock_count'] = stock_count
            self.item_details[item_id]['price'] = price
            print(f"Item with ID {item_id} updated successfully.")
        else:
            print(f"Item with ID {item_id} not found in inventory.")

    def check_item_details(self, item_id):
        if item_id in self.item_details:
            return self.item_details[item_id]
        else:
            print(f"Item with ID {item_id} not found in inventory.")
            return None
        

inventory = Inventory()

inventory.add_item(1, 'Apple', 100, 2.50)
inventory.add_item(2, 'Banana', 150, 1.75)

inventory.update_item(1, 90, 2.75)
inventory.update_item(3, 90, 2.75)  
  