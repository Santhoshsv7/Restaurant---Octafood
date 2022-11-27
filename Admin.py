# Admin
import json,random
class AdminFunctionality:
    def __init__(self):
        self.admin_food_item = {}
        self.admin_food_item_with_id = {}
    def admin_add_new_food(self):
        print("")
        # self.admin_food_count = int(input("Enter the number of food items you want to add: "))
        # for i in range(1,self.admin_food_count+1):
        print("")
        print("Enter the details of food: ")
        print("")
        with open("admin_food_details.json", "r") as file:
            self.admin_previous_food_data = json.load(file)
        self.admin_food_id =len(self.admin_previous_food_data)+1 # random.randint(1,100)# 
        # Since dictionary keys should be unique, I am not using random module here because random module will generate random number each time,
        try:
            self.admin_food_name = input("Enter the food name: ")
            self.admin_food_qty = float(input("Enter the food quantity in KG's or Units: "))
            self.admin_food_price =  float(input("Enter the price of the food for 1 KG or 1 Unit: ")) 
            self.admin_food_discount = float(input("Enter the discout amount for 1 KG or 1 Unit: "))
            self.admin_food_stock = int(input("Enter the count of stocks available: "))
        except:
            print("You have entered invalid details, please enter valid details.")
        else:
            self.admin_food_item = {"name":self.admin_food_name,
                                    "quantity":self.admin_food_qty,
                                    "price":self.admin_food_price,
                                    "discount":self.admin_food_discount,
                                    "stock":self.admin_food_stock}
            self.admin_food_item_with_id[self.admin_food_id] = self.admin_food_item
        with open("admin_food_details.json", "r") as file:
            self.admin_previous_food_data = json.load(file)
        self.admin_previous_food_data.update(self.admin_food_item_with_id)
        with open("admin_food_details.json","w") as f:
            json.dump(self.admin_previous_food_data,f)
        print("")
        print("Food details were added to the JSON file successfully!!!")
        print("")
    ''''''
    def admin_edit_food_details(self):
        print("")
        with open("admin_food_details.json","r") as p:
            self.admin_food_dict = json.load(p)
        print("Food id's available are: ",list(self.admin_food_dict.keys()))
        print("")
        self.admin_food_edit_id = input("Enter the food id you want edit: ")
        if self.admin_food_edit_id in self.admin_food_dict.keys():
        # for self.key in self.admin_food_dict.keys():
        #     if self.key==self.admin_food_edit_id:
            print("")
            print("1. Name updation")
            print("2. Quantity updation")
            print("3. Price updation")
            print("4. Discount updation")
            print("5. Stock updation")
            print("")
            self.admin_edit_option = input("Enter the option to perform the edit operation(1-4): ")
            if self.admin_edit_option=='1':
                print("")
                self.name_edit_value = input("Enter the new value for food name: ")                    
                print("")
                with open("admin_food_details.json", "r") as file:
                    self.admin_name_data = json.load(file)	
                    for self.key in self.admin_name_data.keys():
                        if self.key==self.admin_food_edit_id:
                            self.admin_name_data[self.key]['name']=self.name_edit_value
                            break
                with open("admin_food_details.json","w") as f:
                    json.dump(self.admin_name_data,f)
                print("Name has been updated successfully")
                print("")
            elif self.admin_edit_option=='2':
                print("")
                self.quantity_edit_value = float(input("Enter the new value for quantity(for 1 KG or 1 Unit): "))
                print("")
                with open("admin_food_details.json", "r") as file:
                    self.admin_quantity_data = json.load(file)	
                    for self.key in self.admin_quantity_data.keys():
                        if self.key==self.admin_food_edit_id:
                            self.admin_quantity_data[self.key]['quantity']=self.quantity_edit_value
                            break
                with open("admin_food_details.json","w") as f:
                    json.dump(self.admin_quantity_data,f)
                print("Quantity has been updated successfully")
                print("")
            elif self.admin_edit_option=='3':
                print("")
                self.price_edit_value = float(input("Enter the new value for price(for 1 KG or 1 Unit): "))
                print("")
                with open("admin_food_details.json", "r") as file:
                    self.admin_price_data = json.load(file)	
                    for self.key in self.admin_price_data.keys():
                        if self.key==self.admin_food_edit_id:
                            self.admin_price_data[self.key]['price']=self.price_edit_value
                            break
                with open("admin_food_details.json","w") as f:
                    json.dump(self.admin_price_data,f)
                print("Price has been updated successfully")
                print("")
            elif self.admin_edit_option=='4':
                print("")
                self.discount_edit_value = float(input("Enter the new value for discount(for 1 KG or 1 Unit): "))
                print("")
                with open("admin_food_details.json", "r") as file:
                    self.admin_discount_data = json.load(file)	
                    for self.key in self.admin_discount_data.keys():
                        if self.key==self.admin_food_edit_id:
                            self.admin_discount_data[self.key]['discount']=self.discount_edit_value
                            break
                with open("admin_food_details.json","w") as f:
                    json.dump(self.admin_discount_data,f)
                print("Discount has been updated successfully")
                print("")
            elif self.admin_edit_option=='5':
                print("")
                self.stock_edit_value = int(input("Enter the new value for stock: "))
                print("")
                with open("admin_food_details.json", "r") as file:
                    self.admin_stock_data = json.load(file)	# get data from file
                    for self.key in self.admin_stock_data.keys():
                        if self.key==self.admin_food_edit_id:
                            self.admin_stock_data[self.key]['stock']=self.stock_edit_value
                            break
                with open("admin_food_details.json","w") as f:
                    json.dump(self.admin_stock_data,f)
                print("Stock has been updated successfully")
                print("")
        else:
            print("")
            print("Entered ID is not present")   
            print("")
            
    ''''''
    def admin_view_food_details(self):
        print("")
        with open("admin_food_details.json","r") as p:
            self.admin_food_dict = json.load(p)
        print("Food id's available are: ",list(self.admin_food_dict.keys()))
        print("")
        self.admin_food_view_id = input("Enter the food id you want to view: ")
        print("")
        if self.admin_food_view_id in self.admin_food_dict.keys():
            print("Item details: ",self.admin_food_dict[self.admin_food_view_id])
        else:
            print("Entered ID is not present")
        print("")
    ''''''
    def admin_delete_food_details(self):
        print("")
        with open("admin_food_details.json","r") as p:
            self.admin_food_dict = json.load(p)
        print("Food id's available are: ",list(self.admin_food_dict.keys()))
        print("")
        try: 
            self.admin_delete_food_id = input("Enter the food id you want to delete: ")
            with open("admin_food_details.json") as f:
                self.delete_dict = json.load(f)
            del self.delete_dict[self.admin_delete_food_id] 
            with open("admin_food_details.json", "w") as f:
                json.dump(self.delete_dict, f)
            print("")
            print("Item with id",self.admin_delete_food_id,"is deleted successfully")
            print("")
        except KeyError:
            print("")
            print("Entered item with id",self.admin_delete_food_id,"is not present in the food list")
            print("")
        except:
            print("")
            print("Please enter valid input")
            print("")