

class entity() :
    def __init__(self, name = "", Type = "", hp = 1, ad = 0, price = 0, inventory = {}, px = 0, py = 0, wx = 0, wy = 0, owners = {}, password = 0, level = 0, entityData = {}):
        self.name = name
        self.type = Type
        self.hp = hp
        self.ad = ad
        self.price = price
        self.inventory = inventory
        self.px = px
        self.py = py
        self.wx = wx
        self.wy = wy
        self.owners = owners
        self.password = password
        self.level = level
        self.entityData = entityData

    def getEntityData(self):
        return self.entityData

    def setEntityData(self, newEntityData, owner, password):
        if(owner in self.owners):
            if(self.owners.get(owner).getPassword() == hash(password)):
                self.entityData = newEntityData

    def getPassword(self):
        return self.password

    def getLevel(self):
        return self.level

    def setLevel(self, newLevel, owner, password):
        if(owner in self.owners):
            if(self.owners.get(owner).getPassword() == hash(password)):
                self.level = newLevel

    def getOwners(self):
        return self.owners

    def addOwner(self, newOwner, owner, password):
        if(owner in self.owners):
            if(self.owners.get(owner).getPassword() == hash(password)):
                self.owners[str(newOwner.getName())] = newOwner

    def removeOwner(self, ownerToRemove, owner, password):
        if(owner in self.owners):
            if(self.owners.get(owner).getPassword() == hash(password)):
                self.owners.pop(ownerToRemove.getName())

    def getName(self):
        return self.name
    
    def setName(self, newName, owner, password):
        if(owner in self.owners):
            if(self.owners.get(owner).getPassword() == hash(password)):
                self.name = newName

    def getType(self):
        return self.type

    def setType(self, newType, owner, password):
        if(owner in self.owners):
            if(self.owners.get(owner).getPassword() == hash(password)):
                self.type = newType

    def getHP(self):
        return self.hp

    def setHP(self, newHP, owner, password):
        if(owner in self.owners):
            if(self.owners.get(owner).getPassword() == hash(password)):
                self.hp = newHP

    def getAD(self):
        return self.ad

    def setAD(self, newAD, owner, password):
        if(owner in self.owners):
            if(self.owners.get(owner).getPassword() == hash(password)):
                self.ad = newAD

    def getPrice(self):
        return self.price

    def setPrice(self, newPrice, owner, password):
        if(owner in self.owners):
            if(self.owners.get(owner).getPassword() == hash(password)):
                self.price = newPrice

    def getInventory(self):
        return self.inventory

    def setInvetory(self, newInventory, owner, password):
        if(owner in self.owners):
            if(self.owners.get(owner).getPassword() == hash(password)):
                self.inventory = newInventory

    def getPX(self):
        return self.px

    def setPX(self, newPX, owner, password):
        if(owner in self.owners):
            if(self.owners.get(owner).getPassword() == hash(password)):
                self.px = newPX

    def getPY(self):
        return self.py

    def setPY(self, newPY, owner, password):
        if(owner in self.owners):
            if(self.owners.get(owner).getPassword() == hash(password)):
                self.py = newPY

    def getWX(self):
        return self.wx

    def setWX(self, newWX, owner, password):
        if(owner in self.owners):
            if(self.owners.get(owner).getPassword() == hash(password)):
                self.wx = newWX
    
    def getWY(self):
        return self.wy

    def setWY(self, newWY, owner, password):
        if(owner in self.owners):
            if(self.owners.get(owner).getPassword() == hash(password)):
                self.wy = newWY