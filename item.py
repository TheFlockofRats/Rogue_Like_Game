from abc import ABC, abstractmethod
from enum import Enum
from typing import List
import math


class Condition(Enum):
    EXCELLENT = 1
    GOOD = 2
    ACCEPTABLE = 3
    BAD = 4
    ABYSMAL = 5


class AttackType(Enum):
    PHYSICAL = 1
    MAGICAL = 2


class Item(ABC):
    def __init__(self, name: str, value: int, condition: Condition):
        self.__name = name
        self.__value = value
        self.__condition = condition

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 1:
            raise TypeError
        self.__name = value
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        if not isinstance(value, int):
            raise TypeError
        if value < 0:
            raise ValueError
        self._value = value
    
    @property
    def condition(self):
        return self.__condition
    
    @condition.setter
    def condition(self, value):
        if not isinstance(value, Condition):
            raise TypeError
        else:
            self.__condition = value
    
    @abstractmethod
    def item_info(self) -> str:
        return f"Name: {self.name}, Value: {self.value}, Condition: {self.condition.name}"

    @abstractmethod
    def stats(self, stats: List[int], int):
        pass

    @abstractmethod
    def adjust_stats(self):
        pass


class Loot(Item):
    def __init__(self, name, value, condition):
        super().__init__(name, value, condition)

    def item_info(self):
        return super().item_info()

    def set_stats(self, stats: int):
        condition_modifiers = {
            Condition.EXCELLENT: 1.25,
            Condition.GOOD: 1.0,
            Condition.ACCEPTABLE: 0.8,
            Condition.BAD: 0.5,
            Condition.ABYSMAL: 0.1
        }
        self.value = math.floor(self.value * condition_modifiers[self.condition])
    
    def adjust_stats(self):
        pass

if __name__ == "__main__":
    loot_item = Loot("Gold Coin", 100, Condition.EXCELLENT)
    print(loot_item)  # Output: Name: Gold Coin, Value: 100, Condition: EXCELLENT