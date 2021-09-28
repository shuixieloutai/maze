#Yichen Gao 2021/9/28

import sys

class Node:
    def __init__(self, x, y, cost, parent_x, parent_y, nodetype="unknown"):
        self.x = x  # x
        self.y = y  # y
        self.cost = cost  # shortest cost from the start
        self.parent_x = parent_x  # index of the previous node
        self.parent_y = parent_y
        self.nodetype = nodetype
        self.visited=0

    def __str__(self):
        return "x:" + str(self.x) + ", y:" + str(self.y) + ", cost:" + str(
            self.cost) + ", parent:(" + str(self.parent_x) + "," + str(
                self.parent_y) + ")"

    def type(self):
        print("nodetype:" + str(self.nodetype))

    def update(self, cost, parent_x, parent_y):
        self.cost = cost
        self.parent_x = parent_x
        self.parent_y = parent_y
        
class Maze:

    def __init__(self):
        self.startnode=[]
        self.endnode=[]
        self.endpoint=-1
        #self.openset=[]
        #self.closedset=[]
        self.action = [[ 1,  0, 1],
          [ 0,  1, 1],
          [-1,  0, 1],
          [ 0, -1, 1]]
    
    def maze_initialize(self, width, height):
        maze = [[Node(y, x, float('inf'), -1, -1) for x in range(width)] for y in range(height)]
        return maze
        
    def MazeReader(self, file_path):
        with open(file_path) as f:
            self.lines=f.readlines()
            #remove the '\n'，replace with ''
            for i in range(len(self.lines)):
                self.lines[i]=self.lines[i].replace('\n','')    
        return self.lines
    
    def build_maze(self):
        height=len(self.lines)
        width=len(self.lines[height-1])
        self.maze=self.maze_initialize(width, height)
        for i in range(height):
            for j in range(width):
                c=self.lines[i][j]
                if c=='#':
                    self.maze[i][j].nodetype='wall'
                elif c=='.':
                    self.maze[i][j].nodetype='open'
                elif c=='o':
                    self.maze[i][j].nodetype='start'
                    self.startnode=self.maze[i][j]
                    self.startnode.cost=0
                elif c=='*':
                    self.maze[i][j].nodetype='end'
                    self.endnode.append(self.maze[i][j])
                else:
                    print('IllegalArgumentException')
                    sys.exit()
                    
    def verifyend(self, verify_node):
        for i in range(len(self.endnode)):
            if self.endnode[i]==verify_node:
                endpoint=i
                return True
        return False
    
    def verifywall(self, verify_node):
        if verify_node.nodetype=='wall':
            return True
        else:
            return False
        

def maze(file_path):
    maze=Maze()
    
    #read the data from .txt file
    maze.MazeReader(file_path)
    maze.lines
    maze.build_maze()
    return maze