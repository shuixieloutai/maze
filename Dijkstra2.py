# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 22:34:35 2021

@author: ASUS
"""


import sys
import matplotlib.pyplot as plt
import numpy as np
import time

file_path='maze-2.txt'

#node class
class Node:
    def __init__(self, x, y, cost, parent_x, parent_y):
        self.x = x # x
        self.y = y # y
        self.cost = cost # shortest cost from the start 
        self.parent_x = parent_x # index of the previous node
        self.parent_y = parent_y

    def __str__(self):
        return "x:"+str(self.x) + ", " + "y:"+str(self.y) + ", " + "cost:"+str(self.cost) + ", " + "parent_x:"+str(self.parent_x) + ", " + "parent_y:"+str(self.parent_y)
    
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
    for i in range(len(closedset)):
        plt.pause(0.01)
        draw_map(index_wall, index_start, index_end)
        for j in range(i+1):
            plt.plot(closedset[j].y, max(index_wall[:,0])-closedset[j].x, "ys")

def draw_path(endnode, endpoint, index_wall):
    path_x, path_y=[endnode[endpoint].x], [endnode[endpoint].y]
    parent_x=endnode[endpoint].parent_x
    parent_y=endnode[endpoint].parent_y
    while parent_x!=-1:
        for i in range(len(closedset)):
            if closedset[i].x==parent_x and closedset[i].y==parent_y:
                parent_x=closedset[i].parent_x
                parent_y=closedset[i].parent_y
                path_x.append(closedset[i].x)
                path_y.append(closedset[i].y)
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
startnode=Node(index_start[0,0],index_start[0,1],0,-1,-1)
endnode=[]
for i in range(len(index_end)):
    endnode.append(Node(index_end[i,0],index_end[i,1],0,-1,-1))
    
#node  has been checked
openset=[]
#node has not been checked
closedset = []

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
            t=t = heap[k]
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

# add start node
openset.append(startnode)

start=time.time()

#draw_map()
endpoint=-1
while True:
    #if search all point, end
    if openset==[]:
        print("We have searched all reachable nodes ")
        break
    
    # find min cost set in openset
    current=heap_pop(openset)
    
    current_id=index_node(current, width)
    #print("current:",current)
    
    closedset.append(current)
    
    #judge if the end node
    ver, end=verifyend(current, endnode)
    if ver:
        print("We recive the final goal")
        endnode[end].parent_x = current.parent_x
        endnode[end].parent_y = current.parent_y
        endnode[end].cost = current.cost
        endpoint=end
        break
    
    #Maintain boundary vector
    for i in range(len(action)):
        node=Node(current.x+action[i][0], current.y+action[i][1], current.cost + action[i][2], current.x, current.y)
        node_id = index_node(node, width)
        #if the node is wall, next
        if verifywall(node,maze):
            continue
        
        flag=0
        for j in range(len(closedset)):
            if node.x==closedset[j].x and node.y==closedset[j].y:
                flag=1
                continue
        if flag==1:
            continue
        
        flag=0
        for j in range(len(openset)):
            if node.x==openset[j].x and node.y==openset[j].y:
                flag=1
                if openset[j].cost > node.cost:
                    openset[j].cost = node.cost
                    openset[j].parent = current_id
                    openset=shift_up(openset, k)
                # add in the openset
        if flag==0:
            openset=heap_insert(openset, node)
    
end=time.time()            

draw_search(closedset, index_wall)

draw_path(endnode, endpoint, index_wall)

print("time:", end-start)