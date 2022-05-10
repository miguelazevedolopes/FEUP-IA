class Node:
    def __init__(self,parent=None):
        self.parent=parent


class Bottles(Node):
    def __init__(self,parent,capacity1 ,maxCapacity1,capacity2,maxCapacity2,cost):
        self.capacity1=capacity1
        self.maxCapacity1=maxCapacity1
        self.capacity2=capacity2
        self.maxCapacity2=maxCapacity2
        self.cost=cost
        super().__init__(parent)
    def __eq__(self, o) -> bool:
        if(o==None):
            return False
        if( self.capacity1==o.capacity1 and self.capacity2==o.capacity2):
            return True
        
        return False
    
def getAdjacentNodes(node):
    amount1=node.maxCapacity1-node.capacity1
    if(amount1>node.capacity2):
        amount1=node.capacity2
    amount2=node.maxCapacity2-node.capacity2
    if(amount2>node.capacity1):
        amount2=node.capacity1    
    return [
        Bottles(node,node.maxCapacity1,node.maxCapacity1,node.capacity2,node.maxCapacity2,node.cost+1),
        Bottles(node,node.capacity1,node.maxCapacity1,node.maxCapacity2,node.maxCapacity2,node.cost+1),
        Bottles(node,0,node.maxCapacity1,node.capacity2,node.maxCapacity2,node.cost+1),
        Bottles(node,node.capacity1,node.maxCapacity1,0,node.maxCapacity2,node.cost+1),
        Bottles(node,node.capacity1+amount1,node.maxCapacity1,node.capacity2-amount1,node.maxCapacity2,node.cost+1),
        Bottles(node,node.capacity1-amount2,node.maxCapacity1,node.capacity2+amount2,node.maxCapacity2,node.cost+1)
        ]
    


def isGoal(node):
    if(node.capacity1==2):
        return True
    return False

def bfs(node):
    q=[]
    visited=[node]
    q.append(node)
    while(len(q)!=0):
        n=q.pop(0)
        if(isGoal(n)==True):
            return n
        adjacentNodes=getAdjacentNodes(n)
        for e in adjacentNodes:
            if(e not in visited):
                visited.append(e)
                q.append(e)

def dfs(node):
    s=[node]
    visited=[]
    while(len(s)!=0):
        n=s.pop()
        if(isGoal(n)==True):
            return n
        if(n not in visited):
            visited.append(n)
            adjacentNodes=getAdjacentNodes(n)
            for e in adjacentNodes:
                s.append(e)

def ids(node):
    s=[node]
    visited=[]
    maxDepth=0
    while(True):
        maxDepth+=1
        s=[node]
        visited=[]
        while(len(s)!=0):
            n=s.pop()
            if(isGoal(n)==True):
                return n
            if(n not in visited):
                visited.append(n)
                if(n.cost==maxDepth):
                    continue
                adjacentNodes=getAdjacentNodes(n)
                for e in adjacentNodes:
                    s.append(e)

def getPath(node):
    path=[node]
    print(str(node.capacity1))
    while(node.parent!=None):
        node=node.parent
        path.append(node)
    path.reverse()
    return path

def main():
    print("\nStarting\n--------\n")
    start=Bottles(None,0,4,0,3,0)
    print("Starting BFS\n------------\n")
    end=ids(start)
    print("Getting Path\n------------\n")
    path=getPath(end)
    for p in path:
        print("Bottle 1 Capacity: "+str(p.capacity1))
        print("Bottle 2 Capacity: "+str(p.capacity2)+"\n")
    print("Cost:" +str(end.cost))

main()