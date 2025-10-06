from .chain_handler import Handler
from ..OOP import StoreTransaction


class CharacterEquipHandler(Handler):

    def handle(self, request: StoreTransaction) -> None:
        print(self)
        character = request.buyer
        item = request.equipable_object
        if character.can_equip(item):
            character.equip_item(item)
            request.buyer = character
            print(f"{self._next_handler}")
            super().handle(request)
        else:
            print("Character cannot equip item")
