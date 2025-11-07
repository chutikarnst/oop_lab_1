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

Table class: Handles the functions
- def __init__(self, name, dict_list):
        Initialize the name and list of dictionaries.
- def aggregate(self, aggregation_function, aggregation_key):
        Get the data from the aggregation_key and use aggeregation_function to find the results.
- def filter(self, condition):
	Filter the data by the condition and return a new table.
