# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 17:25:02 2021

@author: ASUS
"""


from maze_genernate import maze
#from data_structure import heap, FIFO, FILO, priority_queue, Manhattan_Distance, Euclidean_distance
from algorithm import Dijkstra, DFS, IDS, Astar, BFS

file_path='maze-2.txt'

maze=maze(file_path)

closedset=DFS(maze)
print(len(closedset))
maze.reset()

closedset=BFS(maze)
print(len(closedset))
maze.reset()

closedset=Dijkstra(maze)
print(len(closedset))
maze.reset()

closedset=IDS(maze)
print(len(closedset))
maze.reset()

closedset=Astar(maze)
print(len(closedset))
maze.reset()