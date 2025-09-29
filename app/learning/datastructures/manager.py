from .listener import Listener
from pydantic import Field


class ListenerManager[T]:
    def __init__(self):
        self.listeners: list[Listener] = []

    def subscribe(self, listener: Listener) -> None:
        self.listeners.append(listener)

    def unsubscribe(self, listener: Listener) -> None:
        self.listeners.remove(listener)

    # T type must be consistent to listener generic definition
    def notify(self, event: T) -> None:
        for listener in self.listeners:
            listener.notify(event)
