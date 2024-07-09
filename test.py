import unittest
from enum import Enum
from typing import List
import math
from item import Condition, AttackType, Item, Loot, Armor, Weapon


# THIS IS FOR THE ITEM CLASS
class TestItem(unittest.TestCase):
    def test_item_initialization(self):
        item = Loot("Test Item", 50, Condition.GOOD)
        self.assertEqual(item.name, "Test Item")
        self.assertEqual(item.value, 50)
        self.assertEqual(item.condition, Condition.GOOD)

    def test_loot_set_stats(self):
        loot = Loot("Test Loot", 50, Condition.GOOD)
        loot.set_stats(100)
        self.assertEqual(loot.value, 100)

    def test_weapon_stats_validation(self):
        with self.assertRaises(TypeError):
            # Does not raise TypeError - looking into it
            Weapon("Test Weapon", 150, Condition.ACCEPTABLE, [15, 25, 10, 20], AttackType.PHYSICAL, "30")

        with self.assertRaises(ValueError):
            Weapon("Test Weapon", 150, Condition.ACCEPTABLE, [15, 25, 10, 20], AttackType.PHYSICAL, -30)

    def test_item_condition_validation(self):
        with self.assertRaises(TypeError):
            Loot("Test Item", 50, "Good Condition")

            
if __name__ == "__main__":
    unittest.main()
