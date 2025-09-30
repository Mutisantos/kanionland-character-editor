from .chain_handler import Handler
from OOP.store_transaction import StoreTransaction


class CharacterEquipHandler(Handler):

    def handle(self, request: StoreTransaction) -> None:
        print(self)
        character = request.buyer
        item = request.item
        if (character.can_equip(item)):
            character.equip_item(item)
            request.buyer = character
            print(f"{self._next_handler}")
            super().handle(request)
        else:
            print("Character cannot equip item")
