from .listener import Listener
from pydantic import Field


class StoreListener[T](Listener):
    listener_id: str = Field(..., description="Listener ID")

    def __init__(self, listener_id: str):
        self.listener_id = listener_id

    def notify(self, event: T) -> None:
        print(f"<{self.listener_id}>: Item retrieved from store: {event}")
