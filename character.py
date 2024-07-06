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
        self.__equipment = {'HEAD': NO_ARMOR, 'BODY': NO_ARMOR, 'HANDS': NO_ARMOR, 'LEGS': NO_ARMOR, 'FEET': NO_ARMOR}
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
        damage = random.randint(1, Weapon.damage)
        rand_num = random.randint(1,100)
        if rand_num <= (self.__critical_percentage + self.__luck):
            damage = floor(damage * self.__critical_modifier)
            critical_strike_bool = True

        else:
            critical_strike_bool = False
        return damage, critical_strike_bool

#test
    def take_damage(self, damage) -> None:
        temp_health = damage - self.__health[0]
        if temp_health < 1:
            raise CharacterDeathException

    def attack(self, target: Character) -> str:
        pass

    def equip(self, item: Item, position: str = None) -> None:
        if not isinstance(item, Weapon) or not isinstance(item, Armor):
            raise CannotEquipException

        if isinstance(item, Weapon):
            self.__inventory.append(self.__weapon)
            self.__weapon = item

        elif isinstance(item, Armor):

            if position == 'HEAD':
                self.__inventory.append(self.__equipment[0])
                self.__equipment[0] = item

            elif position == 'BODY':
                self.__inventory.append(self.__equipment[1])
                self.__equipment[1] = item

            elif position == 'HANDS':
                self.__inventory.append(self.__equipment[2])
                self.__equipment[2] = item

            elif position == 'LEGS':
                self.__inventory.append(self.__equipment[3])
                self.__equipment[3] = item

            elif position == 'FEET':
                self.__inventory.append(self.__equipment[4])
                self.__equipment[4] = item

            else:
                raise CannotEquipException

    def pick_up(self, item: Item) -> str:
        self.__inventory.append(item)
        return f'{item} was picked up'

    def drop(self, item: Item) -> (str, Item):
        self.__inventory.remove(item)
        return f'{item} was dropped'


class Warrior(Character):
    def __init__(self, char_name: str):
        super().__init__(char_name)

        # Warrior Health Stats:
        rand_num_health = random.randint(10, 20)
        self.__health[0] += rand_num_health
        self.__health[1] += rand_num_health

        # Warrior Physical Stats:
        rand_num_physical = random.randint(1, 4)
        self.__physical_stats[1] += rand_num_physical

        # Warrior Magical Stats:
        rand_num_magical = random.randint(0, 2)
        self.__magical_stats[0] = 0
        self.__magical_stats[1] -= rand_num_magical


class Rouge(Character):
    def __init__(self, char_name: str):
        super().__init__(char_name)
        self.__luck += 10
        self.__critical_percentage = 10
        self.__critical_modifier = 2.5
        self.__health = [20,20]
        rand_num_physical = random.randint(1,3)
        self.__physical_stats[1] -= rand_num_physical

class Mage(Character):
    def __init__(self, char_name: str):
        super().__init__(char_name)

        rand_num_magical = random.randint(1,3)
        self.__magical_stats[0] += rand_num_magical

        rand_num_physical = random.randint(0,2)
        self.__physical_stats[0] = 0
        self.__physical_stats[1] = 3 - rand_num_physical
        self.__health = [20, 20]
        rand_num_mana = random.randint(10, 15)
        self.__mana[0] += rand_num_mana
        self.__mana[1] += rand_num_mana
        self.__weapon = Weapon('Practice Wand', 0, 'GOOD', [0, 0, 0, 0], 'MAGICAL', 2)

    def cast_magic_missile(self, target: Creature) -> str:
        if self.__mana <= 5:
            pass
            # rand_num_damage = random.randint(5, 10)
            # target.health[0] -= rand_num_damage
        else:
            raise LowMana



    def cast_fire_ball(self, targets: List[Creatures]) -> str:
        if self.__mana <= 8:
            pass

        else:
            raise LowMana




class priest(Character):
    def __init__(self, char_name):
        pass

class CharacterDeathException(Exception):
    def __init__(self, character):
        self.message = f'{character} was slain!'
        Character.health = [0,25]

class LowMana(Exception):
    def __init__(self):
        self.message = f'Mana has been depleted!'

class InvalidTarget(Exception):
    def __init__(self):
        self.message = f'You cannot attack this target!'

class CannotEquipException(Exception):
    def __init__(self):
        self.message = f'Not a weapon/armor or unable to attach armor to designated location !'













