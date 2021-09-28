#heap operation
def shift_down(heap, k):
    heap_len=len(heap)
    while k < heap_len:
        if 2*k+2 < heap_len:
            if heap[k].cost<heap[2*k+1].cost or heap[k].cost<heap[2*k+2].cost:
                t = heap[k]
                if heap[2*k+1].cost<heap[2*k+2].cost:
                    heap[k] = heap[2 * k + 1]
                    heap[2 * k + 1] = t
                    k = 2 * k + 1
                else:
                    t = heap[k]
                    heap[k] = heap[2 * k + 2]
                    heap[2 * k + 2] = t
                    k = 2 * k + 2
            else:
                break
        elif 2*k+2 == heap_len:
            if heap[k].cost<heap[2*k+1].cost:
                t = heap[k]
                heap[k] = heap[2 * k + 1]
                heap[2 * k + 1] = t
                k = 2 * k + 1 
            else:
                break
        else:
            break
            
    return heap

def shift_up(heap, k):
    while k!=0:
        if heap[k].cost < heap[int((k - 1) / 2)].cost:
            t = heap[k]
            heap[k] = heap[int((k - 1) / 2)]
            heap[int((k - 1) / 2)] = t
            k = int((k - 1) / 2)
        else:
            break
    return heap

def heap_pop(heap):
    node=heap[0]
    heap[0]=heap[-1]
    del(heap[-1])
    heap=shift_down(heap, 0)
    return node
    
def heap_insert(heap, node):
    heap.append(node)
    heap=shift_up(heap, len(heap)-1)
    return heap

from maze_genernate import maze

file_path='maze-2.txt'

maze=maze(file_path)

#node  has been checked
openset=[]
#node has not been checked
closedset = []

# add start node
openset.append(maze.startnode)
maze.startnode.visited=1

while True:
    #if search all point, end
    if openset==[]:
        print("We have searched all reachable nodes ")
        break
    
    # find min cost set in openset
    current=heap_pop(openset)
    current.visited
    
    closedset.append(current)
    
    if maze.verifyend(current):
        print("We recive the final goal")
        break
        
    for i in range(len(maze.action)):
        node=maze.maze[current.x+maze.action[i][0]][current.y+maze.action[i][1]]
        #node.cost=current.cost+maze.action[i][2]

        if node.nodetype=='wall':
            continue
            
        if node.visited:
            if openset.count(node)>0:
                index=openset.index(node)
                #print(index)
                if node.cost>current.cost+maze.action[i][2]:
                    node.cost=current.cost+maze.action[i][2]
                    node.parent_x=current.x
                    node.parent_y=current.y
                    openset=shift_up(openset, index)
                
                
        else:
            node.cost=current.cost+maze.action[i][2]
            node.parent_x=current.x
            node.parent_y=current.y
            openset=heap_insert(openset, node)
            node.visited=1