from typing import List

class Item:
    pass

class Creature:
    pass

class Dungeon:
    def __init__(self, name: str, description: str):
        if not isinstance(name, str) or len(name) < 1:
            raise TypeError
        if not isinstance(description, str) or len(description) < 1:
            raise TypeError
        
        if not len(self.__creatures) > 5:
            self.__creatures: List[Creature] = []
        else:
            raise ValueError('Too many Creatures')

        self.__name = name
        self.__description = description
        self.__items: List[Item] = []
        self.__prior: Dungeon = None
        self.__next: Dungeon = None

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or len(value) < 1:
            raise TypeError
        self.__name = value
    
    @property
    def description(self) -> str:
        return self.__description
    
    @description.setter
    def description(self, value):
        if not isinstance(value, str) or len(value) < 1:
            raise TypeError
        self.__description = value
    
    @property
    def creatures(self) -> List[Creature]:
        if not len(self.__creatures):
            return self.__creatures
    
    @property
    def items(self) -> List[Creature]:
            return self.__items

    @items.setter
    def items(self, new_items):
        if self.__items < 4:
            self.__items.append(new_items)

    
    @property
    def next(self):
        return self.__next

    def Loot(self):
        pass

    def Armor(self):
        pass

    def Weapon(self):
        pass

