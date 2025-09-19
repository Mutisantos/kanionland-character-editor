class Item:
    def __init__(self, name, price, stat, modifier=0, description=""):
        self.name = name
        self.price = price
        self.stat = stat
        self.modifier = modifier
        self.description = description

    def to_dict(self):
        """Dictionary representation makes the class JSON serializable"""
        return self.__dict__.copy()

    def display_info(self, amount=1):
        info = f"Item: {self.name} ({amount})\n"
        info += f"Price: {self.price}\n"
        info += f"Stat: {self.stat}\n"
        info += f"Modifier: {self.modifier}\n"
        info += f"Description: {self.description}\n"
        return info
