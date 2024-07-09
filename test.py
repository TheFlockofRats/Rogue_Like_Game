import unittest
from enum import Enum
from typing import List
import math
from item import Condition, AttackType, Item, Loot, Armor, Weapon


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


if __name__ == "__main__":
    unittest.main()
