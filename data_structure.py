class heap:
    def __init__(self):
        self.heap=[]
        
    def shift_down(self, k):
        heap_len=len(self.heap)
        while k < heap_len:
            if 2*k+2 < heap_len:
                if self.heap[k].cost<self.heap[2*k+1].cost or self.heap[k].cost<self.heap[2*k+2].cost:
                    t = self.heap[k]
                    if self.heap[2*k+1].cost<self.heap[2*k+2].cost:
                        self.heap[k] = self.heap[2 * k + 1]
                        self.heap[2 * k + 1] = t
                        k = 2 * k + 1
                    else:
                        t = self.heap[k]
                        self.heap[k] = self.heap[2 * k + 2]
                        self.heap[2 * k + 2] = t
                        k = 2 * k + 2
                else:
                    break
            elif 2*k+2 == heap_len:
                if self.heap[k].cost<self.heap[2*k+1].cost:
                    t = self.heap[k]
                    self.heap[k] = self.heap[2 * k + 1]
                    self.heap[2 * k + 1] = t
                    k = 2 * k + 1 
                else:
                    break
            else:
                break

        return 

    def shift_up(self, k):
        while k!=0:
            if self.heap[k].cost < self.heap[int((k - 1) / 2)].cost:
                t = self.heap[k]
                self.heap[k] = self.heap[int((k - 1) / 2)]
                self.heap[int((k - 1) / 2)] = t
                k = int((k - 1) / 2)
            else:
                break
        return 

    def pop(self):
        node=self.heap[0]
        self.heap[0]=self.heap[-1]
        del(self.heap[-1])
        self.shift_down( 0)
        return node

    def insert(self, node):
        self.heap.append(node)
        self.shift_up(len(self.heap)-1)
        return 


    
class FIFO:
    def __init__(self):
        self.queue=[]
        
    def pop(self):
        node=self.queue[0]
        del self.queue[0]
        return node
    
    def push(self, node):
        self.queue.append(node)
        
class FILO:
    def __init__(self):
        self.queue=[]
        
    def pop(self):
        node=self.queue[-1]
        del self.queue[-1]
        return node
    
    def push(self, node):
        self.queue.append(node)
        

class priority_queue():
    def __init__(self):
        self.queue=[]
        
    def pop_min(self):
        index=-1
        t=float('inf')
        for i in range(len(self.queue)):
            if self.queue[i].value<t:
                insex=i
                t=self.queue[i].value
        node=self.queue[insex]
        del self.queue[insex]
        return node
    
    def pop_max(self):
        index=-1
        t=-float('inf')
        for i in range(len(self.queue)):
            if self.queue[i].value>t:
                insex=i
                t=self.queue[i].value
        node=self.queue[insex]
        del self.queue[insex]
        return node
    
    def push(self, node):
        self.queue.append(node)
        
        
def Manhattan_Distance(Node1, Node2):
    distance=abs(Node1.x-Node2.x)+abs(Node1.y-Node2.y)
    return distance

def Euclidean_distance(Node1, Node2):
    distance=((Node1.x-Node2.x)**2+(Node1.y-Node2.y)**2)**0.5
    return distance