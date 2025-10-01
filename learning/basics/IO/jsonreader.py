# These imports are brought from Python standard libraries
from item import Item
import json
import os
import sys
import random
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'OOP'))

file_path = os.path.join(os.path.dirname(__file__), 'creeper.json')
file_path_b = os.path.join(os.path.dirname(__file__), 'items.json')
with open(file_path, mode='r', encoding='utf-8') as file:
    index = 0
    # JSON reader loads file and interprets it as a list of dictionaries
    for troop in json.load(file):
        index += 1
        print(f"----{index}.{troop}\n")

item_a = Item(
    "Salticubo",
    description="Teletransportador",
    price=2500,
    stat=None,
    modifier=0)
item_b = Item(
    "Sopita Fria",
    description="Restaura 12 de VIT",
    price=11,
    stat="VIT",
    modifier=12)
item_c = Item(
    "Comida Fria",
    description="Restaura 12 de VIT",
    price=11,
    stat="VIT",
    modifier=12)
item_d = Item(
    "Galleta dura",
    description="Restaura 12 de VIT",
    price=11,
    stat="VIT",
    modifier=12)

item_list = [
    item_a.to_dict(),
    item_b.to_dict(),
    item_c.to_dict(),
    item_d.to_dict()]
random.shuffle(item_list)

with open(file_path_b, mode='w', encoding='utf-8') as file:
    json.dump(item_list, file, indent=4)
    file.close()


json_files = [jsonfile for jsonfile in os.listdir(
    os.path.dirname(__file__)) if jsonfile.endswith('.json')]
print(list(map(lambda f: f[:-5], json_files)))

if 'items_renamed.json' not in json_files:
    os.rename(
        file_path_b,
        os.path.join(
            os.path.dirname(__file__),
            'items_renamed.json'))
