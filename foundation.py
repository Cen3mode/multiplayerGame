from typing import Tuple, Dict, List

class entity:
    def __init__(
        self,
        name: str="",
        Type: str="",
        hp: int=1,
        ad: int=0,
        price: int=0,
        inventory: Dict={},
        pos: Tuple[int,int]=(0, 0),
        char: str="",
        owners: Dict={},
        password: int=0,
        level: int=0,
        entityData: Dict={},
    ):
        self.name = name
        self.type = Type
        self.hp = hp
        self.ad = ad
        self.price = price
        self.inventory = inventory
        self.pos = pos
        self.char = char
        self.owners = owners
        self.password = password
        self.level = level
        self.entityData = entityData

    def move(self, byX: int, byY: int):
        self.pos += (byX, byY)
