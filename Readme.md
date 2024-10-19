# Midterm-Project
IS601 Web systems Mid term project 
Summary
We have a Json file and 2 python files which takes the existing Json file as an input and gives out customer details like name and phone number, and also gives information about the menu items,price and number of orders we got. 

Customer.json file is the output of customer.py file and items.json file is output of items.py file.
 
Installation
1. Install Python3.3
2. Install GIt
3. Create an account
4. Make a Repositories
5. Import required libraries

Functionalities and design implementation


Customers.py file takes example_orders.json as input. It goe to the main method and calls the function read_object(), which opens a Json file and returns Json file. Then calls the function extract_customer_data() which returns required customer data and stores it in the variable customer_data(). Later it creates a customer.json file and dumps the customer name and phone number into it. 


The items.py file takes example_orders.json as input. Compiler goes into main method and calls read_orders() and opens the input json file. Then returns back to the main method and calls the function process_items() which returns items of the json fileFor each item in an order, the script checks if the item is already in the items dictionary: If not, it adds the item with its price and initializes the order count to 1. If the item already exists, it increments the order count for that item by 1.
 And after compiler returns to main method and and creates json file that dumps order name, price and number of orders

 
Make sure all the files are in the same directory. 


After the execution of file 2 python files, customer.json and items.json is created on the same directory. 
