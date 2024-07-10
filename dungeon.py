from typing import List

import item
from character import Character
from item import Armor, Weapon, Loot
"""

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
            self.__creatures = []
        else:
            raise ValueError("Too many creatures in this dungeon")

        self.__name = name
        self.__description = description
        self.__items: List[Item] = []
        self.__previous: Dungeon = None
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
    def creatures(self) -> list[Creature]:
            # Returns self.__creatures
            return self.__creatures


    @creatures.setter
    def creatures(self, new_creatures):
        # Check to ensure that Self.__creatures length is not more than 4, else raise ValueError
        if len(self.__creatures) < 5:
            self.__creatures = new_creatures
        else:
            raise ValueError

    @property
    def items(self) -> list[Creature]:
        # Returns self.__items
        return self.__items

    @items.setter
    def items(self, new_items):
        # Check to ensure that self.__items is not more than 4
        if len(self.__items) < 4:
            # Adding new_item to self.__items
            self.__items.append(new_items)
        else:
            raise ValueError('There are to many items')

    @property
    def next(self):
        # Returns self.__next
        return self.__next

    @next.setter
    def next(self, new_next):
        # Sets self.__next to something new
        self.__next = new_next

    @property
    def previous(self):
        # Returns previous dungeon
        return self.__previous

    @previous.setter
    def previous(self, new_previous):
        # Sets the previous dungeon to something new
        self.__previous = new_previous

    def show_creatures(self) -> str:
        # Shows all the creatures from a given list and separates with a comma using .join()
        separated = ', '.join(self.__creatures)
        return separated

    def check_creature(self, creature_name: str):
        #if the creature in question is in the list of creatures then it returns True else returns False
        if creature_name in self.__creatures:
            return True

        else:
            return False

    def show_items(self) -> str:
        # Loop runs as many times as there is items in the list.
        for i in range(len(self.__items)):
            # If the item is armor it returns the item with -Armor after
            if i in item.Armor:
                return f'{self.__items[i]} - Armor'
            # If the item is weapon it returns the item with -Weapon after
            if i in item.Weapon:
                return f'{self.__items[i]} - Weapon'
            # If the item is Loot it returns the item with -Loot after
            if i in item.Loot:
                return f'{self.__items[i]} - Loot'

    def check_item(self, item_name: str) -> bool:
        # If the item in question is in the list of items in the dungeon it returns True else returns False
        if item_name in self.__items:
            return True

        else:
            return False

    def pick_up_item(self, item_name: str, target: Character) -> str:
        # If the item in question is not in the items within dungeon it returns with Item not found, else it picks up
        # the item and appends it to the targets inventory
        if item_name not in self.__items:
            return 'Item not found!'

        else:
            target.pick_up(item_name)

    def drop_item(self, item_name: str, target: Character) -> str:
        # If the item in question is not in the targets inventory it returns with No item with that name in your
        # inventory, else it drops the item from the target's inventory
        if item_name not in target.inventory:
            return 'No item with that name in your inventory'
        else:
            target.drop(item_name)

    def __str__(self) -> str:
        # Returns the room name, description of the room, the creatures in the room, and the items in the room
        return (f'Room Name: {self.__name}\nDescription: {self.__description}\n'
                f'===========================================================================\n'
                f'Creatures: {self.__creatures}\n'
                f'--------------------------------------------------------------------------\nItems: {self.__items}')
