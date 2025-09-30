# Customizing the __init__ of OOP module allows to make direct imports
from OOP import StoreStockService, TaxingService, Character, Weapon, Armor
from OOP.partEnum import Parts
from OOP.store_transaction import StoreTransaction
from handlers import TransactionCostHandler, StoreStockHandler, CharacterEquipHandler

if __name__ == "__main__":
    store_stock_service = StoreStockService()
    taxing_service = TaxingService()
    char_a = Character(name="Gazz Leudos", race="Kanion", gender="M", age=21, weight=42, height=90,
                       aura=430, money=2500, title="Frost Knight", hunger=100, thrist=100, sleep=100)
    equipable_pinchito = Weapon(
        id=1001,
        name="Pinchito",
        weight=2,
        strength=2,
        power=0,
        range=5,
        stealth=-10,
        price=10,
        part=Parts.RIGHT_ARM,
        description="Autoexplicativo",
        quality="Common")
    equipable_armor = Armor(
        id=2202,
        name="Gambesón",
        weight=7,
        defense=5,
        balance=5,
        spirit=2,
        stealth=-2,
        part=Parts.TORSO,
        description="Armadura de telas y cueros",
        quality="Common")

    store_stock_service.add_equipment(equipable_pinchito, 5)
    store_stock_service.add_equipment(equipable_armor, 5)
    store_transaction = StoreTransaction(char_a, equipable_pinchito, 3)

    transaction_cost_handler = TransactionCostHandler(taxing_service)
    store_stock_handler = StoreStockHandler(store_stock_service)
    character_equip_handler = CharacterEquipHandler()

    transaction_cost_handler.set_next(None)
    store_stock_handler.set_next(transaction_cost_handler)
    character_equip_handler.set_next(store_stock_handler)
    # Must go character handler -> store stock handler -> transaction cost handler
    character_equip_handler.handle(store_transaction)
