from maze_genernate import Maze

from random import randint, choice
class Maze_initializer(Maze):
    def maze_create(self, width, height, end_num=1):
        self.width=width
        self.height=height
        if self.width % 2 != 1 or self.height % 2 != 1:
            print("The width and height should be odd")
            return
        self.maze=self.maze_initialize(self.width, self.height)
        for i in range(self.height):
            for j in range(self.width):
                self.maze[i][j].nodetype='wall'
        self.prime()
        self.set_end(end_num)
        

                                 
    def prime(self):
        self.set_start()
        checklist=[self.startnode]
        while len(checklist):
            #self.print_maze()
            entry = choice(checklist)
            if not self.check_neighbors(entry, checklist):
                checklist.remove(entry)
    
    def check_neighbors(self, entry, checklist):
        directions=[]
        
        #check four directions
        if entry.x>2:
            if self.maze[entry.x-2][entry.y].nodetype=='wall':
                directions.append([-1,0])
        if entry.y>2:
            if self.maze[entry.x][entry.y-2].nodetype=='wall':
                directions.append([0,-1])
        if entry.x+2<self.height-1:
            if self.maze[entry.x+2][entry.y].nodetype=='wall':
                directions.append([1,0])
        if entry.y+2<self.width-1:
            if self.maze[entry.x][entry.y+2].nodetype=='wall':
                directions.append([0,1])
        
        if len(directions):
            direction = choice(directions)
            self.maze[entry.x+direction[0]][entry.y+direction[1]].nodetype='open'
            self.maze[entry.x+2*direction[0]][entry.y+2*direction[1]].nodetype='open'
            checklist.append(self.maze[entry.x+2*direction[0]][entry.y+2*direction[1]])
            #print(entry.x+2*direction[0],entry.y+2*direction[1])
            return True
            
        return False
                
    
    
    def set_start(self, end_num=1):
        start_x,start_y=(randint(1, (self.height - 1)/2), randint(1, (self.width - 1)/2))
        self.maze[2*start_x-1][2*start_y-1].nodetype='start'
        self.startnode=self.maze[2*start_x-1][2*start_y-1]
        self.startnode.cost=0
        
    def set_end(self, num_end=1):
        start_x=(self.startnode.x+1)/2
        start_y=(self.startnode.y+1)/2
        for i in range(num_end):
            end_x,end_y=(randint(1, (self.height - 1)/2), randint(1, (self.width - 1)/2))
            while(abs(2*(end_x-start_x))<(self.height-3)/2 or abs(2*(end_y-start_y))<(self.width-3)/2):
                end_x, end_y=(randint(1, (self.height - 1)/2), randint(1, (self.width - 1)/2))
            self.maze[2*end_x-1][2*end_y-1].nodetype='end'
            self.endnode.append(self.maze[2*end_x-1][2*end_y-1])
            
    def print_maze(self):
        import numpy as np
        m=np.zeros([self.height,self.width])
        for i in range(self.height):
            for j in range(self.width):
                if self.maze[i][j].nodetype=='wall':
                    m[i][j]=1
                elif self.maze[i][j].nodetype=='open':
                    m[i][j]=0
                elif self.maze[i][j].nodetype=='start':
                    m[i][j]=2
                else:
                    m[i][j]=3     
        print(m)
        
    def maze2lines(self):
        self.lines=[]
        for i in range(self.height):
            line=''
            for j in range(self.width): 
                if self.maze[i][j].nodetype=='wall':
                    line=line+'#'
                elif self.maze[i][j].nodetype=='open':
                    line=line+'.'
                elif self.maze[i][j].nodetype=='start':
                    line=line+'o'
                else:
                    line=line+'*'  
            self.lines.append(line)
            
    def save(self):
        self.maze2lines()
        file_name='maze_'+str(self.height)+'_'+str(self.width)+'.txt'
        with open(file_name,'w') as f:
            for line in self.lines:
                f.write(line+'\n')
                
