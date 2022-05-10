from pydoc import visiblename
from time import sleep
from matplotlib.pyplot import getp
from numpy import vstack


class Node:
    def __init__(self,parent=None):
        self.parent=parent

class Bank:
    def __init__(self,missionaries,cannibals):
        self.missionaries=missionaries
        self.cannibals=cannibals
    def __eq__(self, o) -> bool:
        return (o.missionaries==self.missionaries and o.cannibals==self.cannibals)
    def __str__(self) -> str:
        return "Missionaries - " + str(self.missionaries) + "\nCannibals - " + str(self.cannibals)

class Boat:
    def __init__(self,missionaries,cannibals,left):
        self.missionaries=missionaries
        self.cannibals=cannibals
        self.left=left
    def __eq__(self, o) -> bool:
        return (o.missionaries==self.missionaries and o.cannibals==self.cannibals and o.left==self.left)
    def __str__(self) -> str:
        return "Missionaries - " + str(self.missionaries) + "\nCannibals - " + str(self.cannibals)

class StateNode(Node):
    def __init__(self,parent=None,boat:Boat=None,leftBank:Bank=None,rightBank:Bank=None,cost=0):
        self.boat=boat
        self.leftBank=leftBank
        self.rightBank=rightBank
        self.cost=cost
        super().__init__(parent)
    def __eq__(self,o):
        if(o==None):
            return False
        return (o.leftBank==self.leftBank and o.rightBank==self.rightBank and o.boat==self.boat)
    def __str__(self):
        return "-------------\nLeft Bank: \n" + self.leftBank.__str__() + "\n\nRight Bank: \n" + self.rightBank.__str__() + "\n\nBoat Bank: \n" + self.boat.__str__() + "\n-------------\n\n" 

def isGoal(node:StateNode):
    if(node.rightBank.missionaries==3 and node.rightBank.cannibals==3):
        return True
    return False

def validMove(node:StateNode):
    return ((node.boat.cannibals+node.boat.missionaries)<=2
    and (node.boat.cannibals>=0) and (node.boat.missionaries>=0)
    and (node.boat.cannibals+node.boat.missionaries)>=0
    and (node.leftBank.cannibals>=0) and (node.leftBank.missionaries>=0)
    and (node.rightBank.cannibals>=0) and (node.rightBank.missionaries>=0)
    and (node.boat.cannibals+node.boat.missionaries)>=0
    and (node.leftBank.cannibals<=node.leftBank.missionaries)
    and (node.rightBank.cannibals<=node.rightBank.missionaries)
    and (node.leftBank.cannibals+node.leftBank.missionaries)>=0
    and (node.rightBank.cannibals+node.rightBank.missionaries)>=0)

def getAdjacentNodes(node:StateNode):
    adjacentNodes=[]
    option=StateNode(node,
        Boat(node.boat.missionaries+1,node.boat.cannibals,node.boat.left),
        Bank(node.leftBank.missionaries-1,node.leftBank.cannibals),
        Bank(node.rightBank.missionaries,node.rightBank.cannibals),node.cost)
    if(validMove(option) and node.boat.left==True):
        adjacentNodes.append(option) 
    option=StateNode(node,
        Boat(node.boat.missionaries+1,node.boat.cannibals,node.boat.left),
        Bank(node.leftBank.missionaries,node.leftBank.cannibals),
        Bank(node.rightBank.missionaries-1,node.rightBank.cannibals),node.cost)
    if(validMove(option) and node.boat.left==False):
        adjacentNodes.append(option)
    option=StateNode(node,
        Boat(node.boat.missionaries,node.boat.cannibals+1,node.boat.left),
        Bank(node.leftBank.missionaries,node.leftBank.cannibals-1),
        Bank(node.rightBank.missionaries,node.rightBank.cannibals),node.cost)
    if(validMove(option) and node.boat.left==True):
        adjacentNodes.append(option)
    option=StateNode(node,
        Boat(node.boat.missionaries,node.boat.cannibals+1,node.boat.left),
        Bank(node.leftBank.missionaries,node.leftBank.cannibals),
        Bank(node.rightBank.missionaries,node.rightBank.cannibals-1),node.cost)
    if(validMove(option)and node.boat.left==False):
        adjacentNodes.append(option)
    option=StateNode(node,
        Boat(node.boat.missionaries,node.boat.cannibals-1,node.boat.left),
        Bank(node.leftBank.missionaries,node.leftBank.cannibals+1),
        Bank(node.rightBank.missionaries,node.rightBank.cannibals),node.cost)
    if(validMove(option) and node.boat.left==True):
        adjacentNodes.append(option)
    option=StateNode(node,
        Boat(node.boat.missionaries,node.boat.cannibals-1,node.boat.left),
        Bank(node.leftBank.missionaries,node.leftBank.cannibals),
        Bank(node.rightBank.missionaries,node.rightBank.cannibals+1),node.cost)
    if(validMove(option) and node.boat.left==False):
        adjacentNodes.append(option)
    option=StateNode(node,
        Boat(node.boat.missionaries-1,node.boat.cannibals,node.boat.left),
        Bank(node.leftBank.missionaries,node.leftBank.cannibals),
        Bank(node.rightBank.missionaries+1,node.rightBank.cannibals),node.cost)
    if(validMove(option) and node.boat.left==False):
        adjacentNodes.append(option)
    option=StateNode(node,
        Boat(node.boat.missionaries-1,node.boat.cannibals,node.boat.left),
        Bank(node.leftBank.missionaries+1,node.leftBank.cannibals),
        Bank(node.rightBank.missionaries,node.rightBank.cannibals),node.cost)
    if(validMove(option) and node.boat.left==True):
        adjacentNodes.append(option)
    option=StateNode(node,
        Boat(node.boat.missionaries,node.boat.cannibals,not node.boat.left),
        Bank(node.leftBank.missionaries,node.leftBank.cannibals),
        Bank(node.rightBank.missionaries,node.rightBank.cannibals),node.cost+1)
    if(validMove(option) and ((node.boat.cannibals+node.boat.missionaries)>0)):
        adjacentNodes.append(option)
    return adjacentNodes

def bfs(node):
    visited=[node]
    q=[node]
    while(len(q)!=0):
        n=q.pop(0)
        if(isGoal(n)==True):
            return n
        adjacentNodes=getAdjacentNodes(n)
        for a in adjacentNodes:
            if(a not in visited):
                q.append(a)
                visited.append(a)
    return node

def dfs(node):
    visited=[]
    s=[node]
    while(len(s)!=0):
        n=s.pop()
        if(isGoal(n)==True):
            return n
        if(n not in visited):
            visited.append(n)
            for a in getAdjacentNodes(n):
                s.append(a)

def getPath(start,node:StateNode):
    path=[node]
    while(node.parent!=None):
        node=node.parent
        path.append(node)
    path.reverse()
    return path

def ids(node):
    maxDepth=1
    while(True):
        maxDepth+=1
        depth=1
        s=[node]
        visited=[]
        while(len(s)!=0):
            n=s.pop()
            if(isGoal(n)==True):
                return n
            if(n not in visited):
                visited.append(n)
                if(depth<maxDepth):
                    for a in getAdjacentNodes(n):
                        s.append(a)
                    depth+=1

def main():
    leftBank=Bank(3,3)
    rightBank=Bank(0,0)
    boat=Boat(0,0,True)
    start=StateNode(None,boat,leftBank,rightBank)
    end=ids(start)
    path=getPath(start,end)
    for p in path:
        print(p)
    print(end.cost)

main()