from character import Character
from item import Item

char_a = Character("Gazz Leudos", "Kanion", "M", 21, 42, 90, 430, 2500, "Frost Knight", 100, 100, 100)

item_a = Item("Sopita Caliente", description="Restaura 50 de VIT", price=50, stat="VIT", modifier=50)
item_b = Item("Sopita Fria", description="Restaura 12 de VIT", price=11, stat="VIT", modifier=12)


# Method Call
print(char_a.display_info())
print(char_a.withdraw_money(300))
print(char_a.deposit_money(500))    
print(char_a.update_hunger(30))
print(char_a.update_thirst(-50))
print(char_a.update_sleep(-20))
print(char_a.show_inventory())
print(char_a.add_item(item_a,10))
print(char_a.add_item(item_b))
print(char_a.show_inventory())

print(char_a.consume_item("Sopita Caliente",5))
print(char_a.show_inventory()) 
try:
    print(char_a.consume_item("Sopita Caliente",6))
except ValueError as e:
    print(f"Error: {e}")
print(char_a.consume_item("Sopita Caliente",5))
print(char_a.show_inventory()) 
print(char_a.consume_item("Sopita Fria",1))
print(char_a.show_inventory())