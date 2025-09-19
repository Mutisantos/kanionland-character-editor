from character import Character
from item import Item
from partEnum import Parts
from weapon import Weapon
from armor import Armor
from typing import Optional, Tuple


def race_check(race: str):
    def decorator(func):
        def wrapper(chara: Character):
            result = func(chara)
            if race != chara.race:
                print(f"Character {chara.name} is louder!!")
                if isinstance(result, str):
                    return result.upper()
            return result
        return wrapper
    return decorator


def log_debugger(func):
    # It can be specified which arguments the wrapper receives
    def wrapper(chara):
        print(f"Calling function: {func.__name__}")
        # then passes the arguments to the original function
        result = func(chara)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper


# The order of decorators matters, as they are applied from the bottom up
@log_debugger
@race_check('Kanion')
def character_debugger(chara: Character):
    return chara.display_info()


char_a = Character("Gazz Leudos", "Kanion", "M", 21, 42, 90,
                   430, 2500, "Frost Knight", 100, 100, 100)

char_b = Character("Mayu", "Pumiblu", "F", 12, 12, 72,
                   421, 2500, "Salvajita", 100, 100, 100)


print(character_debugger(char_a))
print(character_debugger(char_b))
