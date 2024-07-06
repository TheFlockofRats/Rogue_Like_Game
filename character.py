from abc import ABC, abstractmethod
from item import Item, Armor, Weapon, Condition, AttackType
import random


class Character(ABC):
    def __init__(self, char_name: str):
        NO_ARMOR = Armor('N/A', 0, Condition.GOOD, [0, 0, 0, 0])
        BARE_HANDS = Weapon('Bare hands', 0, Condition.GOOD, [0, 0, 0, 0], AttackType.PHYSICAL, 2)
        self.__name = char_name
        self.__health = [25,25]
        self.__mana = [20,20]
        self.__physical_stats = [3,3]
        self.__magical_stats = [3,3]
        self.__luck = 5 + random.randint(-5, 5)
        self.__critical_percentage = 1
        self.__critical_modifier = 1.5
        self.__inventory = []
        self.__equipment = {NO_ARMOR['HEAD', 'BODY', 'HANDS', 'LEGS', 'FEET']}
        self.__weapon = BARE_HANDS

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name != '' and isinstance(new_name, str):
            self.__name = new_name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, new_health):
        if len(new_health) == 2 and new_health[0] == int and new_health[1] == int:
            self.__health = new_health

    @property
    def mana(self):
        return self.__mana

    @mana.setter
    def mana(self, new_mana):
        if new_mana[0] == int and new_mana[1] == int:
            self.__mana = new_mana

    @property
    def physical_stats(self):
        return self.__physical_stats

    @physical_stats.setter
    def physical_stats(self, new_physical_stats):
        self.__physical_stats = new_physical_stats

    @property
    def magical_stats(self):
        return self.__magical_stats

    @magical_stats.setter
    def magical_stats(self, new_magical_stats):
        self.__magical_stats = new_magical_stats

    @property
    def luck(self):
        return self.__luck

    @luck.setter
    def luck(self, new_luck):
        self.__luck = new_luck

    @property
    def critical_percentage(self):
        return self.__critical_percentage

    @critical_percentage.setter
    def critical_percentage(self, new_critical_percentage):
        self.__critical_percentage = new_critical_percentage

    @property
    def critical_modifier(self):
        return self.__critical_modifier

    @critical_modifier.setter
    def critical_modifier(self, new_critical_modifier):
        self.__critical_modifier = new_critical_modifier

    @property
    def inventory(self):
        return self.__inventory

    @inventory.setter
    def inventory(self, new_inventory):
        self.__inventory = new_inventory

    @property
    def equipment(self):
        return self.__equipment

    @equipment.setter
    def equipment(self, new_equipment):
        self.__equipment = new_equipment

    @property
    def weapon(self):
        return self.__weapon

    @weapon.setter
    def weapon(self, new_weapon):
        self.__weapon = new_weapon

    def phys_attack_modifier(self) -> int:
        pass

    def phys_defense_modifier(self) -> int:
        pass

    def magic_attack_modifier(self) -> int:
        pass

    def magic_defense_modifier(self) -> int:
        pass

    def deal_damage(self) -> (int, bool):
        critical_strike = random.randint(0,100)
        if critical_strike <= self.__critical_percentage:
            critical_strike_bool = True
        else:
            critical_strike_bool = False

        damage = random.randint(1, Weapon.damage)
        rand_num = random.randint(1,100)
        if rand_num <= (self.__critical_percentage + self.__luck):
            damage = floor(damage * self.__critical_modifier)
        return damage, critical_strike_bool

#test
    def take_damage(self, damage) -> None:
        pass

    def attack(self, target: Character) -> str:
        pass

    def equip(self, item: Item, position: str = None) -> None:
        pass

    def pick_up(self, item: Item) -> str:
        pass

    def drop(self, item: Item) -> (str, Item):
        pass


class Warrior(Character):
    pass

class Rouge(Character):
    def __init__(self, char_name):
        super().__init__()
        self.__luck += 10
        self.__critical_percentage = 0.1
        self.__critical_modifier = 2.5
        self.__health = [20,20]






class Mage(Character):
    def __init__(self, char_name):
        pass


class priest(Character):
    def __init__(self, char_name):
        pass










