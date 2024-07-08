from abc import ABC, abstractmethod
from enum import Enum
from typing import List
import math

class Condition(Enum):
    """
    Enum for item condition.
    """
    EXCELLENT = 1
    GOOD = 2
    ACCEPTABLE = 3
    BAD = 4
    ABYSMAL = 5


class AttackType(Enum):
    """
    Enum for attack types.
    """
    PHYSICAL = 1
    MAGICAL = 2


class Item(ABC):
    """
    Abstract base class for an item.
    """
    def __init__(self, name: str, value: int, condition: Condition):
        """
        Initialize an Item.

        Args:
            name (str): The name of the item.
            value (int): The value of the item.
            condition (Condition): The condition of the item.
        """
        if not isinstance(name, str) or len(name) < 1:
            raise ValueError
        if not isinstance(value, int) or value < 0:
            raise ValueError
        if not isinstance(condition, Condition):
            raise TypeError
        
        self.__name = name
        self.__value = value
        self.__condition = condition

    @property
    def name(self):
        """
        Get the name of the item.
        """
        return self.__name
    
    @name.setter
    def name(self, value):
        """
        Set the name of the item.
        """
        if not isinstance(value, str) or len(value) < 1:
            raise ValueError
        self.__name = value
    
    @property
    def value(self):
        """
        Get the value of the item.
        """
        return self.__value
    
    @value.setter
    def value(self, value):
        """
        Set the value of the item.
        """
        if not isinstance(value, int) or value < 0:
            raise ValueError
        self.__value = value
    
    @property
    def condition(self):
        """
        Get the condition of the item.
        """
        return self.__condition
    
    @condition.setter
    def condition(self, value):
        """
        Set the condition of the item.
        """
        if not isinstance(value, Condition):
            raise TypeError
        self.__condition = value

    def __str__(self):
        """
        Return a string description of the item.
        """
        return f"Item: {self.name}, Value: {self.value}, Condition: {self.condition.name}"
    
    @abstractmethod
    def item_info(self) -> str:
        """
        Abstract method for item information.
        """
        pass 

    @abstractmethod
    def set_stats(self, stats: List[int]):
        """
        Abstract method to set item stats.
        """
        pass

    @abstractmethod
    def adjust_stats(self):
        """
        Abstract method to adjust item stats.
        """
        pass


class Loot(Item):
    """
    Class representing loot items.
    """
    def item_info(self):
        """
        Provides information about the loot item.
        """
        return super().__str__()

    def set_stats(self, stats: int):
        """
        Set stats for the loot item.

        Args:
            stats (int): The base value for the loot item.
        """
        if not isinstance(stats, int):
            raise ValueError
        
        if self.condition == Condition.EXCELLENT:
            self.value = math.floor(stats * 1.25)
        elif self.condition == Condition.GOOD:
            self.value = stats
        elif self.condition == Condition.ACCEPTABLE:
            self.value = math.floor(stats * 0.8)
        elif self.condition == Condition.BAD:
            self.value = math.floor(stats * 0.5)
        elif self.condition == Condition.ABYSMAL:
            self.value = math.floor(stats * 0.1)
    
    def adjust_stats(self):
        """
        Adjust stats for the loot item.
        """
        pass


class Armor(Item):
    """
    Class representing armor items.
    """
    def __init__(self, name: str, value: int, condition: Condition, stats: List[int]):
        """
        Initialize an Armor item.

        Args:
            name (str): The name of the armor item.
            value (int): The value of the armor item.
            condition (Condition): The condition of the armor item.
            stats (List[int]): List of stat values [physical_attack, physical_defense, magical_attack, magical_defense].
        """
        super().__init__(name, value, condition)
        self.__physical_attack_modifier = 0
        self.__physical_defense_modifier = 0
        self.__magical_attack_modifier = 0
        self.__magical_defense_modifier = 0
        self.set_stats(stats)

    @property
    def physical_attack(self):
        """
        Get the physical attack modifier of the armor.
        """
        return self.__physical_attack_modifier

    @property
    def physical_defense(self):
        """
        Get the physical defense modifier of the armor
        """
        return self.__physical_defense_modifier

    @property
    def magical_attack(self):
        """
        Get the magical attack modifier of the armor.
        """
        return self.__magical_attack_modifier

    @property
    def magical_defense(self):
        """
        Get the magical defense modifier of the armor.
        """
        return self.__magical_defense_modifier

    def set_stats(self, stats: List[int]):
        """
        Set stats for the armor item.

        Args:
            stats (List[int]): List of stat values [physical_attack, physical_defense, magical_attack, magical_defense].
        """
        if not isinstance(stats, list) or len(stats) != 4:
            raise ValueError
        for i in stats:
            if not isinstance(i, int):
                raise ValueError
            
        self.__physical_attack_modifier, self.__physical_defense_modifier, self.__magical_attack_modifier, self.__magical_defense_modifier = stats

    def adjust_stats(self):
        """
        Adjust stats for the armor item based on its condition.
        """
        if self.condition == Condition.EXCELLENT:
            modifier = 1.25
        elif self.condition == Condition.GOOD:
            modifier = 1.0
        elif self.condition == Condition.ACCEPTABLE:
            modifier = 0.8
        elif self.condition == Condition.BAD:
            modifier = 0.5
        elif self.condition == Condition.ABYSMAL:
            modifier = 0.25
    
        self.__physical_attack_modifier = math.floor(self.__physical_attack_modifier * modifier)
        self.__physical_defense_modifier = math.floor(self.__physical_defense_modifier * modifier)
        self.__magical_attack_modifier = math.floor(self.__magical_attack_modifier * modifier)
        self.__magical_defense_modifier = math.floor(self.__magical_defense_modifier * modifier)

    def item_info(self):
        """
        Provide detailed information about the armor item.
        """
        return (f"Item: {self.name}, Value: {self.value}, Condition: {self.condition.name}, "
                f"Physical Attack: {self.physical_attack}, Physical Defense: {self.physical_defense}, "
                f"Magical Attack: {self.magical_attack}, Magical Defense: {self.magical_defense}")    
    

class Weapon(Armor):
    """
    Class representing weapon items.
    """
    def __init__(self, name: str, value: int, condition: Condition, stats: List[int], attack_type: AttackType, damage: int):
                """
        Initialize a Weapon item.

        Args:
            name (str): The name of the weapon item.
            value (int): The value of the weapon item.
            condition (Condition): The condition of the weapon item.
            stats (List[int]): List of stat values [physical_attack, physical_defense, magical_attack, magical_defense].
            attack_type (AttackType): The type of attack the weapon uses.
            damage (int): The damage value of the weapon.
        """
        super().__init__(name, value, condition, stats)
        if not isinstance(attack_type, AttackType):
            raise TypeError
        if not isinstance(damage, int) or damage < 0:
            raise ValueError
        self.__attack_type = attack_type
        self.__damage = damage

    @property
    def attack_type(self):
        return self.__attack_type
    
    @attack_type.setter
    def attack_type(self, attack_type: AttackType):
        if not isinstance(attack_type, AttackType):
            raise TypeError
        self.__attack_type = attack_type
    
    @property
    def damage(self):
        return self.__damage
    
    @damage.setter
    def damage(self, damage: int):
        if not isinstance(damage, int):
            raise ValueError
        self.__damage = damage
    
    def set_stats(self, stats: List[int]):
        if len(stats) != 4:
            raise ValueError
        for i in stats:
            if not isinstance(i, int):
                raise ValueError
        super().set_stats(stats[:-1])
        self.__damage = stats[-1]



if __name__ == "__main__":
    # Create a Loot item
    loot_item = Loot("Ancient Coin", 100, Condition.EXCELLENT)
    print(loot_item.item_info())  # Output: Item: Ancient Coin, Value: 100, Condition: EXCELLENT

    # Modify the stats of the Loot item based on its condition
    loot_item.set_stats(100)
    print(loot_item.item_info())  # Output: Item: Ancient Coin, Value: 125, Condition: EXCELLENT

    # Create an Armor item
    armor_item = Armor("Knight's Armor", 500, Condition.GOOD, [10, 20, 5, 15])
    print(armor_item.item_info())  # Output: Item: Knight's Armor, Value: 500, Condition: GOOD, Physical Attack: 10, Physical Defense: 20, Magical Attack: 5, Magical Defense: 15

    # Adjust the stats of the Armor item based on its condition
    armor_item.adjust_stats()
    print(armor_item.item_info())  # Output: Item: Knight's Armor, Value: 500, Condition: GOOD, Physical Attack: 10, Physical Defense: 20, Magical Attack: 5, Magical Defense: 15

    # Change the condition of the Armor item and adjust stats again
    armor_item.condition = Condition.BAD
    armor_item.adjust_stats()
    print(armor_item.item_info())  # Output: Item: Knight's Armor, Value: 500, Condition: BAD, Physical Attack: 5, Physical Defense: 10, Magical Attack: 2, Magical Defense: 7