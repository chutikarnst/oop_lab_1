import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Let's write a function to filter out only items that meet the condition
# Hint: condition will be associated with an anonymous function, e.x., lamdbda x: max(x)
def filter(condition, dict_list):
    temps = []
    for item in dict_list:
        if condition(item):
            temps.append(item)
    return temps

# Let's write a function to do aggregation given an aggregation function and an aggregation key
def aggregate(aggregation_key, aggregation_function, dict_list):
    temps = []
    for item in dict_list:
        try:
            temps.append(float(item[aggregation_key]))
        except ValueError:
            temps.append(item[aggregation_key])
    return aggregation_function(temps)

# Print all cities in Germany
print("All cities in Germany")
g = lambda x: x['country'] == 'Germany'
fg = filter(g,cities)
for city in fg:
    print(city['city'])
print()

# Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with a temperature above 12°C")
c = lambda x: x['country'] == 'Spain' and float(x['temperature']) > 12
fs = filter(c,cities)
for city in fs:
    print(city['city'])
print()

# Count the number of unique countries
print("Number of unique countries")
print(aggregate('country', lambda x: len(set(x)),cities))
print()

# Print the average temperature for all the cities in Germany
print("Average temperature for all the cities in Germany")
val = aggregate('temperature',lambda x: sum(x)/len(x),filter(lambda x: x['country'] == 'Germany',cities))
print(val)
print()

# Print the max temperature for all the cities in Italy
print("Max temperature for all the cities in Italy")
val = aggregate('temperature',lambda x: max(x),filter(lambda x: x['country'] == 'Italy',cities))
print(val)