# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 17:25:02 2021

@author: ASUS
"""


from maze_genernate import maze
from maze_initializer import Maze_initializer
#from data_structure import heap, FIFO, FILO, priority_queue, Manhattan_Distance, Euclidean_distance
from algorithm import Dijkstra, DFS, IDS, Astar, BFS

file_path='maze-2.txt'

maze=maze(file_path)
start=time.time()
closedset=DFS(maze)
print(len(closedset))
length_shortest=0
x=-1
y=-1
x,y=maze.endnode[maze.endpoint].parent_x,maze.endnode[maze.endpoint].parent_y
while 1:
    if maze.maze[x][y].parent_x==-1:
        break
    x,y=maze.maze[x][y].parent_x,maze.maze[x][y].parent_y
    #print(x,y)
    length_shortest+=1
print('shortest path:',length_shortest)
maze.reset()

closedset=BFS(maze)
print(len(closedset))
length_shortest=0
x=-1
y=-1
x,y=maze.endnode[maze.endpoint].parent_x,maze.endnode[maze.endpoint].parent_y
while 1:
    if maze.maze[x][y].parent_x==-1:
        break
    x,y=maze.maze[x][y].parent_x,maze.maze[x][y].parent_y
    #print(x,y)
    length_shortest+=1
print('shortest path:',length_shortest)
maze.reset()

closedset=Dijkstra(maze)
print(len(closedset))
length_shortest=0
x=-1
y=-1
x,y=maze.endnode[maze.endpoint].parent_x,maze.endnode[maze.endpoint].parent_y
while 1:
    if maze.maze[x][y].parent_x==-1:
        break
    x,y=maze.maze[x][y].parent_x,maze.maze[x][y].parent_y
    #print(x,y)
    length_shortest+=1
print('shortest path:',length_shortest)
maze.reset()

closedset=IDS(maze)
print(len(closedset))
length_shortest=0
x=-1
y=-1
x,y=maze.endnode[maze.endpoint].parent_x,maze.endnode[maze.endpoint].parent_y
while 1:
    if maze.maze[x][y].parent_x==-1:
        break
    x,y=maze.maze[x][y].parent_x,maze.maze[x][y].parent_y
    #print(x,y)
    length_shortest+=1
print('shortest path:',length_shortest)
maze.reset()

closedset=Astar(maze)
print(len(closedset))
length_shortest=0
x=-1
y=-1
x,y=maze.endnode[maze.endpoint].parent_x,maze.endnode[maze.endpoint].parent_y
while 1:
    if maze.maze[x][y].parent_x==-1:
        break
    x,y=maze.maze[x][y].parent_x,maze.maze[x][y].parent_y
    #print(x,y)
    length_shortest+=1
print('shortest path:',length_shortest)
maze.reset()
end=time.time()
print(end-start)