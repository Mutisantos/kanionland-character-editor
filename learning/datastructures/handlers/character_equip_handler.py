from ...OOP.store_transaction import StoreTransaction
from .chain_handler import Handler


class CharacterEquipHandler(Handler):

    def handle(self, request: StoreTransaction) -> None:
        character = request.buyer
        item = request.item
        if (character.can_equip(item)):
            character.equip_item(item)
            request.buyer = character
            self._next_handler.handle(request)
        else:
            print("Character cannot equip item")
