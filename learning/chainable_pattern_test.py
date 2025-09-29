import OOP
import datastructures

if __name__ == "__main__":
    store_stock_service = OOP.services.store_stock_service.StoreStockService()
    taxing_service = OOP.services.taxing_service.TaxingService()
    char_a = OOP.character.Character(name="Gazz Leudos", race="Kanion", gender="M", age=21, weight=42, height=90,
                                     aura=430, money=2500, title="Frost Knight", hunger=100, thrist=100, sleep=100)
    equipable_pinchito = OOP.weapon.Weapon(
        name="Pinchito",
        weight=2,
        strength=2,
        power=0,
        range=5,
        stealth=-10,
        price=10,
        part=OOP.partEnum.Parts.RIGHT_ARM,
        description="Autoexplicativo",
        quality="Common")
    equipable_armor = OOP.armor.Armor(
        name="Gambesón",
        weight=7,
        defense=5,
        balance=5,
        spirit=2,
        stealth=-2,
        part=OOP.partEnum.Parts.TORSO,
        description="Armadura de telas y cueros",
        quality="Common")

    store_transaction = OOP.store_transaction.StoreTransaction(
        char_a, equipable_pinchito, 3)

    transaction_cost_handler = datastructures.handlers.TransactionCostHandler(
        taxing_service)
    store_stock_handler = datastructures.handlers.StoreStockHandler(
        store_stock_service)
    character_equip_handler = datastructures.handlers.CharacterEquipHandler()

    character_equip_handler.set_next(store_stock_handler)
    store_stock_handler.set_next(transaction_cost_handler)
    # Must go character handler -> store stock handler -> transaction cost handler
    character_equip_handler.handle(store_transaction)
