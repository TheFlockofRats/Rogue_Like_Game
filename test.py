import unittest
from enum import Enum
from typing import List
import math
from item import Condition, AttackType, Item, Loot, Armor, Weapon
from character import *

class TestItem(unittest.TestCase):
    def test_item_initial(self):
        item = Loot("Test Item", 50, Condition.GOOD)
        self.assertEqual(item.name, "Test Item")
        self.assertEqual(item.value, 50)
        self.assertEqual(item.condition, Condition.GOOD)

    def test_item_name(self):
        with self.assertRaises(TypeError):
            Loot(123, 50, Condition.GOOD)

    def test_item_value(self):
        with self.assertRaises(TypeError):
            Loot("Test Item", "50", Condition.GOOD)

    def test_item_condition(self):
        with self.assertRaises(TypeError):
            Loot("Test Item", 50, "Good Condition")

    def test_loot_set_stats(self):
        loot = Loot("Loot", 50, Condition.GOOD)
        loot.set_stats(100)
        self.assertEqual(loot.value, 100)

    def test_armor_initial(self):
        armor = Armor("Test Armor", 100, Condition.EXCELLENT, [10, 20, 5, 15])
        self.assertEqual(armor.name, "Test Armor")

    def test_armor_stats(self):
        with self.assertRaises(TypeError):
            Armor("Test Armor", 100, Condition.EXCELLENT, "AHHHH")

    def test_weapon_stats(self):
        with self.assertRaises(TypeError):
            Weapon("Test Weapon", 150, Condition.ACCEPTABLE, [15, 25, 10, 20], AttackType.PHYSICAL, "AHHH")

        with self.assertRaises(ValueError):
            Weapon("Test Weapon", 150, Condition.ACCEPTABLE, [15, 25, 10, 20], AttackType.PHYSICAL, -30)


class TestCharacter(unittest.TestCase):
    def test_name_int(self):
        with self.assertRaises(TypeError):
            Character(4)

    def test_name_list(self):
        with self.assertRaises(TypeError):
            Character([])

    def test_WARRIOR(self):
        with self.assertRaises(ValueError):
            Jeff = Warrior('Jeff')
            Jeff.name = ''


class Character_Test(unittest.TestCase):
    def test_warrior_karate_kick(self):
        with self.subTest("Testing Warrior karate kick"):
            self.warrior_name = "Rick"
            self.creature_name = "US_Government"
            self.creature = Creature(self.creature_name)
            self.warrior = Warrior(self.warrior_name)

            result = self.warrior.karate_kick(self.creature.name)
            self.assertEqual(result, '3 damage has been dealt to US_Government')
        
    def test_cast_magic_missile(self):
        with self.subTest("Testing Mage cast magic missile"):
            self.creature_name = "US_Government"
            self.mage_name = 'Morty'
            self.creature = Creature(self.creature_name)
            self.mage = Mage(self.mage_name)
            rand_damage = 5
            result = self.mage.cast_magic_missile(self.creature.name, rand_damage)
            self.assertEqual(result, '5 damage has been dealt to US_Government')

    def test_cast_fire_ball(self):
        with self.subTest("Testing Mage cast fire ball"):
            self.creature_name = "US_Government"
            self.mage_name = 'Morty'
            self.creature = Creature(self.creature_name)
            self.mage = Mage(self.mage_name)
            rand_damage = 5
            result = self.mage.cast_fire_ball(self.creature.name, rand_damage)
            self.assertEqual(result, 'Morty dealt 5 damage using FireBall')
    
    def test_thunderbolt(self):
        with self.subTest("Testing Mage cast Thunderbolt"):
            self.creature_name = "US_Government"
            self.mage_name = 'Morty'
            self.creature = Creature(self.creature_name)
            self.mage = Mage(self.mage_name)
            rand_damage = 5
            result = self.mage.cast_thunderbolt(self.creature.name, rand_damage)
            self.assertEqual(result, 'Morty dealt 5 damage using Thunderbolt')

    def test_heal(self):
        with self.subTest("Testing priest heal"):
            self.creature_name = "US_Government"
            self.priest_name = 'Father_Brown'
            self.creature = Creature(self.creature_name)
            self.priest = priest(self.priest_name)
            self.mage_name = 'Morty'
            self.mage = Mage(self.mage_name)
            rand_heal = 5
            result = self.priest.heal(self.mage, rand_heal)
            self.assertEqual(result, 'Morty gained 5 health!')

    def test_resurrect(self):
        with self.subTest("Testing priest resurrect"):
            self.creature_name = "US_Government"
            self.priest_name = 'Father_Brown'
            self.creature = Creature(self.creature_name)
            self.priest = priest(self.priest_name)
            self.mage_name = 'Morty'
            self.mage = Mage(self.mage_name)
            result = self.priest.resurrect(self.mage)
            self.assertEqual(result, 'Morty is not dead')

if __name__ == "__main__":
    unittest.main()
