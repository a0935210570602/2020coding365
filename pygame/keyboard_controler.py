class Keyboard_controler():
    keylist = []

    def addKey(self, key):  
        if not self.hasKey(key):
            self.keylist.append(key) 

    def printKey(self):
        for i in self.keylist:
            print(i)

    def hasKey(self, key):
        for i in self.keylist:
            if i == key:
                return True
        return False

    def deleteKey(self, key):
        if self.hasKey(key):
            self.keylist.remove(key)