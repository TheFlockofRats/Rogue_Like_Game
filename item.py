from enum import Enum
from abc import ABC, abstractmethod
from typing import List
import math


class Condition(Enum):
    """
    The condition of an item.
    """
    EXCELLENT = 1
    GOOD = 2
    ACCEPTABLE = 3
    BAD = 4
    ABYSMAL = 5


class AttackType(Enum):
    """
    The type of attack an item can perform.
    """
    PHYSICAL = 1
    MAGICAL = 2


class Item(ABC):
    """
    Abstract base class of an item.

    Attributes:
        name (str): Name of the item.
        value (int): Value of the item in gold.
        condition (Condition): Condition state of the item.
    """

    def __init__(self, name: str, value: int, condition: Condition):
        """
        Initialize an Item.

        Args:
            name (str): Name of the item.
            value (int): Value of the item in gold.
            condition (Condition): Condition state of the item.
        """
        self.name = name
        self.value = value
        self.condition = condition


    @property
    def name(self) -> str:
        """
        str: Name of item.
        """
        return self.__name

    @name.setter
    def name(self, name: str):
        """
        Setter for the name attribute.

        Args:
            name (str): Name of the item.

        Raises:
            TypeError: If name is not a string.
            ValueError: If name has length less than 1.
        """
        if not isinstance(name, str):
            raise TypeError
        if len(name) < 1:
            raise ValueError
        self.__name = name

    @property
    def value(self) -> int:
        """
        int: Value of the item in gold.
        """
        return self.__value

    @value.setter
    def value(self, value: int):
        """
        Setter for the value attribute.

        Args:
            value (int): Value of the item in gold.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError
        if value < 0:
            raise ValueError
        self.__value = value

    @property
    def condition(self) -> Condition:
        """
        Condition: Condition state of the item.
        """
        return self.__condition

    @condition.setter
    def condition(self, condition: Condition):
        """
        Setter for the condition attribute.

        Args:
            condition (Condition): Condition state of the item.

        Raises:
            TypeError: If condition is not a Condition enum.
        """
        if not isinstance(condition, Condition):
            raise TypeError
        self.__condition = condition

    @abstractmethod
    def item_info(self) -> str:
        """
        Abstract method to get basic information about the item.

        Returns:
            str: Basic information about the item.
        """
        pass

    @abstractmethod
    def set_stats(self, stats: list[int]):
        """
        Abstract method to set the stats of the item based on list of integers.

        Args:
            stats (List[int]): List of integers representing stats.

        Raises:
            TypeError: If stats is not a list.
            ValueError: If stats list does not have the correct length or doesn't have an integer.
        """
        pass

    @abstractmethod
    def adjust_stats(self):
        """
        Abstract method to adjust the stats of the item based on its condition.
        """
        pass


class Loot(Item):
    """
    Class representing loot, inheriting from Item.
    """
    LOOT = (
        "Amulet of the Eternal Sun",
        "Ring of Shadows",
        "Cloak of the Celestial Winds",
        "Gloves of the Arcane Master",
        "Boots of Frostbite Resistance",
        "Pendant of the Moonlit Path",
        "Belt of Thundering Giants",
        "Elixir of Eternal Youth",
        "Scroll of Ancient Wisdom",
        "Orb of Void Echoes",
        "Crystal of Elemental Power",
        "Tome of Lost Secrets",
        "Chalice of Life",
        "Scepter of Timeless Kings",
        "Mask of the Spirit Walker",
        "Shard of the Fallen Star",
        "Phoenix Feather Charm",
        "Shadow Cloak",
        "Golden Gauntlets of Valor",
        "Emerald Eye of the Serpent",
        "Ruby Heart Pendant",
        "Diamond Shard",
        "Sapphire Tear",
        "Obsidian Skull",
        "Titanium Key",
        "Enchanted Mirror",
        "Mystic Horn",
        "Crown of Kings",
        "Ancient Relic",
        "Dragon Scale")

    def item_info(self) -> str:
        """
        Get basic information about the loot item.

        Returns:
            str: Basic information about the loot item.
        """
        return f"Item: {self.name}, Value: {self.value} gold, Condition: {self.condition.name}"

    def set_stats(self, stats: int):
        """
        Set the stats of the loot item based on a single integer stat.

        Args:
            stats (int): Integer representing the stats of the loot item.

        Raises:
            TypeError: If stats is not an integer.
            ValueError: If stats is less than 0.
        """
        if not isinstance(stats, int):
            raise TypeError
        if stats < 0:
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
        Adjust the stats of the loot item based on its condition.
        """
        pass


class Armor(Item):
    """
    Class representing armor, inheriting from Item.

    Attributes:
        Inherits attributes from Item class.
        physical_attack (int): Physical attack bonus of the armor.
        physical_defense (int): Physical defense bonus of the armor.
        magical_attack (int): Magical attack bonus of the armor.
        magical_defense (int): Magical defense bonus of the armor.
    """

    ARMOR = (
        "Dragonsteel Plate",
        "Shadowweave Robes",
        "Titanium Vanguard",
        "Celestial Mail",
        "Dreadnought Helm",
        "Soulforge Gauntlets",
        "Ebonsteel Greaves",
        "Phoenix Guard",
        "Moonstone Circlet",
        "Obsidian Aegis",
        "Silversilk Cloak",
        "Stormbreaker Helm",
        "Bloodbound Bracers",
        "Runic Chainmail",
        "Aetherial Vestments",
        "Wyrmscale Armor",
        "Echoesong Helm",
        "Venomshroud Mantle",
        "Frostforged Plate",
        "Thunderheart Robe",
        "Shadowmend Leggings",
        "Infernal Warplate",
        "Emberfury Boots",
        "Starlight Veil",
        "Nightmare Cloak",
        "Spectral Greaves",
        "Frostfire Crown",
        "Mystic Defender",
        "Voidwalkers",
        "Doomguard Pauldrons")

    def __init__(self, name: str, value: int, condition: Condition, stats: List[int]):
        """
        Initializes Armor.

        Args:
            name (str): Name of the armor.
            value (int): Value of the armor in gold.
            condition (Condition): Condition state of the armor.
            stats (List[int]): List of integers representing stats of the armor.
        """
        super().__init__(name, value, condition)
        self.set_stats(stats)

    @property
    def physical_attack(self) -> int:
        """
        int: Physical attack bonus of the armor.
        """
        return self.__physical_attack_modifier

    @property
    def physical_defense(self) -> int:
        """
        int: Physical defense bonus of the armor.
        """
        return self.__physical_defense_modifier

    @property
    def magical_attack(self) -> int:
        """
        int: Magical attack bonus of the armor.
        """
        return self.__magical_attack_modifier

    @property
    def magical_defense(self) -> int:
        """
        int: Magical defense bonus of the armor.
        """
        return self.__magical_defense_modifier

    def set_stats(self, stats: List[int]):
        """
        Set the stats of the armor based on a list of integers.

        Args:
            stats (List[int]): List of integers representing stats of the armor.

        Raises:
            TypeError: If stats is not a list of integers.
            ValueError: If stats list does not have the correct length or doesn't have integers.
        """
        if not isinstance(stats, list):
            raise TypeError
        if len(stats) != 4:
            raise ValueError
        for stat in stats:
            if not isinstance(stat, int):
                raise ValueError

        self.__physical_attack_modifier = stats[0]
        self.__physical_defense_modifier = stats[1]
        self.__magical_attack_modifier = stats[2]
        self.__magical_defense_modifier = stats[3]

    def adjust_stats(self):
        """
        Adjust the stats of the armor based on its condition.
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
        else:
            modifier = 1.0

        self.__physical_attack_modifier = math.floor(self.__physical_attack_modifier * modifier)
        self.__physical_defense_modifier = math.floor(self.__physical_defense_modifier * modifier)
        self.__magical_attack_modifier = math.floor(self.__magical_attack_modifier * modifier)
        self.__magical_defense_modifier = math.floor(self.__magical_defense_modifier * modifier)

    def item_info(self) -> str:
        """
        Get basic information about the armor.

        Returns:
            str: Basic information about the armor, including its bonuses.
        """
        return (
            f"Item: {self.name}, Value: {self.value} gold, Condition: {self.condition.name}\n"
            f"Physical Attack Modifier: {self.physical_attack}\n"
            f"Physical Defense Modifier: {self.physical_defense}\n"
            f"Magical Attack Modifier: {self.magical_attack}\n"
            f"Magical Defense Modifier: {self.magical_defense}"
        )


class Weapon(Item):
    """
    Class representing a weapon, inheriting from Item.

    Attributes:
        Inherits attributes from Item class.
        attack_type (AttackType): Type of attack the weapon uses.
        damage (int): Damage range of the weapon.
    """

    WEAPONS = weapon_names = (
        "Bloodmoon Blade",
        "Doomhammer",
        "Shadowstrike",
        "Dragonfang Axe",
        "Soulreaper Scythe",
        "Frostbite Dagger",
        "Stormcaller Staff",
        "Hellfire Crossbow",
        "Voidblade",
        "Thunderfury",
        "Eclipse Bow",
        "Venomfang Spear",
        "Mystic Wand",
        "Runeblade",
        "Starfall Bow",
        "Deathbringer Sword",
        "Celestial Staff",
        "Infernal Cleaver",
        "Whisperwind Bow",
        "Dreadscythe",
        "Dragonfire Wand",
        "Spectral Edge",
        "Blazefire Greatsword",
        "Moonshadow Dagger",
        "Riftblade",
        "Nightfall Axe",
        "Abyssal Trident",
        "Soulshatterer",
        "Harbinger of Doom",
        "Voidcaster")

    def __init__(self, name: str, value: int, condition: Condition, stats: List[int], attack_type: AttackType,
                 damage: int):
        """
        Initializes a Weapon.

        Args:
            name (str): Name of the weapon.
            value (int): Value of the weapon in gold.
            condition (Condition): Condition state of the weapon.
            stats (List[int]): List of integers representing stats of the weapon.
            attack_type (AttackType): Type of attack the weapon uses.
            damage (int): Damage range of the weapon.
        """
        super().__init__(name, value, condition)
        self.__attack_type = attack_type
        if not isinstance(damage, int):
            raise TypeError
        if damage < 0:
            raise ValueError
        self.__damage = damage
        self.set_stats(stats)


    @property
    def attack_type(self) -> AttackType:
        """
        AttackType: Type of attack the weapon uses.
        """
        return self.__attack_type

    @attack_type.setter
    def attack_type(self, value: AttackType):
        """
        Setter for the attack_type attribute.

        Args:
            value (AttackType): Type of attack the weapon uses.

        Raises:
            TypeError: If value is not an AttackType enum.
        """
        if not isinstance(value, AttackType):
            raise TypeError
        self.__attack_type = value

    @property
    def damage(self) -> int:
        """
        int: Damage range of the weapon.
        """
        return self.__damage

    @damage.setter
    def damage(self, value: int):
        """
        Setter for the damage attribute.

        Args:
            value (int): Damage range of the weapon.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError
        if value < 0:
            raise ValueError
        self.__damage = value

    def set_stats(self, stats: List[int]):
        """
        Set the stats of the weapon based on list of integers.

        Args:
            stats (List[int]): List of integers representing stats of the weapon.

        Raises:
            TypeError: If stats is not a list of integers.
            ValueError: If stats list does not have the correct length or doesn't have integers.
        """
        if not isinstance(stats, list):
            raise TypeError
        if len(stats) != 4:
            raise ValueError
        for stat in stats:
            if not isinstance(stat, int):
                raise ValueError

        self.__physical_attack_modifier = stats[0]
        self.__physical_defense_modifier = stats[1]
        self.__magical_attack_modifier = stats[2]
        self.__magical_defense_modifier = stats[3]

    def adjust_stats(self):
        """
        Adjust the stats of the weapon based on its condition.
        """
        condition_modifiers = {
            Condition.EXCELLENT: 1.25,
            Condition.GOOD: 1.0,
            Condition.ACCEPTABLE: 0.8,
            Condition.BAD: 0.5,
            Condition.ABYSMAL: 0.25
        }

        modifier = condition_modifiers[self.condition]

        self.__physical_attack_modifier = math.floor(self.__physical_attack_modifier * modifier)
        self.__physical_defense_modifier = math.floor(self.__physical_defense_modifier * modifier)
        self.__magical_attack_modifier = math.floor(self.__magical_attack_modifier * modifier)
        self.__magical_defense_modifier = math.floor(self.__magical_defense_modifier * modifier)
        self.__damage = math.floor(self.__damage * modifier)

    @property
    def physical_attack(self) -> int:
        """
        int: Physical attack bonus of the weapon.
        """
        return self.__physical_attack_modifier

    @property
    def physical_defense(self) -> int:
        """
        int: Physical defense bonus of the weapon.
        """
        return self.__physical_defense_modifier

    @property
    def magical_attack(self) -> int:
        """
        int: Magical attack bonus of the weapon.
        """
        return self.__magical_attack_modifier

    @property
    def magical_defense(self) -> int:
        """
        int: Magical defense bonus of the weapon.
        """
        return self.__magical_defense_modifier

    def item_info(self) -> str:
        """
        Get basic information about the weapon.

        Returns:
            str: Basic information about the weapon, including its bonuses, attack type, and damage range.
        """
        return (
            f"Item: {self.name}, Value: {self.value} gold, Condition: {self.condition.name}\n"
            f"Physical Attack Modifier: {self.physical_attack}\n"
            f"Physical Defense Modifier: {self.physical_defense}\n"
            f"Magical Attack Modifier: {self.magical_attack}\n"
            f"Magical Defense Modifier: {self.magical_defense}\n"
            f"Attack Type: {self.attack_type.name}\n"
            f"Damage: {self.damage}"
        )


if __name__ == "__main__":
    # cool = Loot("Diamond Sword", 200, Condition.GOOD)
    # print(cool.item_info())
    weapon_item = Weapon("Fire Sword", 200, Condition.EXCELLENT, [11, 20, 5, 10], AttackType.MAGICAL, 200)
    print(weapon_item.item_info())
    print("-----------------------------------------------")
    weapon_item.adjust_stats()
    print(weapon_item.item_info())
