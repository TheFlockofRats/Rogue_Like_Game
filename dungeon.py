from typing import List
"""
fix still Self.__prior should be self.__previous

"""

class Item:
    pass


class Creature:
    pass


class Dungeon:
    """ A class that creates the board for the game
    ...

    Attributes
    ----------
    self.__name : str
        Name for the dungeon. Cannot be None
    self.__description: str
        A brief description of the dungeon
    self.__items: List[Item]
        A list of items that hold the contents found in the Dungeon
    self.__creatures: List[Creature]
        Holds all the creatures in a given Dungeon.
    self.__previous: Dungeon
        The previous Dungeon the players came from
    self.__next: Dungeon
        The next Dungeon the players came move to.

    Methods
    -------
    show_creatures(self) -> str
        This method returns a string of the list of creature names
    check_creature(self, creature_name: str) -> bool
        This method returns a bool if a creature is in the Dungeon by searching through self__creatures
    show_items(self) -> str
        This method returns a string of the list of items
    check_item(self, item_name: str) -> bool
        This method returns a bool if an item is in the Dungeon by searching through __items
    pick_up_item(self, item_name: str, target: Character) -> str
        This method searches for an item in the room by name and adds it to the inventory of the target Character.
    drop_item(self, item_name: str, target: Character) -> str
        This method searches for an item in the target Character's inventory and returns it back to the Dungeon
    __str__(self) -> str
        A string override to return the details of the room.
    """
    def __init__(self, name: str, description: str):
        """
        Parameters
        ----------
        self.__name : str
            Name for the dungeon. Cannot be None
        self.__description: str
            A brief description of the dungeon
        self.__items: List[Item]
            A list of items that hold the contents found in the Dungeon
        self.__creatures: List[Creature]
            Holds all the creatures in a given Dungeon.
        self.__previous: Dungeon
            The previous Dungeon the players came from
        self.__next: Dungeon
            The next Dungeon the players came move to.
        """
        # Check to see if name is of type str and the length is greater than 0, else raise TypeError
        if not isinstance(name, str) or len(name) < 1:
            raise TypeError
        # Check to see if description is of type str and the length is greater than 0, else raise TypeError
        if not isinstance(description, str) or len(description) < 1:
            raise TypeError
        # Check to ensure that Self.__creatures length is not more than 4, else raise ValueError
        if not len(self.__creatures) > 5:
            self.__creatures: List[Creature] = []
        else:
            raise ValueError("Too many creatures in this dungeon")

        self.__name = name
        self.__description = description
        self.__items: List[Item] = []
        self.__prior: Dungeon = None
        self.__next: Dungeon = None

    @property
    def name(self) -> str:
        # Returns self.__name
        return self.__name

    @name.setter
    def name(self, value: str):
        # Check to see if value is of type str and the length is greater than 0, else raise TypeError
        if not isinstance(value, str) or len(value) < 1:
            raise TypeError
        # Sets self.__name to value input
        self.__name = value

    @property
    def description(self) -> str:
        # Returns self.__description
        return self.__description

    @description.setter
    def description(self, value):
        # Check to see if value is of type str and the length is greater than 0, else raise TypeError
        if not isinstance(value, str) or len(value) < 1:
            raise TypeError
        # Sets self.__name to value input
        self.__description = value

    @property
    def creatures(self) -> List[Creature]:
        # Check to ensure that Self.__creatures length is not more than 4, else raise ValueError
        if not len(self.__creatures) < 5:
            # Returns self.__creatures
            return self.__creatures
        else:
            raise ValueError

    @property
    def items(self) -> List[Creature]:
        # Returns self.__items
        return self.__items

    @items.setter
    def items(self, new_items):
        # Check to ensure that self.__items is not more than 4
        if self.__items < 4:
            # Adding new_item to self.__items
            self.__items.append(new_items)
        else:
            raise ValueError('There are to many items')

    @property
    def next(self):
        # Returns self.__next
        return self.__next

    def Loot(self):
        pass

    def Armor(self):
        pass

    def Weapon(self):
        pass
