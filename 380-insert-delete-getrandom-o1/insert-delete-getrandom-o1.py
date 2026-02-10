import random
class RandomizedSet:    
    def __init__(self):
        self.count = defaultdict(int)
    def insert(self, val: int) -> bool:
        if self.count[val] > 0 :
            return False
        else:
            self.count[val] += 1
            return True
    def remove(self, val: int) -> bool:
        if self.count[val] > 0:
            self.count[val] -= 1
            return True
        else:          
            return False 
    def getRandom(self) -> int:
        self.val = [i for i in self.count.keys() if self.count[i] > 0]
        n = len(self.val)-1
        ranInt = random.randint(0, n)
        return self.val[ranInt]

        


# Your randmset object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()