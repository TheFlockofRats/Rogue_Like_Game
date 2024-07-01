from abc import ABC, abstractmethod
from enum import Enum
from typing import List
from random import randint
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
    def set_stats(self, stats: List[int], int):
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


class Armor(Item):
    def __init__(self, name: str, value: int, condition: Condition, stats: List[int]):
        super().__init__(name, value, condition)
        self.__physical_attack_modifier = 0
        self.__physical_defense_modifier = 0
        self.__magical_attack_modifier = 0
        self.__magical_defense_modifier = 0
        self.__stats = stats

    def set_stats(self, stats: List[int]):
        self.__physical_attack_modifier = self.__stats[0]
        self.__physical_defense_modifier = self.__stats[1]
        self.__magical_attack_modifier = self.__stats[2]
        self.__magical_defense_modifier = self.__stats[3]

        if len(stats) != 4:
            raise ValueError

        for i in range(len(stats)):
            if not isinstance(i, int):
                raise TypeError


    def adjust_stats(self):
        self.__physical_attack_modifier = math.floor(self.__physical_attack_modifier)
        self.__physical_defense_modifier = math.floor(self.__physical_defense_modifier)
        self.__magical_attack_modifier = math.floor(self.__magical_attack_modifier)
        self.__magical_defense_modifier = math.floor(self.__magical_defense_modifier)

    def item_info(self):
        return f"Name: {self.name}, Value: {self.value}, Condition: {self.condition.name}, physical_attack_modifier: {self.__physical_attack_modifier}, physical_defense_modifier: {self.__physical_defense_modifier}, magical_attack_modifier: {self.__magical_attack_modifier}, magical_defense_modifier: {self.__magical_defense_modifier}  "

    @property
    def physical_attack_modifier(self):
        return self.__physical_attack_modifier

    @property
    def physical_defense_modifier(self):
        return self.__physical_defense_modifier

    @property
    def magical_attack_modifier(self):
        return self.__magical_attack_modifier

    @property
    def magical_defense_modifier(self):
        return self.__magical_defense_modifier

class weapon(Item):
    def __init__(self, name: str, value: int, condition: Condition, stats: List[int], AttackType, damage: int):
        super().__init__(name, value, condition, stats)
        self.__attack_type = AttackType
        self.__damage = damage

    @property
    def attack_type(self):
        return self.__attack_type

    @property
    def dammage(self):
        return self.__damage
    
    @attack_type.setter
    def attack_type(self, value):
        self.__attack_type = value

    @dammage.setter
    def dammage(self, value):
        if isinstance(value, int):
            self.__damage = value
        else:
            raise ValueError
        
    def set_stats(self, stats: List[int]):
        
        
    







class Creature(Character):

    def __init__(self, char_name):
        super().__init__(char_name)
        self.physical_stats = [randint(0, 8), randint(0, 8)]
        self.magical_stats = [randint(0, 8), randint(0, 8)]
        x = randint(20, 40)
        self.health = [x, x]
        self.equip(Weapon(choice(Weapon.WEAPONS), condition=Condition.GOOD, value=0,
                          stats=[randint(1,5) for _ in range(4)],
                          attack_type=(choice(list(AttackType))), damage=randint(2, 12)))
        self.__gold = randint(0, 25)




if __name__ == "__main__":
    loot_item = Loot("Gold Coin", 100, Condition.EXCELLENT)
    print(loot_item)  # Output: Name: Gold Coin, Value: 100, Condition: EXCELLENT