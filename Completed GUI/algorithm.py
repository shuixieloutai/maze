from maze_genernate import maze
from data_structure import heap, FIFO, FILO, priority_queue, Manhattan_Distance, Euclidean_distance

#file_path='maze-2.txt'

#maze=maze(file_path)

### we can use 'maze=maze(file_path)' to read a maze file and genernate a maze or use 'maze=Maze()' to creat a Maze class
### There are four types of algorithm in this file: Dijkstra, DFS, BFS, IDS, A*
### To use one type of algorithm, like Astar just use 'Astar(maze)'to find the path
### 'maze.reset()' can reset the maze to the initial state(not been visited)


#### BFS
def BFS(maze, output=False):
    #node  has been checked
    openset=FIFO()
    #node has not been checked
    closedset = []

    # add start node/
    openset.push(maze.startnode)
    maze.startnode.visited=1

    while True:
        #if search all point, end
        if openset.queue==[]:
            if output:
                print("We have searched all reachable nodes ")
            break

        # find min cost set in openset
        current=openset.pop()

        #current.visited=1
        closedset.append(current)

        if maze.verifyend(current):
            if output:
                print("We recive the final goal")
            break

        for i in range(len(maze.action)):
            node=maze.maze[current.x+maze.action[i][0]][current.y+maze.action[i][1]]
            #node.cost=current.cost+maze.action[i][2]

            if node.nodetype=='wall':
                continue

            if not node.visited:
                node.cost=current.cost+maze.action[i][2]
                node.parent_x=current.x
                node.parent_y=current.y
                openset.push(node)
                node.visited=1
    return closedset

#### Dijkstra/UCS
def Dijkstra(maze, output=False):
    #node  has been checked
    openset=heap()
    #node has not been checked
    closedset = []

    # add start node/
    openset.insert(maze.startnode)
    maze.startnode.visited=1

    while True:
        #if search all point, end
        if openset.heap==[]:
            if output:
                print("We have searched all reachable nodes ")
            break

        # find min cost set in openset
        current=openset.pop()

        current.visited=2
        closedset.append(current)

        if maze.verifyend(current):
            if output:
                print("We recive the final goal")
            break

        for i in range(len(maze.action)):
            node=maze.maze[current.x+maze.action[i][0]][current.y+maze.action[i][1]]
            #node.cost=current.cost+maze.action[i][2]

            if node.nodetype=='wall':
                continue

            if not node.visited:
                if node.visited==1:
                    index=openset.heap.index(node)
                    #print(index)
                    if node.cost>current.cost+maze.action[i][2]:
                        node.cost=current.cost+maze.action[i][2]
                        node.parent_x=current.x
                        node.parent_y=current.y
                        openset.shift_up(index)  
                else:
                    node.cost=current.cost+maze.action[i][2]
                    node.parent_x=current.x
                    node.parent_y=current.y
                    openset.insert(node)
                    #node.visited=1
    return closedset

#### DFS
def DFS(maze, output=False):
    #node  has been checked
    openset=FILO()
    #node has not been checked
    closedset = []

    # add start node/
    openset.push(maze.startnode)
    maze.startnode.visited=1

    while True:
        #if search all point, end
        if openset.queue==[]:
            if output:
                print("We have searched all reachable nodes ")
            break

        # find min cost set in openset
        current=openset.pop()

        #current.visited=1
        closedset.append(current)

        if maze.verifyend(current):
            if output:
                print("We recive the final goal")
            break

        for i in range(len(maze.action)):
            node=maze.maze[current.x+maze.action[i][0]][current.y+maze.action[i][1]]
            #node.cost=current.cost+maze.action[i][2]

            if node.nodetype=='wall':
                continue

            if not node.visited:
                node.cost=current.cost+maze.action[i][2]
                node.parent_x=current.x
                node.parent_y=current.y
                openset.push(node)
                node.visited=1
    return closedset


####  IDS
def IDS(maze, output=False):
    #node  has been checked
    openset=FILO()
    #node has not been checked
    closedset = []

    # add start node/
    #openset.push(maze.startnode)
    #maze.startnode.visited=1

    deep=0
    while True:
        deep+=1
        #reset the graph
        maze.reset()
        closedset = []
        maze.startnode.visited=1
        openset.push(maze.startnode)
        while openset.queue!=[]:
            # find min cost set in openset
            current=openset.pop()

            #current.visited=1
            closedset.append(current)

            if maze.verifyend(current):
                if output:
                    print("We recive the final goal")
                break

            for i in range(len(maze.action)):
                node=maze.maze[current.x+maze.action[i][0]][current.y+maze.action[i][1]]
                #node.cost=current.cost+maze.action[i][2]

                if node.nodetype=='wall':
                    continue

                if current.cost+maze.action[i][2]>deep:
                    break

                if not node.visited:
                    node.cost=current.cost+maze.action[i][2]
                    node.parent_x=current.x
                    node.parent_y=current.y
                    openset.push(node)
                    node.visited=1
        if maze.endpoint>=0:
            break
    return closedset

#### A*
def Astar(maze, output=False):
    #node  has been checked
    openset=priority_queue()
    #node has not been checked
    closedset = []

    # add start node/
    openset.push(maze.startnode)
    maze.startnode.visited=1
    maze.startnode.value=maze.startnode.cost+Euclidean_distance(maze.startnode, maze.endnode[0])
    
    while True:
        #if search all point, end
        if openset.queue==[]:
            if output:
                print("We have searched all reachable nodes ")
            break

        # find min cost set in openset
        current=openset.pop_min()

        #current.visited=1
        closedset.append(current)

        if maze.verifyend(current):
            if output:
                print("We recive the final goal")
            break

        for i in range(len(maze.action)):
            node=maze.maze[current.x+maze.action[i][0]][current.y+maze.action[i][1]]
            #node.cost=current.cost+maze.action[i][2]

            if node.nodetype=='wall':
                continue

            if not node.visited:
                node.cost=current.cost+maze.action[i][2]
                node.parent_x=current.x
                node.parent_y=current.y
                node.value=node.cost+Euclidean_distance(node, maze.endnode[0])
                openset.push(node)
                node.visited=1
            elif openset.queue.count(node)>0:
                #index=openset.queue.index(node)
                if node.value>current.cost+maze.action[i][2]+Euclidean_distance(node, maze.endnode[0]):
                    node.cost=current.cost+maze.action[i][2]
                    node.parent_x=current.x
                    node.parent_y=current.y
                    node.value=node.cost+Euclidean_distance(node, maze.endnode[0])
    return closedset


            

#closedset=IDS(maze)
#maze.reset()
