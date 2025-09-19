from character import Character
from item import Item
from partEnum import Parts
from weapon import Weapon
from armor import Armor
from typing import Optional, Tuple

char_a = Character("Gazz Leudos", "Kanion", "M", 21, 42, 90,
                   430, 2500, "Frost Knight", 100, 100, 100)
# Calling append to the list returns None, so the items must be
# concatenated differently
pumiblu_parts = Parts.get_basic_body() + [Parts.TAIL]
pumiblu_parts.append(Parts.LEFT_EAR_ARM)
pumiblu_parts.append(Parts.RIGHT_EAR_ARM)
char_b = Character(
    "Mayu",
    "Pumiblu",
    "F",
    12,
    12,
    72,
    421,
    2500,
    "Salvajita",
    100,
    100,
    100,
    pumiblu_parts)

item_a = Item(
    "Sopita Caliente",
    description="Restaura 50 de VIT",
    price=50,
    stat="VIT",
    modifier=50)
item_b = Item(
    "Sopita Fria",
    description="Restaura 12 de VIT",
    price=11,
    stat="VIT",
    modifier=12)

equipable_pinchito = Weapon(
    name="Pinchito",
    weight=2,
    strength=2,
    power=0,
    range=5,
    stealth=-10,
    part=Parts.RIGHT_ARM,
    description="Autoexplicativo",
    quality="Common")
equipable_armor = Armor(
    name="Gambesón",
    weight=7,
    defense=5,
    balance=5,
    spirit=2,
    stealth=-2,
    part=Parts.TORSO,
    description="Armadura de telas y cueros",
    quality="Common")
equipable_helmet = Armor(
    name="Casco Meh",
    weight=7,
    defense=5,
    balance=5,
    spirit=2,
    stealth=-2,
    part=Parts.HEAD,
    description="Casco Fome",
    quality="Common")
equipable_tail = Armor(
    name="Protector de Cola",
    weight=1,
    defense=1,
    balance=5,
    spirit=2,
    stealth=-2,
    part=Parts.TAIL,
    description="aUTOEXPLICCATIVO",
    quality="Common")

# Method Call
print(char_a.display_info())
try:
    print(char_a.withdraw_money(3000))
except ValueError as e:
    print(f"Insufficient Funds: {e}")
print(char_a.deposit_money(501))
print(char_a.withdraw_money(300))
print(char_a.update_hunger(30))
print(char_a.update_thirst(-50))
print(char_a.update_sleep(-20))
print(char_a.show_inventory())
print(char_a.add_item(item_a, 10))
print(char_a.add_item(item_b))
print(char_a.show_inventory())

print(char_a.consume_item("Sopita Caliente", 5))
print(char_a.show_inventory())
try:
    print(char_a.consume_item("Sopita Caliente", 6))
except ValueError as e:
    print(f"Error: {e}")
print(char_a.consume_item("Sopita Caliente", 5))
print(char_a.show_inventory())
print(char_a.consume_item("Sopita Fria", 1))
print(char_a.show_inventory())
# Enum checks
print(Parts.get_enum_by_name("Head"))
print(Parts.get_enum_by_name("Tentáculo Superior Izquierdo"))

print(char_a.equip_item(equipable_pinchito))
print(char_a.equip_item(equipable_armor))
print(char_a.equip_item(equipable_helmet))
# equipping a second helmet to test multiple items on same part
print(char_a.equip_item(equipable_helmet))
# The body part exists but the character doesn't have it
print(char_a.equip_item(equipable_tail))
print(char_a.show_equipment())

print(char_b.equip_item(equipable_pinchito))
print(char_b.equip_item(equipable_armor))
print(char_b.equip_item(equipable_helmet))
# The body part exists and the character has it
print(char_b.equip_item(equipable_tail))
print(char_b.show_equipment())

optional_a: Optional[Tuple[Item, int]] = char_a.has_item("Sopita Caliente")
# The object will be None
print(f"Optional A: {optional_a}")
print(char_a.add_item(item_a, 10))
optional_a: Optional[Tuple[Item, int]] = char_a.has_item("Sopita Caliente")
# The object is the expected Tuple
print(f"Optional A: {optional_a[0].name}, Amount: {optional_a[1]}")
