w = 4
class Inventory:
     database =  {}
         
     def add_item(self, item_id, item_name, stock_count, price):
         
         self.database[item_id] = {   #The square bracket defines the data in it to be a key
               "Item_name": item_name,
               "Stock_count": stock_count,
               "Price" : price 
         } #the database is the main dictionary and the item_id is a key in it,the dictionary connected to the item_id acts as the value to the key  
     def update_item(self, field, item_id):
        self.database[item_id].update(field)

     def check_item_details(self, id):
        return self.database[id]

    