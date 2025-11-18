this lab shows how to use Lambda and make the code look cleaner

oop_lab_1/
- README.md            #this file
- Cities.csv           #dataset
- data_processing.py   #analysis code

DataLoader class: Handles loading CSV data files
- def __init__(self, base_path=None):
        Initialize the DataLoader with a base path for data files.
- def load_csv(self, filename):
        Load a CSV file and return its contents as a list of dictionaries.

DB class: Handles the Data Base
- def __init__(self):
 		Create an empty table dictionary
- def insert(self, table_obj):
		Add an existing table to the dictionary
- def search(self, table_name):
		get the data by the table name

Table class: Handles the functions
- def __init__(self, name, dict_list):
        Initialize the name and list of dictionaries.
- def aggregate(self, aggregation_function, aggregation_key):
        Get the data from the aggregation_key and use aggeregation_function to find the results.
- def filter(self, condition):
		Filter the data by the condition and return a new table.
- def join(self, other_table, key):
		creates a table and store the other table rows by key (ex. Italy: [data with Italy]), then merge the new table with the table you want to merge with
- def __str__(self):
		defaut string when calling the table
