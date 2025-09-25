
# Unrepeable group of items
if __name__ == "__main__":
    # Using curly brace notation to define a set
    austur_countries = {"Tatama", "Chunsua", "Olmoteptl",
                        "Frocteres", "Chromentina", "Voeldan", "Tatama",
                        "Simite", "Amborghessia", "Simite", "Nueva Lacocia"}
    eosian_countries = {"Lacocia", "Ispamolca",
                        "Parastalan", "Krietmatz", "Balcca", "Zergov"}
    playable_countries = {"Tatama", "Chunsua",
                          "Olmoteptl", "Frocteres", "Amborghessia", "Guacari"}

    print(austur_countries)
    # Set can be created from any iterable, removing repeated elements
    print(set("AGOSTINA"))
    if "Tatama" in austur_countries:
        # Remove requires the element to exist
        austur_countries.remove("Tatama")
    print(austur_countries)
    # Discard doesn't raise an error if the element doesn't exist
    austur_countries.discard("Chromentina")
    print(austur_countries)
    # Repeated records won't be added
    austur_countries.add("Chromentina")
    print(austur_countries)
    # Update can add multiple elements at once
    austur_countries.update(["Tatama", "Grandos"])
    print(austur_countries)
    rand_country = austur_countries.pop()
    print(rand_country)
    print(austur_countries)

    # Intersection returns the common elements between two sets
    print(f"Intersection: {austur_countries.intersection(playable_countries)}")
    # Union returns all elements from both sets
    print(
        f"Union: {austur_countries.union(playable_countries, eosian_countries)}")
    # Difference returns the elements that are in the first set but not in the second
    print(
        f"Difference A - B : {austur_countries.difference(playable_countries)}")
    print(
        f"Difference B - A: {playable_countries.difference(austur_countries)}")
    # Symmetric difference returns the elements that are in one set but not in both
    print(
        f"Symmetric difference: {austur_countries.symmetric_difference(playable_countries)}")

    # Clear removes all elements, leaving an empty set
    austur_countries.clear()
    print(austur_countries)
