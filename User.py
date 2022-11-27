# User login
import json
from Admin import *
class UserFunctionality:
    def __init__(self):
        self.user_signup_dict = {}
        self.user_signup_dict_with_id = {}
    def user_signup(self):
        print("")
        '''Users will be added based on their id's(automatically generated) - Since dictionary takes key value pair'''
        self.user_id = len(self.user_signup_dict_with_id)+1
        print("Please enter your details,")
        print("")
        try:
            self.user_name = input("Enter your full name: ")
            self.user_phone_number = int(input("Enter your phone number(10 digits): "))
            self.user_email = input("Enter your email id: ")
            self.user_address = input("Enter your full address: ")
            self.user_password = input("Enter your password: ")
        except:
            print("")
            print("You have entered invalid details")
            print("")
        else:
            self.user_dict = {
                                "name":self.user_name,
                                "phone":self.user_phone_number,
                                "email":self.user_email,
                                "address":self.user_address,
                                "password":self.user_password
                            }
            self.user_signup_dict_with_id[self.user_id]=self.user_dict
            with open("user_signup_details.json","w") as f:
                    json.dump(self.user_signup_dict_with_id,f)
            print("")
            print("Dear",self.user_name,", you have signed up successfully")
            print("")
    def user_profile_updation(self):
        print("")
        self.user_email_id = input("Enter your email id to update the profile: ")
        print("")
        with open("user_signup_details.json", "r") as file:
            self.user_profile_updation_data = json.load(file)	# get data from file
        for self.key in self.user_profile_updation_data.keys():
            if self.user_profile_updation_data[self.key]['email']==self.user_email_id:
                print("1. Change name")
                print("2. Change phone number")
                print("3. Change email id")
                print("4. Change address")
                print("5. Change password")
                print("")
                self.user_specific_choice = input("Enter your choice to perform the above operations(1-5): ")
                print("")
                if self.user_specific_choice=='1':
                    self.new_username = input("Enter new name: ")
                    self.user_profile_updation_data[self.key]['name'] = self.new_username
                    with open("user_signup_details.json","w") as f:
                        json.dump(self.user_profile_updation_data,f)
                    print("")
                    print("Name has been updated successfully")
                elif self.user_specific_choice=='2':
                    self.new_phone_number = input("Enter new phone number: ")
                    self.user_profile_updation_data[self.key]['phone'] = self.new_phone_number
                    with open("user_signup_details.json","w") as f:
                        json.dump(self.user_profile_updation_data,f)
                    print("")
                    print("Phone number has been updated successfully")
                elif self.user_specific_choice=='3':
                    self.new_email_id = input("Enter new email id: ")
                    self.user_profile_updation_data[self.key]['email'] = self.new_email_id
                    with open("user_signup_details.json","w") as f:
                        json.dump(self.user_profile_updation_data,f)
                    print("")
                    print("Email id has been updated successfully") 
                elif self.user_specific_choice=='4':
                    self.new_address = input("Enter new address: ")
                    self.user_profile_updation_data[self.key]['address'] = self.new_address
                    with open("user_signup_details.json","w") as f:
                        json.dump(self.user_profile_updation_data,f)
                    print("")
                    print("Address has been updated successfully") 
                elif self.user_specific_choice=='5':
                    self.new_password = input("Enter new password: ")
                    self.user_profile_updation_data[self.key]['password'] = self.new_password
                    with open("user_signup_details.json","w") as f:
                        json.dump(self.user_profile_updation_data,f)
                    print("")
                    print("Password has been updated successfully") 
            else:
                print("There is no name available as",self.user_name)
    def user_place_new_order(self):
        print("")
        with open("admin_food_details.json","r") as p:
            self.admin_food_dict = json.load(p)
        print("Menu: ")
        for self.key, self.value in self.admin_food_dict.items():
            print("Food Id: ",self.key,",","Details: ",self.value)
        print("")
        print("Food id's available are: ",list(self.admin_food_dict.keys()))
        print("")
        self.user_order_id = input("Enter the food id's you want to order(Enter comma separated values like 1,2,3): ")
        self.user_order_list = self.user_order_id.split(',')
        print("")
        print("Selected item are: ",self.user_order_list)
        print("")
        print("press 'y/Y' to place order")
        print("press 'n/N' to discard")
        print("")
        self.order_yes_or_no = input("Enter your choice: ").lower()
        print("")
        if self.order_yes_or_no=='y':
            print("")
            self.user_order_history = {}
            for self.key in self.admin_food_dict.keys():
                i = 0
                while(i<len(self.user_order_list)):
                    if self.key == self.user_order_list[i]:
                        self.user_order_history[self.key]=self.admin_food_dict[self.key]
                        with open("user_ordered_food_details.json","w") as f:
                                json.dump(self.user_order_history,f)
                    else:
                        pass
                    i = i+1         
            with open("user_ordered_food_details.json", "r") as file:
                self.order = json.load(file)
            print("Your order details: ",self.order)        
            print("")
            print("Your order has been recieved successfully")    
            print("")
        elif self.order_yes_or_no=='n':
            pass
        else:
            print("You've pressed invalid key")
            print("")
    def user_login_3_options(self):
        print("1. Place new order")
        print("2. Order history")
        print("3. Update profile")
        print("")
        self.user_choice = input("Enter your choice to perform the task: ")
        if(self.user_choice=='1'):
            with open("admin_food_details.json","r") as p:
                self.admin_food_dict = json.load(p)
            if len(self.admin_food_dict) == 0:
                print("")
                print("There are no food items to order")
            else:
                self.user_place_new_order()
        elif(self.user_choice=='2'):
            with open("user_ordered_food_details.json", "r") as file:
                self.order = json.load(file)
                print("")
                print("Your order history is: ",self.order)
        elif(self.user_choice=='3'):
            self.user_profile_updation()
    def user_login(self):
        print("")
        print("Please enter your login credentials,")
        print("")
        self.user_entery_email = input("Enter your email id: ")
        self.user_entry_password = input("Enter your password: ")
        with open("user_signup_details.json", "r") as file:
            self.user_login_data = json.load(file)	
        for self.key in self.user_login_data.keys():
            if self.user_login_data[self.key]["email"]==self.user_entery_email and self.user_login_data[self.key]["password"]==self.user_entry_password:
                print("")
                print("You have logged in successfully!")
                print("")
                self.user_login_3_options()
            else:
                print("")
                print("You have entered wrong login details")
                print("")
        print("")