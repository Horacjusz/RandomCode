from collections import deque
from random import randint
import time


def create_dataset(num) :
    inside = 0
    data = []
    
    for _ in range(num) :
        # value, 0->left 1->right, 0->pop 1->append
        increaser = randint(0,1)
        
        if increaser == 0 :
            if inside == 0 :
                increaser = 1
                inside += 1
            else :
                inside -= 1
        else :
            inside += 1
        
        data.append([0,randint(0,1),increaser])
    
    return data

    
class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class dqueue:
    def __init__(self, initial=None):
        self.size = 0
        self.sentinel = Node()
        self.sentinel.prev = self.sentinel
        self.sentinel.next = self.sentinel
        
        if isinstance(initial, list):
            for val in initial:
                self.append(val)
        elif initial is not None:
            self.append(initial)
            
    def pop_left(self):
        if self.size == 0:
            raise IndexError("Cannot pop from an empty deque")
        val = self.sentinel.next.value
        self.sentinel.next = self.sentinel.next.next
        self.sentinel.next.prev = self.sentinel
        self.size -= 1
        return val
    
    def pop(self):
        if self.size == 0:
            raise IndexError("Cannot pop from an empty deque")
        val = self.sentinel.prev.value
        self.sentinel.prev = self.sentinel.prev.prev
        self.sentinel.prev.next = self.sentinel
        self.size -= 1
        return val
    
    def append_left(self, val):
        new_node = Node(val, self.sentinel, self.sentinel.next)
        self.sentinel.next.prev = new_node
        self.sentinel.next = new_node
        self.size += 1
    
    def append(self, val):
        new_node = Node(val, self.sentinel.prev, self.sentinel)
        self.sentinel.prev.next = new_node
        self.sentinel.prev = new_node
        self.size += 1
        
    def to_list(self):
        current = self.sentinel.next
        list_val = []
        while current is not self.sentinel:
            list_val.append(current.value)
            current = current.next
        return list_val
        
    def print_all(self):
        print(self.to_list(), end=" <- dqueue\n")

        
dataset = create_dataset(1000000)

n = len(dataset)

mine = dqueue()
pythonish = deque()


mine_time = [0,0,0,0]
pythonish_time = [0,0,0,0]

mine_function = lambda : mine.pop()
pythonish_function = lambda : pythonish.pop()


for val, side, action in dataset :
    
    idx = 0
    
    if side == 0 :
        if action == 0 :
            mine_function = lambda : mine.pop_left()
            pythonish_function = lambda : pythonish.popleft()
        else :
            mine_function = lambda : mine.append_left(val)
            pythonish_function = lambda : pythonish.appendleft(val)
            idx = 1
    else :
        if action == 0 :
            mine_function = lambda : mine.pop()
            pythonish_function = lambda : pythonish.pop()
            idx = 2
        else :
            mine_function = lambda : mine.append(val)
            pythonish_function = lambda : pythonish.append(val)
            idx = 3
            
    start = time.time()
    mine_function()
    middle = time.time()
    pythonish_function()
    end = time.time()
    
    mine_time[idx] += (middle - start)
    pythonish_time[idx] += (end - middle)
    
names = ["popping left","appending left", "popping", "appending"]

python_entirety = 0
mine_entirety = 0

N = 4

for i, name in enumerate(names) :
    
    pythonish_val = pythonish_time[i]
    mine_val = mine_time[i]
    
    
    
    if pythonish_val < mine_val :
        val = (mine_val/pythonish_val)
        python_entirety += val
        print("Pythonish faster in",name,val,"times")
        print(pythonish_val, mine_val)
        print()
    elif pythonish_val > mine_val :
        val = (pythonish_val/mine_val)
        mine_entirety += val
        print("Mine faster in",name,val,"times")
        print(mine_val, pythonish_val)
        print()
    else :
        N -= 1
        print("EQUAL")
        print(mine_val)
        print()

if N == 0 : print("PERFECTLY EQUAL")

python_entirety /= 4
mine_entirety /= 4

if python_entirety > mine_entirety :
    print("Pythonish deque is faster",python_entirety,"times")
elif mine_entirety > python_entirety :
    print("Mine dqueue is faster",mine_entirety,"times")
else : print("Equal")