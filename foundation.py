from typing import Tuple, Dict, List

class Entity:
    def __init__(
        self,
        name: str="",
        type: str="",
        hp: int=1,
        ad: int=0,
        price: int=0,
        inventory: List=[],
        pos: List[int]=[0, 0],
        char: str="",
        owners: Dict={},
        password: int=0,
        level: int=0,
        entityData: List=[],
        color:  Tuple[int,int,int] = (255,255,255),
        transparent: bool = False,
        collision: bool = True,
    ):
        self.name = name
        self.type = type
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
        self.color = color
        self.transparent = transparent
        self.collision = collision

    def move(self, byX: int, byY: int):
        self.pos[0] += byX
        self.pos[1] += byY

    def tp(self, destX: int, destY: int):
        self.pos = (destX, destY)

    def give(self, thing):
        pass
