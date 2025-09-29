import datastructures
from OOP.item import Item

if __name__ == "__main__":
    # As an observer pattern, the manager will handle subscriptions and notifications
    manager = datastructures.ListenerManager()
    # Listeners are observers that will be notified when an event occurs
    store_broker = datastructures.StoreListener[Item]("Broker")
    store_supplier = datastructures.StoreListener[Item]("Supplier")
    # Events are the data that will be passed to the listeners
    sword_item = Item("Sword", 100, "Attack", 10, "A sword")
    shield_item = Item("Shield", 100, "Defense", 10, "A shield")
    # Subscribing the listeners to the manager
    manager.subscribe(store_broker)
    manager.subscribe(store_supplier)
    # Notifying the listeners, the listeners will handle the events accordingly
    manager.notify(sword_item)
    manager.notify(shield_item)
    # Unsubscribing the listeners from the manager
    manager.unsubscribe(store_broker)
    # Notifying the listeners again, the store broker shouldn't be notified
    manager.notify(sword_item)
    manager.notify(shield_item)
