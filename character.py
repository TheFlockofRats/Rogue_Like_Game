<<<<<<< HEAD
from abc import ABC, abstractmethod
from item import Item, Armor, Weapon

class Character(ABC):
    def __init__(self, name: str, health: list[int], mana: list[int], physical_stats: list[int], magical_stats: list[int], luck: int, critical_percent: int, critical_modifier: float, inventory: list[Item], equipment: dict[str, Armor], weapon: Weapon ):
        self.__name =
=======
>>>>>>> 868707c1e01d09e6d6a46741c963e2116cc3d81d
