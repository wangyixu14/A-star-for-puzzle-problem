    # Finds the "_" in the puzzle and returns the x and y
def find(puz,x):
    for i in range(0,len(puz)):
        for j in range(0,len(puz)):
            if puz[i][j] == x:
                return i,j
class Node:
    
    # Initialize node
    def __init__(self,data,level,fval):
        self.data = data
        self.level = level
        self.fval = fval

    # Gets all possible moves for the blank
    def get_childern(self):
        x,y = find(self.data,'_')
        val_list = [[x-1,y], [x+1,y], [x,y-1], [x,y+1]]
        children = []
        for i in val_list:
            child = self.child(self.data,x,y,i[0],i[1])
            if child is not None:
                child_node = Node(child,self.level+1,0)
                children.append(child_node)
        return children
    
    # Returns the puzzle after each child is made
    def child(self,puz,x1,y1,x2,y2):
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

    # Makes and returns a copy of the puzzle
    def copy(self,root):
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp  



class Puzzle:
    def __init__(self,size):
        self.n = size
        # Where to visit
        self.open = []
        # Already been visited
        self.closed = []

    def accept(self):
        puz = []
        for i in range(0,self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    # Heuristic function for f(x) = h(x) + g(x) 
    def f(self,start,goal):
        return self.h(start.data,goal)+start.level

    # Difference between goal and current place
    def h(self,start,goal):
        temp = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                #if start[i][j] != goal[i][j] and start[i][j] != '_':
                    #temp += 1
                m, n = find(start, goal[i][j])
                temp += abs(m - i) + abs(n - j)
        #print(temp)

        return temp

    
    def process(self):
        # Initial state of the puzzle
        start = [[4,1,3],[2,6,8], ["_", 7 ,5]]
        goal = [[1,2,3],[4,5,6],[7,8,"_"]]

        # Start node
        start = Node(start,0,0)
        start.fval = self.f(start,goal)
        self.open.append(start)
        
        # Keep trying to find the goal state
        while True:
            cur = self.open[0]
            # print("")
            # print("  | ")
            # print("  | ")
            # print(" \\\'/ \n")
            for i in cur.data:
                for j in i:
                    print(j,end=" ")
                print("")
            if(self.h(cur.data,goal) == 0):
                break
            for i in cur.get_childern():
                i.fval = self.f(i,goal)
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]
            self.open.sort(key = lambda x:x.fval,reverse=False)
            print(self.open[0].level)


puz = Puzzle(3)
puz.process()