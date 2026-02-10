import random
class RandomizedSet:
    def __init__(self):
        self.randmset = set()
    def insert(self, val: int) -> bool:
        if val not in self.randmset:
            self.randmset.add(val)
            return True
        else:            
            return False
    def remove(self, val: int) -> bool:
        if val not in self.randmset:
            return False
        else:
            self.randmset.remove(val)            
            return True 
    def getRandom(self) -> int:
        self.randlist = list(self.randmset)
        n = len(self.randlist)-1
        ranInt = random.randint(0, n)
        return self.randlist[ranInt]

        


# Your randmset object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()