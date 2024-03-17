
class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.book_table =  []
        self.customer_orders = []

    def add_item_to_menu(self, item, price):
        self.menu_items[item]= price
      
        
    
    def book_tables(self, customer_name, table_no):
        self.book_table.append([customer_name, table_no])

    def customer_order(self, table_No, Order ):
        order_details = {"table_no": table_No, "Order": Order}
        self.customer_orders.append(order_details)

    def print_menu(self):
        for item, price in self.menu_items.items():
            print("{}: {}".format(item, price))
                 

    def print_table_reservations(self):
        for customer in self.book_table:
            print("Name: ", customer["customer_name"])
            print("table_no: ", customer["table_no"] )
    
    def print_customer_orders(self):
        for order in self.customer_orders:
            print("Table {} : {}".format(order['table_no'], order['Order']))

restaurant = Restaurant()

restaurant.add_item_to_menu("Cheeseburger", 9.99)
restaurant.add_item_to_menu("Pepper Soup", 8)
restaurant.add_item_to_menu("Jollof rice & Chicken combo", 19.99)
restaurant.add_item_to_menu("Pizza", 3.99)
restaurant.add_item_to_menu("Shawarma:", 15)

restaurant.print_menu()
"""
restaurant.book_tables("Mark", 1)
restaurant.book_tables("Amy", 2)
restaurant.book_tables("Ruby", 3)

restaurant.customer_order(1, "Cheeseburger")
restaurant.customer_order(1, "Pepper Soup")
restaurant.customer_order(2, "Fish & Chips")
restaurant.customer_order(2, "Shawarma")

print("\nPopular dishes in the restaurant along with their prices:")
restaurant.print_menu()
print("\nTable reserved in the Restaurant:")
restaurant.print_table_reservations()
print("\nPrint customer orders:")
restaurant.print_customer_orders()
"""

   