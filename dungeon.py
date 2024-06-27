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

        self.__name = name
        self.__description = description
        self.__items: List[Item] = []
        self.__creatures: List[Creature] = []
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
        return self.__creatures
    
    @property
    def items(self) -> List[Creature]:
            return self.__items

    @items.setter
    def items(self, new_items):
        if self.__items > 0 and self.__items < 4:
            self.__items = new_items

    
    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, new_dungeon):
        self.__next = new_dungeon

    @property
    def previous(self):
        return self.__prior

    @previous.setter
    def previous(self, previous_dungeon):
        self.__prior = previous_dungeon

    def show_creatures(self) -> str:
        return self.__creatures

    def check_creatures(self, creature_name: str) -> bool:
        if creature_name in self.__creatures:
            return True





