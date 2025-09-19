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

    # Magic methods override the default behavior of built-in functions
    # This is the main way to overload basic operations on Python for classes
    # __str__ is called when str() or print() is used on the object
    def __str__(self):
        return self.display_info(self)
    # eq and lt are used for sorting and comparisons, just like
    # overriding Comparator interface in Java
    # __eq__ is called when == operator is used

    def __eq__(self, other):
        return self.name == other.name
    # __lt__ is called when < operator is used

    def __lt__(self, other):
        return self.price < other.price
    # __add__ is called when + operator is used

    def __add__(self, other):
        if self.stat != other.stat:
            raise ValueError("Cannot add items with different stats")
        new_name = f"{self.name} & {other.name}"
        new_price = self.price + other.price
        new_modifier = self.modifier + other.modifier
        new_description = f"Combination of {self.name} and {other.name}"
        return Item(new_name, new_price, self.stat, new_modifier, new_description)
