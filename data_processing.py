import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany
print("All cities in Germany")
for city in cities:
    if city['country'] == 'Germany':
        print(city['city'])
print()

# Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with a temperature above 12°C")
for city in cities:
    if city['country'] == 'Spain' and float(city['temperature']) > 12:
        print(f"{city['city']}: {city['temperature']}")
print()

# Count the number of unique countries
print("Number of unique countries")
unique_countries = len(set(city['country'] for city in cities))
print(unique_countries)
print()

# Print the average temperature for all the cities in Germany
print("Average temperature for all the cities in Germany")
cities_in_G = []
for city in cities:
    if city['country'] == 'Germany':
        cities_in_G.append(city)
temps = [float(city['temperature']) for city in cities_in_G]
print(sum(temps)/len(temps))    
print()

# Print the max temperature for all the cities in Italy
print("Max temperature for all the cities in Italy")
cities_in_I = []
for city in cities:
    if city['country'] == 'Italy':
        cities_in_I.append(city)
temps = [float(city['temperature']) for city in cities_in_I]
print(max(temps))
