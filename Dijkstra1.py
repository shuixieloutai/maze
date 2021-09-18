import sys
import matplotlib.pyplot as plt

#node class
class Node:
    def __init__(self, x, y, cost, parent):
        self.x = x # x
        self.y = y # y
        self.cost = cost # shortest cost from the start 
        self.parent = parent # index of the previous node

    def __str__(self):
        return str(self.x) + "," + str(self.y) + "," + str(self.cost) + "," + str(self.parent)

def MazeReader(file_path):
    with open(file_path) as f:
        lines=f.readlines()
        #remove the '\n'，replace with ''
        for i in range(len(lines)):
            lines[i]=lines[i].replace('\n','')       
    return lines

def charttoint(lines):
    a=len(lines)
    b=len(lines[a-1])
    maze=5*np.ones([a,b])
    index_start=np.empty([0,2])
    index_wall=np.empty([0,2])
    index_open=np.empty([0,2])
    index_end=np.empty([0,2])
    for i in range(a):
        for j in range(b):
            c=lines[i][j]
            if c=='#':
                maze[i,j]=1
                index_wall=np.vstack((index_wall,[i,j]))
            elif c=='.':
                maze[i,j]=0
                index_open=np.vstack((index_open,[i,j]))
            elif c=='o':
                maze[i,j]=2
                index_start=np.vstack((index_start,[i,j]))
            elif c=='*':
                maze[i,j]=3
                index_end=np.vstack((index_end,[i,j]))
            else:
                print('IllegalArgumentException')
                sys.exit()
    return maze, index_wall, index_open, index_start, index_end


def draw_raw(lines):
    print('maze:')
    for line in lines:
        print(line)
        
def draw_map(index_wall, index_start, index_end):
    import matplotlib.pyplot as plt

    plt.plot(index_wall[:,1],max(index_wall[:,0])-index_wall[:,0],"ks")
    plt.plot(index_start[:,1],max(index_wall[:,0])-index_start[:,0], "xr")
    plt.plot(index_end[:,1],max(index_wall[:,0])-index_end[:,0],"xb")
    #plt.plot(index_wall[:,0],index_wall[:,1],"ks")
    #gridobj.set(xlim=(0.5,7.5),ylim=(0,50)) 
    

def draw_search(closedset, index_wall):
    path=list(closedset)
    for i in range(len(path)):
        plt.pause(0.01)
        draw_map(index_wall, index_start, index_end)
        for j in range(i+1):
            index=path[j]
            plt.plot(closedset[index].y, max(index_wall[:,0])-closedset[index].x, "ys")

def draw_path(endnode, endpoint, index_wall):
    path_x, path_y=[endnode[endpoint].x], [endnode[endpoint].y]
    parent = endnode[endpoint].parent
    while parent!=-1:
        node=closedset[parent]
        path_x.append(node.x)
        path_y.append(node.y)
        parent=node.parent
    plt.plot(path_y, max(index_wall[:,0])-path_x,"-r")
    


#return judgement and index
def verifyend(current, endnode):
    for i in range(len(endnode)):
        node=endnode[i]
        if current.x == node.x and current.y == node.y:
            return 1, i
    return 0, 0

#judge if the node is wall
def verifywall(node,maze):
    if maze[int(node.x),int(node.y)]==1:
        return 1
    else:
        return 0

# we can move to four direction
action = [[ 1,  0, 1],
          [ 0,  1, 1],
          [-1,  0, 1],
          [ 0, -1, 1]]

#mange the index of node
def index_node(node, width):
    index_node=node.x*width+node.y
    return index_node

import numpy as np
import sys

file_path='maze-2.txt'

#read the data from .txt file
lines=MazeReader(file_path)

#draw the maze consisted of maze
draw_raw(lines)

#genernate a maze matrix
maze, index_wall, index_open, index_start, index_end=charttoint(lines)

print("\nTransfer maze to matrix\n")
print(maze)

width=maze.shape[1]

#build  start node and endnode
startnode=Node(index_start[0,0],index_start[0,1],0,-1)
endnode=dict()
for i in range(len(index_end)):
    endnode[i]=Node(index_end[0,0],index_end[0,1],0,-1)
    
#node  has been checked
openset=dict()
#node has not been checked
closedset = dict()

# add start node
openset[index_node(startnode, width)] = startnode

#draw_map()
endpoint=-1
while True:
    #if search all point, end
    if openset=={}:
        print("We have searched all reachable nodes ")
        break
    
    # find min cost set in openset
    current_id = min(openset, key=lambda n: openset[n].cost)
    #print(current_id)
    current= openset[current_id]
    #print("current:",current)
    
    
    #move the current node into closedset
    del openset[current_id]
    closedset[current_id] = current
    
    #judge if the end node
    ver, ind_end=verifyend(current, endnode)
    if ver:
        print("\nWe recive the final goal")
        endnode[ind_end].parent = current.parent
        endnode[ind_end].cost = current.cost
        endpoint=ind_end
        break
    
    #Maintain boundary vector
    for i in range(len(action)):
        node=Node(current.x+action[i][0], current.y+action[i][1], current.cost + action[i][2], current_id)
        node_id = index_node(node, width)
        #if the node is wall, next
        if verifywall(node,maze):
            continue
            
        if node_id in closedset:
            continue

        if node_id in openset:
            
            if openset[node_id].cost > node.cost:
                openset[node_id].cost = node.cost
                openset[node_id].parent = current_id
        # add in the openset
        else:
            openset[node_id] = node
            
draw_map(index_wall, index_start, index_end)

draw_search(closedset, index_wall)

draw_path(endnode, endpoint, index_wall)
