# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Daniel White,12.03.21,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
file_name_str = 'products.txt'
list_of_product_objects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Daniel White,12.07.21,Modified code to complete assignment 8
    """

    # TODO: Add Code to the Product class
    def __init__(self, product_name, product_price):
            self.__product_name = str(product_name)
            self.__product_price = float(product_price)


    @property
    def product_name(self):
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, value):
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Names are not Numbers!")

    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        if str(value).isnumeric() == True:
            self.__product_price = float(value)
        else:
            raise Exception("Price must be a Number!")

    def to_string(self):
        return self.__str__()

    def __str__(self):
        return self.product_name + "," + str(self.product_price)
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Daniel White,12.07.21,Modified code to complete assignment 8
    """
    pass
    # TODO: Add Code to process data from a file
    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        try:
            list_of_rows.clear()
            file = open(file_name, "r")
            for line in file:
                data = line.split(",")
                row = Product(data[0], float(data[1]))
                list_of_rows.append(row)
            file.close()
        except Exception as e:
            print(e)
            return list_of_rows

    # TODO: Add Code to process data to a file
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        file = open(file_name, "w")
        for row in list_of_product_objects:
            file.write(row.__str__() + "\n")
        file.close()

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    pass
    # TODO: Add code to show menu to user
    @staticmethod
    def print_menu_tasks():
        print('''
                Menu of Options
                1) Show Current Product List
                2) Add a new Product and Price
                3) Save Data to File
                4) Exit Program        
                ''')
        print()

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def print_current_product_list():
        print("Your Current Product List is:")
        for row in list_of_product_objects:
            print(row.product_name + "," + str(row.product_price))

    # TODO: Add code to get product data from user
    @staticmethod
    def add_product_to_list():
        try:
            name = input("Enter Product Name: ").strip()
            price = float(input("Enter Product Price: ").strip())
            p = Product(product_name=name, product_price=price)
            list_of_product_objects.append(p)
        except Exception as e:
            print(e)

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
FileProcessor.read_data_from_file(file_name_str, list_of_product_objects)

while True:
    # Show user a menu of options
    IO.print_menu_tasks()
    # Get user's menu option choice
    choice_str = IO.input_menu_choice()
    # Show user current data in the list of product objects
    if choice_str.strip() == "1":
        IO.print_current_product_list()
    # Let user add data to the list of product objects
    elif choice_str.strip() == "2":
        IO.add_product_to_list()
    # let user save current data to file and exit program
    elif choice_str.strip() == "3":
        FileProcessor.save_data_to_file(file_name_str, list_of_product_objects)

    elif choice_str.strip() == "4":
        print("Program Terminated")
        break

# Main Body of Script  ---------------------------------------------------- #
