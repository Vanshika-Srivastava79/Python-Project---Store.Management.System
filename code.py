import mysql.connector as myq
import time
from datetime import date
 
# To Create database If Not Present
sql_password = input("Enter Your Mysql Password:")
conn_database = myq.connect(host='localhost', user='root', password=sql_password)
db_database = conn_database.cursor()
db_database.execute("show databases")
lst_database = db_database.fetchall()
if ('store',) not in lst_database:
    db_database.execute("create database store")
print("==============================================")
print("           Welcome To Our Store")
print("==============================================")
con = myq.connect(host='localhost', user='root', password=sql_password, database='store')
# To Create Tables If Not Present
db_table = con.cursor()
db_table.execute("show tables")
lst = db_table.fetchall()
if ('employees',) not in lst:
    db_table.execute(
        "create table employees(USER_ID varchar(50) primary key,password varchar(50),Date_Of_Birth date, Date_Of_Joining date, Gender varchar(8))")
if ('stock',) not in lst:
    db_table.execute(
        "create table stock(product_id integer primary key,product_name varchar(50),cost integer,description varchar(100))")
if ('list',) not in lst:
    db_table.execute(
        "create table list(product_id integer primary key,product_name varchar(50),cost integer,quantity integer,total integer)")
 
# Program Starts From Here
while True:
    print("\n")
    print("==============================================")
    print("|                  MAIN MENU                 |")
    print("==============================================")
    Customer_or_Employee = int(input(
        'Press 1 If You Are A Customer\nPress 2 If You Are An Employee\nPress 3 If You Are Manager\nPress 4 to Exit\n==>'))
    print("==============================================")
    print("\n")
    # ===Employee============================================================================
    if Customer_or_Employee == 2:
        # Login Credentials Input
        while True:
            print("\n")
            print("==============================================")
            print("|                  LOGIN                     |")
            print("==============================================")
            print("\n")
            User_Id = input("User ID:")
            Pass = input("Password:")
            Password = ("('" + Pass + "',)")
            Employee_cursor_login = con.cursor()
            Employee_cursor_login.execute("select password from employees where USER_ID='{}'".format(User_Id))
            password_check = str(Employee_cursor_login.fetchone())
            if password_check == Password:
                print("Correct Password")
                while True:
                    # Employee Work Starts From Here
                    print("\n")
                    print("==============================================")
                    Employee_Menu = int(input(
                        'Press 1 If You Want To ADD An Item To The Stock Data\nPress 2 If You Want To Modify An Item In The Stock Data\nPress 3 If You Want To Delete An Item From The Stock Data\nPress 4 If You Want To Check The Stock Data\nPress 5 If You Want To Change Your Password\nPress 6 If You Want To Exit\n==>'))
                    print("==============================================")
                    print("\n")
                    if Employee_Menu == 1:  # for adding an item
                        while True:
                            employee_cursor_add = con.cursor()
                            employee_product_id = int(input("Enter the product id:"))
                            employee_product_name = input("Enter the product name:")
                            employee_product_cost = int(input("Enter the product cost:"))
                            employee_product_description = input("Enter the product description:")
                            employee_query_add = "insert into stock values({},'{}',{},'{}')".format(employee_product_id,
                                                                                                    employee_product_name,
                                                                                                    employee_product_cost,
                                                                                                    employee_product_description)
                            employee_cursor_add.execute(employee_query_add)
                            con.commit()
                            print("Product Added Successfully")
                            ask_add = int(
                                input('Press 1 if u want to ADD more items\npress 2 if you want to exit\n==>'))
                            if ask_add == 2:
                                break
                    elif Employee_Menu == 2:  # for modifying an item
                        employee_modify_id = int(input("Enter Product Id:"))
                        employee_modify_option = int(input(
                            'Press 1 if you want to change the Product Name\nPress 2 if you want to change the Product Cost\nPress 3 if you want to change the Product Description\n==>'))
                        if employee_modify_option == 1:
                            employee_cursor_modify_name = con.cursor()
                            employee_new_name = input("Enter the new name:")
                            employee_modify_name_query = "update stock set product_name='{}' where product_id={}".format(
                                employee_new_name, employee_modify_id)
                            employee_cursor_modify_name.execute(employee_modify_name_query)
                            con.commit()
                            print("Product Updated Successfully..")
                        elif employee_modify_option == 2:
                            employee_cursor_modify_cost = con.cursor()
                            employee_new_cost = input("Enter the new cost:")
                            employee_modify_cost_query = "update stock set cost={} where product_id={}".format(
                                employee_new_cost, employee_modify_id)
                            employee_cursor_modify_cost.execute(employee_modify_cost_query)
                            con.commit()
                            print("Product Updated Successfully..")
                        elif employee_modify_option == 3:
                            employee_cursor_modify_description = con.cursor()
                            employee_new_description = input("Enter the new description:")
                            employee_modify_description_query = "update stock set description='{}' where product_id={}".format(
                                employee_new_description, employee_modify_id)
                            employee_cursor_modify_description.execute(employee_modify_description_query)
                            con.commit()
                            print("Product Updated Successfully..")
                        else:
                            Invalid_Option = "Invalid Option...\n"
                            for i in Invalid_Option:
                                time.sleep(0.01)
                                print(i, end='')
 
                    elif Employee_Menu == 5:
                        while True:
                            employee_modify_pass = input("Enter The Previous Password:")
                            employee_modify_password = ("('" + employee_modify_pass + "',)")
                            employee_cursor_modify = con.cursor()
                            employee_cursor_modify.execute(
                                "select password from employees where USER_ID='{}'".format(User_Id))
                            password_modify_check = str(employee_cursor_modify.fetchone())
                            if password_modify_check == employee_modify_password:
                                new_password_input = input("Enter The New Password:")
                                employee_modify_password_query = "update employees set password={} where USER_ID='{}'".format(
                                    new_password_input, User_Id)
                                employee_cursor_modify.execute(employee_modify_password_query)
                                con.commit()
                                print("Password Changed Successfully..")
                                break
                            else:
                                print("Incorrect Password")
                    elif Employee_Menu == 3:  # for deleting an item
                        employee_cursor_delete = con.cursor()
                        employee_delete = int(input("Enter the product id:"))
                        employee_delete_query = "delete from stock where product_id={}".format(employee_delete)
                        employee_cursor_delete.execute(employee_delete_query)
                        con.commit()
                        print("Product Deleted Successfully..")
 
                    elif Employee_Menu == 4:  # for displaying stock
                        print("\n")
                        print("==============================================")
                        print("|                  STORE                     |")
                        print("==============================================")
                        print("(ID, NAME, COST, DESCRIPTION)")
                        employee_cursor_show = con.cursor()
                        employee_cursor_show.execute("select product_id,product_name,cost,Description FROM stock")
                        employee_result = employee_cursor_show.fetchall()
                        for employee_row in employee_result:
                            print(employee_row)
                        print("==============================================")
                        print("\n")
 
                    elif Employee_Menu == 6:
                        break  # To break Employee Menu While Statement
                    else:
                        Invalid_Option = "Invalid Option...\n"
                        for i in Invalid_Option:
                            time.sleep(0.01)
                            print(i, end='')
                break  # To break Correct Password while statement(If yeh nhi hota then it will ask id pw again on exit)
            else:
                print("Incorrect User ID or Password")
    # ===Customer============================================================================
    elif Customer_or_Employee == 1:
        # fetching item from stock table
        print("\n")
        print("==============================================")
        print("|                  STORE                     |")
        print("==============================================")
        print("(ID, NAME, COST)")
        employee_cursor_show = con.cursor()
        employee_cursor_show.execute("select product_id,product_name,cost FROM stock")
        employee_result = employee_cursor_show.fetchall()
        for employee_row in employee_result:
            print(employee_row)
        print("These Are The Items Available In Our Store")
        print("==============================================")
        print("\n")
        while True:
            print("\n")
            print("==============================================")
            Customer_Menu = int(input(
                'Press 1 If You Want To ADD an item to your list\npress 2 if u want to delete an item from your list\npress 3 if you want to check your list\npress 4 if you want to clear your list\npress 5 if u want to check the store again\npress 6 if u want to check details of an item\npress 7 if you want to exit\n==>'))
            print("==============================================")
            print("\n")
            if Customer_Menu == 1:
                while True:
                    customer_cursor_add = con.cursor()
                    customer_ask_product_id = int(
                        input("Enter the Product id of the item of which u want to add in your list:"))
                    customer_ask_product_quantity = int(input("Enter the Quantity:"))
                    customer_list_add_query_1 = "insert into list select product_id,product_name,cost,NULL,NULL from stock where product_id={}".format(
                        customer_ask_product_id)
                    customer_list_add_query_2 = "update list set quantity={} where product_id={}".format(
                        customer_ask_product_quantity, customer_ask_product_id)
                    customer_cursor_add.execute(customer_list_add_query_1)
                    customer_cursor_add.execute(customer_list_add_query_2)
                    customer_cursor_add.execute("select cost*quantity from list where product_id={}".format(customer_ask_product_id))
                    total_0=customer_cursor_add.fetchall()
                    for total_1 in total_0:
                        for total_2 in total_1:
                            customer_cursor_add.execute("update list set total={} where product_id={}".format(total_2,customer_ask_product_id))
                    con.commit()
                    print("Item Added Successfully")
                    customer_ask_add_again = int(input("Press 1 To Add More Items\nPress 2 To Exit\n==>"))
                    if customer_ask_add_again == 2:
                        break
            elif Customer_Menu == 2:  # for deleting an item
                customer_cursor_delete = con.cursor()
                customer_delete = int(input("Enter the product id:"))
                customer_delete_query = "delete from list where product_id={}".format(customer_delete)
                customer_cursor_delete.execute(customer_delete_query)
                con.commit()
                print("Item Deleted Successfully..")
            elif Customer_Menu == 4:
                customer_cursor_clear = con.cursor()
                customer_clear_query = "Delete from List"
                customer_cursor_clear.execute(customer_clear_query)
                con.commit()
                print("List cleared Successfully")
            elif Customer_Menu == 3:
                print("\n")
                print("==============================================")
                print("                  LIST")
                print("==============================================")
                print("(ID|NAME|COST|QTY|TOTAL)")
                customer_cursor_show = con.cursor()
                customer_cursor_show.execute("select * FROM list")
                customer_result = customer_cursor_show.fetchall()
                for customer_row in customer_result:
                    print(customer_row)
                print("==============================================")
                show_total_0=0
                customer_cursor_show.execute("select total FROM list")
                show_total_1=customer_cursor_show.fetchall()
                for show_total_a in show_total_1:
                    for show_total_b in show_total_a:
                        show_total_0 = show_total_0 + show_total_b
                print("Your Total Is:",show_total_0)
                print("==============================================")
                print("\n")
            elif Customer_Menu == 7:
                break
            elif Customer_Menu == 5:
                print("\n")
                print("==============================================")
                print("                  STORE")
                print("==============================================")
                print("(ID, NAME, COST)")
                employee_cursor_show = con.cursor()
                employee_cursor_show.execute("select product_id,product_name,cost FROM stock")
                employee_result = employee_cursor_show.fetchall()
                for employee_row in employee_result:
                    print(employee_row)
                print("These Are The Items Available In Our Store")
                print("==============================================")
                print("\n")
            elif Customer_Menu == 6:
                customer_item_details_input = int(input("Enter The Product Id Of The Item:"))
                print("\n")
                print("==============================================")
                print("                  PRODUCT DETAILS")
                print("==============================================")
                customer_item_details_show = con.cursor()
                customer_item_details_show.execute(
                    "select product_id FROM stock where product_id={}".format(customer_item_details_input))
                customer_item_details_show_id_0 = customer_item_details_show.fetchone()
                for customer_item_details_show_id_1 in customer_item_details_show_id_0:
                    print("Product Id:", str(customer_item_details_show_id_1))
                customer_item_details_show.execute(
                    "select product_name FROM stock where product_id={}".format(customer_item_details_input))
                customer_item_details_show_name_0 = customer_item_details_show.fetchone()
                for customer_item_details_show_name_1 in customer_item_details_show_name_0:
                    print("Product Name:", str(customer_item_details_show_name_1))
                customer_item_details_show.execute(
                    "select cost FROM stock where product_id={}".format(customer_item_details_input))
                customer_item_details_show_cost_0 = customer_item_details_show.fetchone()
                for customer_item_details_show_cost_1 in customer_item_details_show_cost_0:
                    print("Product Cost:", str(customer_item_details_show_cost_1))
                customer_item_details_show.execute(
                    "select description FROM stock where product_id={}".format(customer_item_details_input))
                customer_item_details_show_description_0 = customer_item_details_show.fetchone()
                for customer_item_details_show_description_1 in customer_item_details_show_description_0:
                    print("Product Description:", str(customer_item_details_show_description_1))
                print("==============================================")
                print("\n")
            else:
                Invalid_Option = "Invalid Option...\n"
                for i in Invalid_Option:
                    time.sleep(0.01)
                    print(i, end='')
# ===Manager============================================================================
    elif Customer_or_Employee == 3:
        while True:
            Manager_Password = input("Enter The Key:")
            if Manager_Password == "12345":
                while True:
                    print("\n")
                    print("==============================================")
                    Staff_Menu = int(input(
                        "Press 1 If You Want To Add A Staff Member\nPress 2 If You Want To Change Any Member's Records\nPress 3 If You Want To Delete Any Member From Records\nPress 4 If You Want To Check The Staff List\nPress 5 If You Want To Check ID card of an employee\nPress 6 If You Want To Exit\n==>"))
                    print("==============================================")
                    print("\n")
                    if Staff_Menu == 1:  # for adding an item
                        while True:
                            staff_cursor_add = con.cursor()
                            staff_product_id = (input("Enter the User Id:"))
                            staff_product_password = input("Create a Password:")
                            staff_product_dob = input("Enter The Date Of Birth(yyyy/mm/dd):")
                            staff_product_doj = input("Enter The Date Of Joining(yyyy/mm/dd):")
                            staff_product_gender = input("Enter The Gender:")
                            staff_query_add = "insert into employees values('{}','{}','{}','{}','{}')".format(
                                staff_product_id, staff_product_password, staff_product_dob, staff_product_doj,
                                staff_product_gender)
                            staff_cursor_add.execute(staff_query_add)
                            con.commit()
                            print("Credentials Added Successfully")
                            ask_add = int(input('Press 1 if u want to add more\npress 2 if you want to exit\n==>'))
                            if ask_add == 2:
                                break
                    elif Staff_Menu == 2:  # for modifying an item
                        staff_modify_id = (input("Enter User Id:"))
                        while True:
                            staff_modify_ask = int(input(
                                "Press 1 If You Want To change Password\nPress 2 If You Want To change DOB\nPress 3 If You want To Change Date Of Joining\nPress 4 If You Want To change Gender\n==>"))
                            staff_cursor_modify = con.cursor()
                            if staff_modify_ask == 1:
                                staff_new_password = input("Enter the new password:")
                                staff_modify_password_query = "update employees set password='{}' where USER_ID='{}'".format(
                                    staff_new_password, staff_modify_id)
                                staff_cursor_modify.execute(staff_modify_password_query)
                                con.commit()
                                print("Updated Successfully..")
                                break
                            if staff_modify_ask == 2:
                                staff_new_DOB = input("Enter the new Date Of Birth:")
                                staff_modify_DOB_query = "update employees set Date_Of_Birth='{}' where USER_ID='{}'".format(
                                    staff_new_DOB, staff_modify_id)
                                staff_cursor_modify.execute(staff_modify_DOB_query)
                                con.commit()
                                print("Updated Successfully..")
                                break
                            if staff_modify_ask == 3:
                                staff_new_DOJ = input("Enter the new Date Of Joining:")
                                staff_modify_DOJ_query = "update employees set Date_Of_Joining='{}' where USER_ID='{}'".format(
                                    staff_new_DOJ, staff_modify_id)
                                staff_cursor_modify.execute(staff_modify_DOJ_query)
                                con.commit()
                                print("Updated Successfully..")
                                break
                            if staff_modify_ask == 4:
                                staff_new_Gen = input("Enter the Gender:")
                                staff_modify_Gen_query = "update employees set Gender='{}' where USER_ID='{}'".format(
                                    staff_new_Gen, staff_modify_id)
                                staff_cursor_modify.execute(staff_modify_Gen_query)
                                con.commit()
                                print("Updated Successfully..")
                                break
                            else:
                                Invalid_Option = "Invalid Option...\n"
                                for i in Invalid_Option:
                                    time.sleep(0.01)
                                    print(i, end='')
                    elif Staff_Menu == 3:  # for deleting an item
                        Staff_cursor_delete = con.cursor()
                        Staff_delete = (input("Enter the user id:"))
                        Staff_delete_query = "delete from employees where USER_ID='{}'".format(Staff_delete)
                        Staff_cursor_delete.execute(Staff_delete_query)
                        con.commit()
                        print("Record Deleted Successfully..")
 
                    elif Staff_Menu == 4:
                        print("\n")
                        print("==============================================")
                        print("                   Staff")
                        print("==============================================")
                        print("(User_ID, Password)")
                        staff_cursor_show = con.cursor()
                        staff_cursor_show.execute("select USER_ID,password FROM employees")
                        staff_result = staff_cursor_show.fetchall()
                        for staff_row in staff_result:
                            print(staff_row)
                        print("==============================================")
                        print("\n")
 
                    elif Staff_Menu == 5:
                        ID_USER = input("Enter The User Id:")
                        print("\n")
                        print("==============================================")
                        print("                   ID CARD")
                        print("==============================================")
                        employee_details_show = con.cursor()
                        employee_details_show.execute(
                            "select USER_ID FROM employees where USER_ID='{}'".format(ID_USER))
                        employee_details_show_ID_0 = employee_details_show.fetchone()
                        for employee_details_show_ID_1 in employee_details_show_ID_0:
                            print("User ID:", employee_details_show_ID_1,)
                            employee_details_show.execute(
                            "select Date_Of_Birth FROM employees where USER_ID='{}'".format(ID_USER))
                        employee_details_show_DOB_0 = employee_details_show.fetchone()
                        for employee_details_show_DOB_1 in employee_details_show_DOB_0:
                            print("Date Of Birth:", employee_details_show_DOB_1)
                        today = date.today()
                        print("Age:", today.year - employee_details_show_DOB_1.year - ((today.month, today.day) < (
                        employee_details_show_DOB_1.month, employee_details_show_DOB_1.day)))
                        employee_details_show.execute(
                            "select Date_Of_Joining FROM employees where USER_ID='{}'".format(ID_USER))
                        employee_details_show_DOJ_0 = employee_details_show.fetchone()
                        for employee_details_show_DOJ_1 in employee_details_show_DOJ_0:
                            print("Date Of Joining:", employee_details_show_DOJ_1)
                        employee_details_show.execute("select Gender FROM employees where USER_ID='{}'".format(ID_USER))
                        employee_details_show_gender_0 = employee_details_show.fetchone()
                        for employee_details_show_gender_1 in employee_details_show_gender_0:
                            print("Gender:", employee_details_show_gender_1)
                        print("==============================================")
                        print("\n")
 
                    elif Staff_Menu == 6:
                        break
                    else:
                        Invalid_Option = "Invalid Option...\n"
                        for i in Invalid_Option:
                            time.sleep(0.01)
                            print(i, end='')
                break  # key ka break
            else:
                print("Incorrect Key")
    # ===Others==============================================================================
    elif Customer_or_Employee == 4:
        break
    else:
        Invalid_Option = "Invalid Option...\n"
        for i in Invalid_Option:
            time.sleep(0.01)
            print(i, end='')
 
