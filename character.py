from abc import ABC, abstractmethod
from math import floor


from item import Item, Armor, Weapon, Condition, AttackType
import random


class Character(ABC):
    """ A class that creates the character's for the game
    ...

    Attributes
    ----------
    __init__(self, char_name: str)
            This is the constructor for a base character without any modifications
    NO_ARMOR:
        Set to the following - Armor('N/A', 0, Condition.GOOD, [0, 0, 0, 0])
    BARE_HANDS:
        Set to the following - Weapon('Bare hands, 0, Condition.GOOD, [0, 0, 0, 0], AttackType.PHYSICAL, 2)
    Self.__name: str
        The character's name, must be a non-empty string
    self.__health: List[int]
        The character's temporary health and maximum health are stored here, this is a 2 element list and must be ints
    self.__mana: List[int]
        The character's temporary mana and maximum mana are stored here as a list of integers.
    self.__physical_stats: List[int]
        The character's physical attack modifier and physical defense modifier are stored as a list of integers
    self.__magical_stats: List[int]
        tThe character's magical attack modifier and magical defense modifier stored as a list of integers
    self.__luck: int
        An integer that act's as a modifier used to determine the success of a critical strike.
    self.__critical_percentage: int
        This is the character's percentage chance to land a critical strike.
    self.___critical_modifier: float
        This is the character's damage multiplier when a critical strike is landed.
    self.__inventory: List[Item]
        This is the character's inventory where unequipped items are stored.
    self.__equipment: Dict[str, Armor]
        This is a dictionary representing a character's equipped items.
    self.__weapon: Weapon
        This is the character's equipped weapon

    Methods
    -------
    phys_attack_modifier(self) -> int
        This method will return an integer that totals the physical attack of a character, and modifiers from character's items
    phys_defense_modifier(self) -> int
        This method does the same as the phys_attack_modifier, but for physical defense instead
    magic_attack_modifier(self) -> int
        This method will return an integer that totals the magical attack of a character, and modifiers from character's items
    magic_defense_modifier(self) -> int
        This method like the magic_attack_modifier, does the same, but with magic defense instead.
    deal_damage(self) -> (int, bool)
        This method returns the total damage that would be dealt when an attack is successful and a boolean that represents if a critical strike was made
    take_damage(self, damage) -> None
        This method subtracts the damage from the temporary health of the character.
    attack(self, target: Character) -> str
        This method determines whether or not a character can attack a Creature, if so it will determine how much damage
    equip(self, item: Item, position: str=None) -> None
        This method passes in an Item that is either Armor or a Weapon and a position on the body to place the Item.
    pick_up(self, item: Item) -> str
        Puts an item into the Character's __inventory and returns a string to indicate it was picked up
    drop(self, item: Item) -> (str, Item)
        Removes an item from a Character's __inventory and returns it with a string to indicate that it was dropped.

    Exception's
    -------
    CharacterDeathException
        Allows a character that has or is going to below zero to have its slain message string set and its temp health set to zero
    """
    def __init__(self, char_name: str):
        """
        Parameters
        ----------
        __init__(self, char_name: str)
            This is the constructor for a base character without any modifications
        NO_ARMOR:
            Set to the following - Armor('N/A', 0, Condition.GOOD, [0, 0, 0, 0])
        BARE_HANDS:
            Set to the following - Weapon('Bare hands, 0, Condition.GOOD, [0, 0, 0, 0], AttackType.PHYSICAL, 2)
        Self.__name: str
            The character's name, must be a non-empty string
        self.__health: List[int]
            The character's temporary health and maximum health are stored here, this is a 2 element list and must be ints
        self.__mana: List[int]
            The character's temporary mana and maximum mana are stored here as a list of integers.
        self.__physical_stats: List[int]
            The character's physical attack modifier and physical defense modifier are stored as a list of integers
        self.__magical_stats: List[int]
            tThe character's magical attack modifier and magical defense modifier stored as a list of integers
        self.__luck: int
            An integer that act's as a modifier used to determine the success of a critical strike.
        self.__critical_percentage: int
            This is the character's percentage chance to land a critical strike.
        self.___critical_modifier: float
            This is the character's damage multiplier when a critical strike is landed.
        self.__inventory: List[Item]
            This is the character's inventory where unequipped items are stored.
        self.__equipment: Dict[str, Armor]
            This is a dictionary representing a character's equipped items.
        self.__weapon: Weapon
            This is the character's equipped weapon
        """
        NO_ARMOR = Armor('N/A', 0, Condition.GOOD, [0, 0, 0, 0])
        BARE_HANDS = Weapon('Bare hands', 0, Condition.GOOD, [0, 0, 0, 0], AttackType.PHYSICAL, 2)
        self.__name = char_name
        self.__health = [25, 25]
        self.__mana = [20, 20]
        self.__physical_stats = [3, 3]
        self.__magical_stats = [3, 3]
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
        """
        Calculates the total physical attack modifier including armor and weapon modifiers.
        
        Returns:
            int: The total physical attack modifier.
        """
        total_modifier = self.__physical_stats[0]
        
        for part in self.__equipment.values():
            total_modifier += part.physical_attack
        
        total_modifier += self.__weapon.physical_attack
        return total_modifier

    def phys_defense_modifier(self) -> int:
        """
        Calculates the total physical defense modifier including armor and weapon modifiers.
        
        Returns:
            int: The total physical defense modifier.
        """
        total_modifier = self.__physical_stats[1]
        
        for part in self.__equipment.values():
            total_modifier += part.physical_defense
        
        total_modifier += self.__weapon.physical_defense
        return total_modifier

    def magic_attack_modifier(self) -> int:
        """
        Calculates the total magic attack modifier including armor and weapon modifiers.
        
        Returns:
            int: The total magic attack modifier.
        """
        total_modifier = self.__magical_stats[0]
        
        for part in self.__equipment.values():
            total_modifier += part.magical_attack
        
        total_modifier += self.__weapon.magical_attack
        return total_modifier

    def magic_defense_modifier(self) -> int:
        """
        Calculates the total magic defense modifier including armor and weapon modifiers.
        
        Returns:
            int: The total magic defense modifier.
        """
        total_modifier = self.__magical_stats[1]
        
        for part in self.__equipment.values():
            total_modifier += part.magical_defense
        
        total_modifier += self.__weapon.magical_defense
        return total_modifier

    def deal_damage(self) -> (int, bool):
        d = Weapon.damage
        damage = random.randint(1, d)
        rand_num = random.randint(1, 100)
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

    def attack(self, target: Character, damage, critical_strike_bool) -> str:
        attacker = random.randint(1, 20)
        defender = random.randint(1, 20)
        if Weapon.attack_type == 1:
            attacker += Armor.physical_attack
            attacker += Armor.physical_defense

            defender += Armor.physical_attack
            defender += Armor.physical_defense

        elif Weapon.attack_type == 2:
            attacker += Armor.magical_attack
            attacker += Armor.magical_defense

            defender += Armor.magical_attack
            defender += Armor.magical_defense

        if critical_strike_bool is True:

            if attacker >= defender:
                target.deal_damage()
                if target.health[0] <= 0:
                    return f'{target} lost {damage} health and died with a critical hit from {self.__name}!'
                else:
                    return f'{target} lost {damage} health with a critical hit from {self.__name}!'

            else:
                if target.health[0] <= 0:
                    return f'{target} lost {damage} health and died from {self.__name}!'
                else:
                    return f'{target} lost {damage} health from {self.__name}!'

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
                self.__inventory.append(self.__eq.uipment[2])
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


class Creature(Character):

    def __init__(self, char_name):
        super().__init__(char_name)
        self.physical_stats = [random.randint(0, 8), random.randint(0, 8)]
        self.magical_stats = [random.randint(0, 8), random.randint(0, 8)]
        x = random.randint(20, 40)
        self.health = [x, x]
        self.equip(Weapon(random.choice(Weapon.WEAPONS), condition=Condition.GOOD, value=0,
                          stats=[random.randint(1,5) for _ in range(4)],
                          attack_type=(random.choice(list(AttackType))), damage=random.randint(2, 12)))
        self.__gold = random.randint(0, 25)


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

    def karate_kick(self, target: Creature):
        if self.__mana[0] >= 2:
            target.health[0] -= 3
            self.__mana[0] -= 2
            return f'{3} damage has been dealt to {target}'
        else:
            raise LowMana('Karate Kid ran out of stamina because he wrote too much code for this project')


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
        self.__weapon = Weapon('Practice Wand', 0, Condition.GOOD, [0, 0, 0, 0], AttackType.MAGICAL, 2)

    def cast_magic_missile(self, target: Creature) -> str:
        rand_damage = random.randint(5, 10)
        if self.__mana[0] >= 5:
            target.health[0] -= rand_damage
            self.__mana[0] -= 5
            return f'{rand_damage} damage has been dealt to {target}'
        else:
            raise LowMana('Gandalf ran out of mana because he is old and weak')



    def cast_fire_ball(self, target: list[Creature]) -> str:
        rand_damage = random.randint(10, 25)
        if self.__mana[0] >= 8:
            for i in range(len(target)):
                target[i].health[0] -= rand_damage
                return f'{self.__name} dealt {rand_damage} damage using FireBall'
        else:
            raise LowMana(f'{self.__name} ran out of mana because he is old and weak')

    def Thunderbolt(self, target: Creature):
        rand_damage = random.randint(6, 8)
        if self.__mana[0] >= 3:
            target.health[0] -= rand_damage
            self.__mana[0] -= 3
            return f'{self.__name} dealt {rand_damage} damage using Thunderbolt'
        else:
            raise LowMana(f'{self.__name} ran out of mana because he is old and weak')




class priest(Character):
    def __init__(self, char_name):
        super().__init__(char_name)

    def heal(self, target) -> str:
        rand_heal = random.randint(1, 8)
        if target.health[0] != 0:
            if self.__mana[0] >= 4:
                target.health[0] += rand_heal
                self.__mana[0] -= 4
                return f'{target} gained {rand_heal} health!'
            else:
                raise InvalidTarget(f'{target} cannot be healed!')
        else:
            raise InvalidTarget(f'{target} cannot be healed!')

    def resurrect(self, target):
        if target.health[0] == 0:
            if self.__mana[0] >= 10:
                half_health = floor(target.health[1] / 2)
                target.health[0] += half_health
                self.__mana[0] -= 10
                return f'{target} was resurrected from the dead!'
            else:
                return f'Not enough mana!'
        else:
            return f'{target} is not dead!'

    def manage_perish_affairs(self):
        if self.__mana[0] >= 15:
            self.__health[0] += 10
            self.__health[1] += 10
            self.__mana[0] -= 15
            return f'Pastor Joe feels 20 years younger'
        else:
            return f'Pastor Joe is out of mana and croaked'


class CharacterDeathException(Exception):
    def __init__(self, character):
        self.message = f'{character} was slain!'
        Character.health = [0, 25]


class LowMana(Exception):
    def __init__(self):
        pass


class InvalidTarget(Exception):
    def __init__(self):
        pass


class CannotEquipException(Exception):
    def __init__(self):
        pass












