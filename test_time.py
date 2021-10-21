from maze_genernate import Maze
from maze_initializer import Maze_initializer
#from data_structure import heap, FIFO, FILO, priority_queue, Manhattan_Distance, Euclidean_distance
from algorithm import Dijkstra, DFS, IDS, Astar, BFS
import numpy as np

import time
start_whole=time.time()
maze=Maze_initializer()
size=[]
time_BFS=[]
time_Dijkstra=[]
time_Astar=[]
time_IDS=[]
for i in range(5,25,2):
    #print(i)
    maze=Maze_initializer()
    maze.maze_create(i-2,i,1)
    #maze.save()
    size.append((i-2)*i)
    
    #BFS
    #print("BFS:")
    start=timeit.time.clock()
    closedset=BFS(maze, output=False)
    #print('Search step:',len(closedset))
    length_shortest=0
    x=-1
    y=-1
    if maze.endpoint>=0:
        x,y=maze.endnode[maze.endpoint].parent_x,maze.endnode[maze.endpoint].parent_y
        while 1:
            if maze.maze[x][y].parent_x==-1:
                break
            x,y=maze.maze[x][y].parent_x,maze.maze[x][y].parent_y
            #print(x,y)
            length_shortest+=1
    #print('shortest path:',length_shortest)
    end=timeit.time.clock()
    #print("time:",end-start)
    time_BFS.append(end*1000-start*1000)
    maze.reset()
    
    
    #print("Dijkstra:")
    start=timeit.time.clock()
    closedset=Dijkstra(maze, output=False)
    #print('Search step:',len(closedset))
    length_shortest=0
    x=-1
    y=-1
    if maze.endpoint>=0:
        x,y=maze.endnode[maze.endpoint].parent_x,maze.endnode[maze.endpoint].parent_y
        while 1:
            if maze.maze[x][y].parent_x==-1:
                break
            x,y=maze.maze[x][y].parent_x,maze.maze[x][y].parent_y
            #print(x,y)
            length_shortest+=1
    #print('shortest path:',length_shortest)
    end=timeit.time.clock()
    #print("time:",end-start)
    time_Dijkstra.append(end*1000-start*1000)
    maze.reset()
    
    #print("IDS:")
    start=timeit.time.clock()
    closedset=IDS(maze, output=False)
    #print('Search step:',len(closedset))
    length_shortest=0
    x=-1
    y=-1
    if maze.endpoint>=0:
        x,y=maze.endnode[maze.endpoint].parent_x,maze.endnode[maze.endpoint].parent_y
        while 1:
            if maze.maze[x][y].parent_x==-1:
                break
            x,y=maze.maze[x][y].parent_x,maze.maze[x][y].parent_y
            #print(x,y)
            length_shortest+=1
    #print('shortest path:',length_shortest)
    end=timeit.time.clock()
    #print("time:",end-start)
    time_IDS.append(end*1000-start*1000)
    maze.reset()
    
    #print("Astar:")
    start=timeit.time.clock()
    closedset=Astar(maze, output=False)
    #print('Search step:',len(closedset))
    length_shortest=0
    x=-1
    y=-1
    if maze.endpoint>=0:
        x,y=maze.endnode[maze.endpoint].parent_x,maze.endnode[maze.endpoint].parent_y
        while 1:
            if maze.maze[x][y].parent_x==-1:
                break
            x,y=maze.maze[x][y].parent_x,maze.maze[x][y].parent_y
            #print(x,y)
            length_shortest+=1
    #print('shortest path:',length_shortest)
    end=timeit.time.clock()
    #print("time:",end-start)
    time_Astar.append(end*1000-start*1000)
    maze.reset()
    
    maze.maze_create(i-2,i,1)
    size.append(i*i)
    
    #BFS
    #print("BFS:")
    start=timeit.time.clock()
    closedset=BFS(maze, output=False)
    #print('Search step:',len(closedset))
    length_shortest=0
    x=-1
    y=-1
    if maze.endpoint>=0:
        x,y=maze.endnode[maze.endpoint].parent_x,maze.endnode[maze.endpoint].parent_y
        while 1:
            if maze.maze[x][y].parent_x==-1:
                break
            x,y=maze.maze[x][y].parent_x,maze.maze[x][y].parent_y
            #print(x,y)
            length_shortest+=1
    #print('shortest path:',length_shortest)
    end=timeit.time.clock()
    #print("time:",end-start)
    time_BFS.append(end*1000-start*1000)
    maze.reset()
    
    #print("Dijkstra:")
    start=timeit.time.clock()
    closedset=Dijkstra(maze, output=False)
    #print('Search step:',len(closedset))
    length_shortest=0
    x=-1
    y=-1
    if maze.endpoint>=0:
        x,y=maze.endnode[maze.endpoint].parent_x,maze.endnode[maze.endpoint].parent_y
        while 1:
            if maze.maze[x][y].parent_x==-1:
                break
            x,y=maze.maze[x][y].parent_x,maze.maze[x][y].parent_y
            #print(x,y)
            length_shortest+=1
    #print('shortest path:',length_shortest)
    end=timeit.time.clock()
    #print("time:",end-start)
    time_Dijkstra.append(end*1000-start*1000)
    maze.reset()
    
    #print("IDS:")
    start=timeit.time.clock()
    closedset=IDS(maze, output=False)
    #print('Search step:',len(closedset))
    length_shortest=0
    x=-1
    y=-1
    if maze.endpoint>=0:
        x,y=maze.endnode[maze.endpoint].parent_x,maze.endnode[maze.endpoint].parent_y
        while 1:
            if maze.maze[x][y].parent_x==-1:
                break
            x,y=maze.maze[x][y].parent_x,maze.maze[x][y].parent_y
            #print(x,y)
            length_shortest+=1
    #print('shortest path:',length_shortest)
    end=timeit.time.clock()
    #print("time:",end-start)
    time_IDS.append(end*1000-start*1000)
    maze.reset()
    
    #print("Astar:")
    start=timeit.time.clock()
    closedset=Astar(maze, output=False)
    #print('Search step:',len(closedset))
    length_shortest=0
    x=-1
    y=-1
    if maze.endpoint>=0:
        x,y=maze.endnode[maze.endpoint].parent_x,maze.endnode[maze.endpoint].parent_y
        while 1:
            if maze.maze[x][y].parent_x==-1:
                break
            x,y=maze.maze[x][y].parent_x,maze.maze[x][y].parent_y
            #print(x,y)
            length_shortest+=1
    #print('shortest path:',length_shortest)
    end=timeit.time.clock()
    #print("time:",end-start)
    time_Astar.append(end*1000-start*1000)
    maze.reset()
    #maze.save()
    
    del maze
end_whole=time.time()

print(end_whole-start_whole)

size=np.array(size)
np.savetxt( 'maze/size.txt', size, delimiter=',')
np.savetxt( 'maze/time_BFS.txt', time_BFS, delimiter=',')
np.savetxt( 'maze/time_Dijkstra.txt', time_Dijkstra, delimiter=',')
np.savetxt( 'maze/time_IDS.txt', time_IDS, delimiter=',')
np.savetxt( 'maze/time_Astar.txt', time_Astar, delimiter=',')

import matplotlib.pyplot as plt

fig1 = plt.subplots()
plt.xlabel('Size')
plt.ylabel('Time')
plt.plot(size, time_BFS, c='red')
plt.plot(size, time_Dijkstra, c='green')
plt.plot(size, time_IDS,c='yellow')
plt.plot(size, time_Astar, c='blue')
plt.legend(['BFS', 'Dijkstra', 'IDS', 'Astar'], loc='upper left')
plt.savefig('maze/1.png')

fig1 = plt.subplots()
plt.xlabel('Size')
plt.ylabel('Time')
plt.plot(size, time_BFS, c='red')
plt.plot(size, time_Dijkstra, c='green')
#plt.plot(size, time_IDS,c='yellow')
plt.plot(size, time_Astar, c='blue')
plt.legend(['BFS', 'Dijkstra', 'Astar'], loc='upper left')
plt.savefig('maze/2.png')