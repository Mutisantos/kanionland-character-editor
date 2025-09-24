# As the OOP folder is a package, it can be imported
# The import statement allows to import specific elements from a module
from OOP.character import Character
from OOP.armor import Armor
from OOP.weapon import Weapon

char_a = Character("Gazz Leudos", "Kanion", "M", 21, 42, 90,
                   430, 2500, "Frost Knight", 100, 100, 100)
armor_a = Armor("Pumiblu Armor", 10, Parts.BODY,
                10, 10, 10, 10, "Pumiblu Armor")
weapon_a = Weapon("Pumiblu Sword", 10, Parts.RIGHT_HAND,
                  10, 10, 10, 10, "Pumiblu Sword")

char_a.equip_item(armor_a)
char_a.equip_item(weapon_a)

print(char_a.display_info())
print(char_a.show_equipment())
print(char_a.show_inventory())
