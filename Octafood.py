# Main
from Admin import *
from User import *
a1 = AdminFunctionality()
u1 = UserFunctionality()

print("")
print("1. Admin Functionality")
print("2. User Functionality")
print("")
try:
    user_option = int(input("Enter your choice to perform the above operation: "))
    
except: 
    print("")
    print("Only number(single digit) is allowed in the input.")
    print("")
else:
    if user_option==1:
        print("")
        print("1. Add new food")
        print("2. View food details")
        print("3. Edit food details")            
        print("4. Delete food item")
        print("")
        admin_ch = input("Enter your choice: ")
        if admin_ch=='1':
            a1.admin_add_new_food()
        elif admin_ch=='2':
            try:
                with open("admin_food_details.json", "r") as file:
                    a1.admin_food_details = json.load(file)	
            except:
                print("")
                print("You need to enter food details, to perform this operation")
                print("")
            else:
                if len(a1.admin_food_details)==0:
                    print("")
                    print("There are no items to view, add the items to perform this operation")
                    print("")
                else:
                    a1.admin_view_food_details()
        elif admin_ch=='3':
            try:
                with open("admin_food_details.json", "r") as file:
                    a1.admin_food_details = json.load(file)	
            except: 
                print("")
                print("You need to enter food details, to perform this operation")
                print("")
            else:
                if len(a1.admin_food_details)==0:
                    print("")
                    print("There are no items to edit, add the items to perform this operation")
                    print("")
                else:
                    a1.admin_edit_food_details()
        elif admin_ch=='4':
            try:
                with open("admin_food_details.json", "r") as file:
                    a1.admin_food_details = json.load(file)	
            except:
                print("")
                print("You need to enter food details, to perform this operation")
                print("")
            else:
                if len(a1.admin_food_details)==0:
                    print("")
                    print("There are no items to delete, add the items to perform this operation")
                    print("")
                else:
                    a1.admin_delete_food_details()
    elif user_option==2:
        print("")
        print("Welcome to Octafood")
        print("")
        print("1.Register")
        print("2.Login")
        print("")
        user_ch = input("Enter your choice: ")  
        if user_ch=='1':
            u1.user_signup()
        elif user_ch=='2':
            try:
                with open("user_signup_details.json", "r") as file:
                    u1.user_login_data = json.load(file)
            except:
                print("")
                print("You need to signup, to perform this operation")
                print("")
            else:
                if len(u1.user_login_data)==0:
                    print("You need to signup first, to login")
                else:
                    u1.user_login()  
        else: 
            print("You have entered an invalid option, please enter the correct option(1-2)")
            print("")
    else:
        print("You have entered an invalid key, please enter valid option(1-2)")
        print("")