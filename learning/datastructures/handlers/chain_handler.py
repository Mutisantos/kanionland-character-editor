from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Self

# A class helper for creating abstract classes


@dataclass
class Handler[T](ABC):
    _next_handler: Self | None = None

    def set_next(self, next_handler: Self) -> Self:
        self.next_handler = next_handler
        return next_handler

    # As a chain of responsability, the element must handle the request
    # And then use the result of said handling to the next element in the chain
    @abstractmethod
    def handle(self, request: T) -> None:
        if self._next_handler:
            print(f"-----Processing request at {self.__class__}")
            self._next_handler.handle(request)
        else:
            print(f"-----Finished flow at {self.__class__}")
