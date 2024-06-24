# Rogue_Like_Game
CIS 163 project 2

Prior to the graphical power houses that you see output by AAA studios, games began as text-based distractions. This era of gaming forced the user to imagine the adventures you went on, rather than showing you directly. Although this seems arcane, there are still quite a few indie devs out there making these games. The reason for this is that they are highly customizable, systems heavy, and relatively easy to program.
For this project, you will be writing a very basic rogue-like game. A rogue-like (I am not going to argue the difference between rogue-like and a rogue-lite, it's simply not worth our time because game genre's are pointless things to argue about) consists of an adventurer or adventurers often moving from one room to another in a dungeon. Along the way the user may find wonderous treasure that could make them rich, new equipment to increase your odds of survival, and creatures awaiting your arrival, hoping for an easy meal.

Our game will have four character arc types (more commonly known as "classes" but we will not be using that term for this project to avoid any confusion). These arc types are:

Warrior - Characters that can take a beating more so than others. These characters tend to be more focused on dealing out physical damage
Rogues - Characters that can deal out high amounts of physical damage with increased chances of doing critical damage. These characters are often not seen as someone who can take a hit.
Mage - These characters tend to deal with the world of arcane and will cast powerful spells to deal damage using source of power referred to as mana. They are not great in physical combat.
Priests - These characters do not favor combat. Rather their skills remain in the world of healing. These characters are known for their ability to heal the wounds of their compatriots. There have been rumors that they may even bring back a fallen comrade from the brink of death.
For this game, a party of up to four characters can delve into the dungeons for riches and glory.

Game Structure
Our game will be made of the following files:

character.py - This will hold the code for the types of characters in the game.
dungeon.py - This will hold the dungeon class that links one room to another with each room containing some monsters, and items.
item.py - There are different types of items. This file will hold those classes.
game.py - This file runs the engine of the game. This will be provided for you.
Step One - dungeon.py
The first phase of this project will have you create the Dugeon class. This will be a fairly simple class as we will be simply using it to hold information. The Dungeon class should have the following instance variables:

__name: str - Name for the dungeon. Cannot be blank.
__description: str - A brief description of the dungeon.
__items: List[Item] - A list of items that hold the contents found in the Dungeon.
__creatures: List[Creature] - Holds all of the creatures in a given Dungeon.
__prior: Dungeon - The previous Dungeon the players came from.
__next: Dungeon - The next Dungeon the players came move to.
The Dungeon class should have the following properties( created via the use of @property (readable) and @property.setter (writable) decorators as described in class). Make sure the setter enforces any restrictions.

name - Both readable and writable. underlying instance variable is __name. Name must be a string and have a length of 1 or more. Raise a TypeError or a ValueError respectively if it doesn't meet the above conditions.
description - Both readable and writable. The underlying instance variable is __description. The new description must be a string and have a length of 1 or more. Raise a TypeError or a ValueError respectively if it doesn't meet the above conditions.
creatures - Readable. The underlying instance variable is __creatures.
items - Readable. The underlying instance variable is __items.
next - Readable and writable. Returns the next Dungeon.
previous - Readable and writable. Returns the previous Dungeon.
The Dungeon class should have the following methods:

__init__(self, name, description) -> None: The constructor for a dungeon. A dungeon will hold a __name and a __description. Pass these in as parameters and set the instance variables of the class to them. Initialize __items as a list that will hold 0 to 4 random items. Initialize __creatures as a list that will hold 0 to 5 random creatures. Initialize both __next and __previous to None. These will keep track of the next and previous Dungeon objects. This will be how we traverse further in or out of the dungeon.
The initialized __items will be a list of between 0 and 4 random items. There is a 50% chance that each item it will be a random Loot item, 30% chance that it will be a Armor item, and a 20% chance that it will be a Weapon item.
Loot items will have a name, a random condition assigned, and a random value between 5-50 gold.
Armor items will have a random name, a random condition assigned, and a random value between 0-10 gold. Each of the stats will be randomly set between 0-3.
Weapon will have the same randomization as Armor items, but will be randomly assigned an AttackType and damage set between 2-12.
The initialized __creatures will be a list of 0 and 4 random Creatures.
Each creature will be given a random name when instantiated.
show_creatures(self) -> str: This method returns a string of the list of creature names separated by a comma.
check_creature(self, creature_name: str) -> bool: This method returns a boolean of whether or not a creature is in the Dungeon by searching through __creatures using a string.
show_items(self) -> str: This method returns a string of the list of items separated by a comma in the following format: "Needle - Weapon, Helm of Forgetting - Armor, Lamp - Loot".
check_item(self) -> bool: This method returns a boolean of whether or not an item is in the Dungeon by searching through __items using a string.
pick_up_item(self, item_name: str, target: Character) -> str: This method searches for an item in the room by a given name and adds it to the inventory of the target Character. If the the item is not in the room, return the string - 'Item not found!'. Utilize the Character method pick_up(item: Item) to return a string that the item was placed into the Character's inventory.
drop_item(self, item_name: str, target: Character) -> str: This method searches for an item in the target Character's __inventory and returns it back to the Dungeon.
__str__(self) -> str: A string override to return the details of the room. It should look something like the following:
Room Name: The Hole
Description: A room with the exit 10 feet off the ground.
===========================================================================
Creatures: Shadow Beast, Orgre, Skeleton Man
---------------------------------------------------------------------------
Items: Death Bringer - Weapon, Steel Gauntlets - Armor, Pot of Greed - Loot
Step Two - item.py
We will use polymorphism through inheritance to create our various items. We will also be utilizing abstract classes and a couple of abstract methods throughout. There will be four classes for this portion: Item, Loot, Armor, Weapon. You will also be utilizing a two different enums we discussed earlier in class which are Condition and AttackType.

Enums
Condition: This is an enum that has the following states:
EXCELLENT
GOOD
ACCEPTABLE
BAD
ABYSMAL
AttackType: This is an enum that has the following states:
PHYSICAL
MAGICAL
Item Class
Start by creating the Item class in item.py. This will be an abstract class.

The Item class has the following attributes:

__name: A string that holds the name of the item. It must be a string and have length of 1 or more. If it isn't a string raise a TypeError and a ValueError if it has an invalid length
__value: An integer that holds the value in gold of the given item. If it isn't an integer raise a TypeError and a ValueError if it worth less than 0 gold.
__condition: A Condition state that holds its given condition. If assigned anything other than a Condition raise a TypeError.
Write readable and writeable properties for each attribute. Drop the __ from their names.

Write the following methods as abstract methods:

item_info(self) -> str: This method provides a string of the basic information of the Item.
set_stats(self, stats: (List[int], int): This method will set the stats of an Item based on the given list.
adjust_stats(self): This method will adjust the stats of a given item based on its Condition
Loot Class
This class will inherit Item. Override the following methods:

item_info(self): Provide basic information much like the Item class using super().
set_stats(self, stats: int): This will change the value of an item based on the condition. It will modify the item's value by the a percentage and then rounded down to the nearest integer. Please use the table below as a reference.
Condition	Modifier
EXCELLENT	125%
GOOD	100%
ACCEPTABLE	80%
BAD	50%
ABYSMAL	10%
 	
 	
Armor Class
The armor class inherits the Item class. It adds four additional attributes:

__physical_attack_modifier: int This represents the physical attack bonus.
__physical_defense_modifier: int This represents the physical defense bonus.
__magical_attack_modifier: int This represents the magic attack bonus.
__magical_defense_modifier: int This represents the magic defense bonus.
Create readable only properties for the above attributes. They should read like the following:

physical_attack for __physical_attack_modifier
physical_defense for __physical_defense_modifier
magical_attack for __magical_attack_modifier
magical_defense for __magical_defense_modifier
Override the following methods:

__init__(self, name: str, value: int, condition: Condition, stats: List[int]): Utilize super() to set the name, value, and condition. Then utilize set_stats(self, stats) to set the new attributes listed above.
set_stats(self, stats: List[int]): This method sets both the physical and magical attributes listed above. It will take in a list that must have a length of 4 and every element must be an integer. Raise a TypeError, ValueError, and ValueError respectively.
adjust_stats(self): This method adjusts all of the physical and magical attributes by the following percentage rounded down to the nearest integer. Reference the following table for the modifiers.
item_info(self): Provide basic information much like the Item class, but be sure to include all four of its modifiers.
Condition	Modifier
EXCELLENT	125%
GOOD	100%
ACCEPTABLE	80%
BAD	50%
ABYSMAL	25%
 	
 	
Weapon Class
The weapon class holds the same attributes as the armor class with the exception of two more additions. They are as follows:

__attack_type: AttackType This attribute dictates the type of attack the weapon uses
__damage: int This attribute dictates how much damage as an integer the weapon can deal. When being used in an attack, the weapon will deal out damage between 1-__damage.
Create readable and writeable properties for both __attack_type and __damage.

Ensure that __attack_type is an AttackType. If it isn't, raise a TypeError.
Ensure that __damage is sent to an integer and it must be greater than -1. Raise a TypeError or ValueError respectively.
Override the following methods:

set_stats(self, stats: List[int]): This function is the same as Armor's, but __damage must also be set.
adjust_stats(self): This function is the same as Armor's, but __damage must also be modified.
item_info(self): Provide basic information much like the Item class, but be sure to include all four of its modifiers in addition to its attack type and damage.
Step Three - character.py
After all of the above have been completed, we may now begin to develop the various character arc types for the game itself. This section will cover the four classes and the various exceptions.

Exceptions
Write each of the following custom exceptions at the bottom of your file. Write all other code above these. Each of the following exceptions are barebone and can just be created without the need of a constructor.

LowMana: Exception This is an exception that is raised when a method is attempted when a user does not have enough mana
InvalidTarget: Exception This is an exception that is raised when the target of a method does not meet the requirements to be targeted.
CannotEquipException: Exception This is an exception raised when an Item is considered unequipable (not Armor or a Weapon) or has been tried to be attached to an invalid position on the body.
Character Class
The Character class is an abstract class that all of the arc types rely on for existing. This is the keystone for the rest of this project. Many of the character actions are executed through this template.

The Character class has the following constants:

NO_ARMOR: set it to the following - Armor('N/A', 0, Condition.GOOD, [0, 0, 0, 0])
BARE_HANDS: set it to the following - Weapon('Bare hands, 0, Condition.GOOD, [0, 0, 0, 0], AttackType.PHYSICAL, 2) The Character class should have the following instance variables:
__name: str, the character's name, must be a string and cannot be empty
__health: List[int], the character's temporary health and maximum health are stored here. This must be a list of 2 and both elements must be integers.
__mana: List[int], the character's temporary mana and maximum mana are stored here as a list of integers.
__physical_stats: List[int], the character's physical attack modifier and physical defense modifier are stored as a list of integers.
__magical_stats: List[int], the character's magical attack modifier and magical defense modifier are stored as a list of integers.
__luck: int, an integer that act's as a modifier to how lucky a character is. This is used to determine the success of a critical strike.
__critical_percentage: int, this is the character's percentage chance to land a critical strike.
___critical_modifier: float, this is the character's damage multiplier when a critical strike is landed.
__inventory: List[Item], this is the character's inventory where unequipped items are stored.
__equipment: Dict[str, Armor], this is a dictionary representing a character's equipped items.
__weapon: Weapon, this is the character's equipped weapon.
The Character class should have the following properties. Ensure that setter properties enforce any restrictions on valid values.

name: readable and writable, underlying instance variable for __name.
health: readable and writable, underlying instance variable __health.
mana: readable and writable, underlying instance variable __mana.
physical_stats: readable and writable, underlying instance variable __physical_stats
magical_stats: readable and writable, underlying instance variable __magical_stats
luck: readable and writable, underlying instance variable __luck
critical_precentage: readable and writable, underlying instance variable __critical_percentage
critical_modifier: readable and writable, underlying instance variable __critical_modifier
inventory: readable, underlying instance variable __inventory
equipment: readable, underlying instance variable __equipment
weapon: readable and writable, underlying instance variable __weapon
inventory: readable, underlying instance variable __inventory
The Character the following methods need to be implemented:

__init__(self, char_name: str): This is the constructor for a base character without any modifications. Set the attributes to the following
__name: set this to the argument
__health: set this to [25, 25]
__mana: set this to [20, 20]
__physical_stats & __magical_stats: set both of these to [3, 3]
__luck: set this to 5 + a random number between -5-5
__critical_percentage: set this to 1
__critical_modifier: set this to 1.5
__inventory: set this to an empty list
__equipment: set this to a dictionary with the following using the NO_ARMOR constant. as the value for the following keys: 'HEAD', 'BODY', 'HANDS', 'LEGS', 'FEET'
__weapon: set this to the constant BARE_HANDS
phys_attack_modifier(self) -> int: This method will return an integer that totals the physical attack of a character with that of the physical attack modifier from every piece of Armor equipped and the Weapon's modifier added to it as well.
phys_defense_modifier(self) -> int: This method does the same as the above, but for physical defense instead.
magic_attack_modifier(self) -> int:This method does the same as the previous one, but with magic attack instead.
magic_defense_modifier(self) -> int: This method like the others above, does the same, but with magic defense instead.
deal_damage(self) -> (int, bool): This method returns the total damage that would be dealt when an attack is successful and a boolean that represents if a critical strike was made. The damage is a random number between 1 and the damage of the character's equipped weapon. In addition, a random number is generated between 1 and 100. If this number is less than or equal to the __critical_percentage + __luck, we multiply the damage by the __critical_modifier rounded down to the nearest integer. Return the total damage and whether or not a critical strike was achieved.
take_damage(self, damage) -> None: This method subtracts the damage from the temporary health of the character. Ensure that if the temporary health falls below 1, a CharacterDeathException is raised.
attack(self, target: Character) -> str: This method determines whether or not a character can attack a Creature. If it does, the amount of damage dealt by the Character is determined and then dealt to the target. To determine whether or not a Character hits a target, assign a random number for the attacker and the defender with a random number between 1-20. Then determine the type of attack the attacker is using based on their Weapon's AttackType. Then add the appropriate attack modifier to the attacker's number. Then add the appropriate defense modifier to the defender's number. If the attacker's number is greater than or equal to the defender's number, the attack is successful and you now need to begin to deal damage. Return a string that state's the attacker's name, how much damage was dealt to the defender, and the defender's name (see the example below for reference). If the attack happens to be a critical hit, modify that string to signify it. If the target dies, add a message stating it.
'Arya Joy dealt 10 damage to The Witch in Glass.'
'Critical hit! Faye dealt 10 damage to Spike.'
'Asuka dealt 10 damage to Shinji. Shinji was slain!'
equip(self, item: Item, position: str=None) -> None: This method passes in an Item that is either Armor or a Weapon and a position on the body to place the Item. If the Item is a Weapon a position is not needed and simply place the previous Weapon into the Character's __inventory and set the __weapon to the item. If the Item is Armor, replace the Item at the position with the item and place the previous Item into the Character's __inventory. If the Item is not Armor or a Weapon or the position is not in __equipment raise a CannotEquipException.
pick_up(self, item: Item) -> str: Put the item into the Character's __inventory and returns a string to indicate it was picked up.
drop(self, item: Item) -> (str, Item): Removes an item from a Character's __inventory and returns it with a string to indicate that it was dropped.
CharacterDeathException
Create a custom exception called CharacterDeathException and do the following:

allow a parameter called character. This allows the user to pass in the object whose health fell to or below 0.
set the self.message to a string using the following format: "Jimmy was slain!"
set the temporary health of the character to 0
Warrior Class
The Warrior class is meant to create a fighter that specializes in physical combat. They will have a greater amount of health, a greater physical defense, but little magical defense.

Override the __init__() and make sure to add the following changes:

Adjust the temporary and maximum health by adding randomly between 10-20 to the base stat
Increase the physical defense by a random between 1-4.
Set the magical attack to 0 and subtract a random number between 0-2 from the base magical defense.
Rogue Class
The Rogue class is meant to be able to deal higher amounts of damage by utilizing critical strikes. This is at the cost of lower physical and magical stats overall, but gains greater luck, critical_percentage, and critical_modifier

Override the __init__() and make sure to add the following changes:

Mage Class
The Mage class is meant to prioritize using magic spells to deal high amounts of damage, over traditional forms of combat. Mages often have higher amounts of mana and magical stats.

Override the __init__() and make sure to add the following changes:

magical_attack should be increased by a random integer between 1-3
physical_attack must be set to 0 and physical_defense must be set to 3 - a random number between 0-2.
set the temporary and maximum health to 20
set the mana to the base amount + a random number between 10-15.
Equip a weapon with the following:
name: 'Practice Wand'
value: 0
condition: GOOD
stats: [0, 0, 0, 0]
attack_type: MAGICAL
daamge: 2
Add the following methods:

cast_magic_missile(self, target: Creature) -> str: This method will deal damage to a target between 5-10 randomly. However, the spell can only be cast if the character has 5 mana or more. Reduce the amount of mana. If there isn't enough mana, raise a LowMana exception. Return a string output regarding damage dealt or not having enough mana. Examples are listed below.
LowMana - 'Gandalf tried to cast magic missile, but only pretty lights came out. You need more mana!'
Damage dealt - 'Gandalf dealt 10 damage to Sauron using magic missile.'
Damage dealt resulting in death - 'Gandalf dealt 10 damage to Sauron using magic missile. Sauran was slain!'
cast_fire_ball(self, targets: List[Creatures]) -> str: Similar to magic missile, cast_fire_ball() requires 8 mana and will deal between 10-25 damage to all enemy creatures in the room. Use the examples listed below for the return.
LowMana - 'Gandalf tried to cast fire ball, but only sparks came out. You need more mana!'
Damage dealt - 'Gandalf dealt 10 damage to Sauron using fire ball.'
Damage dealt resulting in death - 'Gandalf dealt 10 damage to Sauron using fire ball. Sauron was slain!'
Priest Class
The Priest is a support character type. They are capable of healing party members and even bringing them back from the dead. That is of course if they enough mana. The Priest makes no changes to the base class constructor.

Add the following methods:

heal(self, target) -> str: Select a target to heal as long as they aren't dead and you have at least 4 mana. heal the target with a random amount of health between 1-8. Reduce the mana by 4. If there isn't enough mana or the target is dead, raise an InvalidTarget exception. Return one of the following messages.
'Grog gained 6 health!'
'Grog cannot be healed!'
resurrect(self, target) -> str: This method selects a target and brings them to half of their health rounded down for the cost of 10 mana. If the target isn't dead, raise an InvalidTarget exception. Return the following one of the following messages:
'Not enough mana!'
'Grog isn't dead!'
'Grog was brought back from the void!'
