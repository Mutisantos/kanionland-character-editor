# Filename must be different from imported standard libraries, otherwise
# it creates a circular import
from item import Item
import statistics
import json
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'OOP'))

# Read the item data from JSON file
item_compendium = {}
file_path = os.path.join(os.path.dirname(__file__), '..', 'IO', 'items.json')
with open(file_path, mode='r') as file:
    data = json.load(file)
    # As long as the JSON structure matches the Item attributes, entries can
    # be directly mapped to Item instances
    item_compendium = [Item(**item) for item in data]

price_compendium = []
for item in item_compendium:
    # print (item.display_info())
    price_compendium.append(item.price)

# Hallar la media
mean_sales = statistics.mean(price_compendium)
print(f"La media es: {mean_sales}")

# Hallar la mediana
median_sales = statistics.median(price_compendium)
print(f"La mediana es: {median_sales}")


# Hallar la moda
mode_sales = statistics.mode(price_compendium)
print(f"La moda es: {mode_sales}")

# Desviación Estandar
stdev_sales = statistics.stdev(price_compendium)
print(f"La Desviación Estandar es: {stdev_sales}")

# Hallar la varianza
variance_sales = statistics.variance(price_compendium)
print(f"La Varianza es: {variance_sales}")

max_sales = max(price_compendium)
min_sales = min(price_compendium)

range_sales = max_sales - min_sales
print(f'Rango de ventas: {range_sales}')
