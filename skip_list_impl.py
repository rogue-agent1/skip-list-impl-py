#!/usr/bin/env python3
"""Skip list — O(log n) expected search/insert/delete."""
import random
class SkipNode:
    def __init__(self,key=None,level=0):
        self.key=key;self.forward=[None]*(level+1)
class SkipList:
    def __init__(self,max_level=16,p=0.5):
        self.MAXLVL=max_level;self.p=p;self.header=SkipNode(None,max_level);self.level=0
    def _random_level(self):
        lvl=0
        while random.random()<self.p and lvl<self.MAXLVL: lvl+=1
        return lvl
    def insert(self,key):
        update=[None]*(self.MAXLVL+1);cur=self.header
        for i in range(self.level,-1,-1):
            while cur.forward[i] and cur.forward[i].key<key: cur=cur.forward[i]
            update[i]=cur
        lvl=self._random_level()
        if lvl>self.level:
            for i in range(self.level+1,lvl+1): update[i]=self.header
            self.level=lvl
        n=SkipNode(key,lvl)
        for i in range(lvl+1): n.forward[i]=update[i].forward[i];update[i].forward[i]=n
    def search(self,key):
        cur=self.header
        for i in range(self.level,-1,-1):
            while cur.forward[i] and cur.forward[i].key<key: cur=cur.forward[i]
        cur=cur.forward[0]
        return cur and cur.key==key
    def to_list(self):
        r=[];cur=self.header.forward[0]
        while cur: r.append(cur.key);cur=cur.forward[0]
        return r
def main():
    random.seed(42);sl=SkipList()
    for x in [3,6,7,9,12,19,17,26,21,25]: sl.insert(x)
    print(f"List: {sl.to_list()}")
    print(f"Search 19: {sl.search(19)}, Search 15: {sl.search(15)}")
if __name__=="__main__":main()
