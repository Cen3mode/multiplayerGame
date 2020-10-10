class mesh:
    def __init__(self, verticies=((0, 0, 0)), edges=((0, 0)), faces=((0, 0))):
        self.verticies = verticies
        self.edges = edges
        self.faces = faces

    def getMesh(self):
        return (self.verticies, self.edges, self.faces)


class entity:
    def __init__(
        self,
        name="",
        Type="",
        hp=1,
        ad=0,
        price=0,
        inventory={},
        pos=(0, 0, 0),
        mesh=mesh(),
        owners={},
        password=0,
        level=0,
        entityData={},
    ):
        self.name = name
        self.type = Type
        self.hp = hp
        self.ad = ad
        self.price = price
        self.inventory = inventory
        self.pos = pos
        self.mesh = mesh
        self.owners = owners
        self.password = password
        self.level = level
        self.entityData = entityData

    def getEntityData(self):
        return self.entityData

    def setEntityData(self, newEntityData, owner, password):
        if owner in self.owners:
            if self.owners.get(owner).getPassword() == hash(password):
                self.entityData = newEntityData

    def getPassword(self):
        return self.password

    def getLevel(self):
        return self.level

    def setLevel(self, newLevel, owner, password):
        if owner in self.owners:
            if self.owners.get(owner).getPassword() == hash(password):
                self.level = newLevel

    def getOwners(self):
        return self.owners

    def addOwner(self, newOwner, owner, password):
        if owner in self.owners:
            if self.owners.get(owner).getPassword() == hash(password):
                self.owners[str(newOwner.getName())] = newOwner

    def removeOwner(self, ownerToRemove, owner, password):
        if owner in self.owners:
            if self.owners.get(owner).getPassword() == hash(password):
                self.owners.pop(ownerToRemove.getName())

    def getName(self):
        return self.name

    def setName(self, newName, owner, password):
        if owner in self.owners:
            if self.owners.get(owner).getPassword() == hash(password):
                self.name = newName

    def getType(self):
        return self.type

    def setType(self, newType, owner, password):
        if owner in self.owners:
            if self.owners.get(owner).getPassword() == hash(password):
                self.type = newType

    def getHP(self):
        return self.hp

    def setHP(self, newHP, owner, password):
        if owner in self.owners:
            if self.owners.get(owner).getPassword() == hash(password):
                self.hp = newHP

    def getAD(self):
        return self.ad

    def setAD(self, newAD, owner, password):
        if owner in self.owners:
            if self.owners.get(owner).getPassword() == hash(password):
                self.ad = newAD

    def getPrice(self):
        return self.price

    def setPrice(self, newPrice, owner, password):
        if owner in self.owners:
            if self.owners.get(owner).getPassword() == hash(password):
                self.price = newPrice

    def getInventory(self):
        return self.inventory

    def setInvetory(self, newInventory, owner, password):
        if owner in self.owners:
            if self.owners.get(owner).getPassword() == hash(password):
                self.inventory = newInventory

    def getPos(self):
        return self.pos

    def setPos(self, newPos, owner, password):
        if owner in self.owners:
            if self.owners.get(owner).getPassword() == hash(password):
                self.pos = newPos

    def getMesh(self):
        return self.mesh

    def setMesh(self, newMesh, owner, password):
        if owner in self.owners:
            if self.owners.get(owner).getPassword() == hash(password):
                self.mesh = newMesh
