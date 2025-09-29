from typing import Protocol

# Generics definition on Python > 3.12.0
# As it extends Protocol, it is an interface


class Listener[T](Protocol):
    def notify(self, event: T) -> None: ...
