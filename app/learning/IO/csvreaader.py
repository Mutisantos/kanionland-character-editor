from character import Character
import csv
import os
import sys
import random
import time
# from ..OOP.character import Character
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'OOP'))

file_path = os.path.join(os.path.dirname(__file__), 'characterdata.csv')
file_path_updated = os.path.join(os.path.dirname(__file__), 'summary.csv')
rand_id = 0

with open(file_path, mode='r', encoding='utf-8') as file:
    # csv package allows parsing CSV files into different structures such as
    # Dictionaries
    csv_reader = csv.DictReader(file)  # Dictionary Iterator
    rows = list(csv_reader)
    rand_id = random.randint(len(rows), 5000)
    for row in rows:
        # As a dictionary, the data can be accessed by key
        print(f'{row["name"]} basic information:')
        print(row)

chara_miri = Character(
    name='Miri Vielakh',
    race='zi-bum',
    age='22',
    gender='F',
    weight=15,
    height=35,
    aura=100,
    money=10000,
    title='Hackerosa Bipolar',
    thrist=100,
    hunger=100,
    sleep=100)

column_attributes = ["id", "created_at"] + list(chara_miri.to_dict().keys())

with open(file_path, mode='a', encoding='utf-8', newline='') as file:
    # For writing, it is neccesary to pass the column names for the csv to
    # write
    file.write('\n')  # To avoid writing on the last line
    csv_appender = csv.DictWriter(file, fieldnames=column_attributes)
    newchara_row = chara_miri.to_dict()
    newchara_row["id"] = rand_id
    newchara_row["created_at"] = time.strftime(
        "%Y-%m-%d %H:%M:%S", time.localtime())
    csv_appender.writerow(newchara_row)

with open(file_path, mode='r', encoding='utf-8') as file:
    # csv package allows parsing CSV files into different structures such as
    # Dictionaries
    csv_reader = csv.DictReader(file)
    with open(
        file_path_updated,
        mode='w',
        encoding='utf-8',
        newline=''
    ) as updated_file:
        csv_writer = csv.DictWriter(
            updated_file, fieldnames=[
                "titled_name", "total_stats"])
        csv_writer.writeheader()
        for row in csv_reader:
            new_model_row = {}
            new_model_row["titled_name"] = f'{row["name"]} the {row["title"]}'
            new_model_row["total_stats"] = int(
                row["hunger"]) + int(row["thrist"]) + int(row["sleep"])
            csv_writer.writerow(new_model_row)
