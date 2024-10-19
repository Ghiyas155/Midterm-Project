# Midterm-Project
We have a JSON file and two Python files that accept the existing JSON file as input and return client information such as phone number and name, as well as menu items, prices, and the number of orders received. 

customer.json is the output of the customer.py file, while items.json is the output of the items.py file.

Installation
1. Install Python3.3
2. Install Git and create an account. 
4. Make a Repository. 
5. Import the relevant libraries. 

Functionalities and Design Implementation


The customers.py file accepts example_orders.json as input. It goes to the main method and calls the function read_object() , which opens and returns a JSON file. The function extract_customer_data() is then called, and the required customer data is returned and stored in the variable customer_data(). Later, it generates a customer.json file and stores the customer's phone number and name in it.


The items.py file accepts example_orders.json as an input. Compiler enters the main method, calls read_orders(), and accesses the input json file. Then returns to the main method and calls the function process_items(), which returns items from the JSON file.The script verifies if each item in the sequence already exists in the items dictionary,  If not it adds the item with its price and resets the order count to one. If the item already exists, the order count for that item increases by one. After the compiler returns to the main procedure, it creates a JSON file that contains the order name, price, and number of orders.
And after compiler returns to main method and and creates json file that dumps order name, price and number of orders

 
Make sure all the files are in the same directory. 


After the execution of file 2 python files, customer.json and items.json is created on the same directory. 
