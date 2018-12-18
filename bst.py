class Node:
    def __init__(self, data=None):
        self.data=data
        self.lChild=None
        self.rChild=None

    def setData(self, data):
        self.data=data

    def setlChild(self, lChild):
        self.lChild=lChild

    def setrChild(self, rChild):
        self.rChild=rChild

    def getData(self):
        return self.data

    def getlChild(self):
        return self.lChild

    def getrChild(self):
        return self.rChild


class BST:
    def __init__(self, root=None):
        self.root=root

    def insertNode(self, node):
        if self.root==None:
            self.root=node
        else:            
            nodeTemp, parentTemp=self.findNode(self.root, None, node)
            if nodeTemp == None:
                if node.getData()> parentTemp.getData():
                    parentTemp.setrChild(node)
                elif node.getData()< parentTemp.getData():
                    parentTemp.setlChild(node)
                    

    def inorder(self, root):
        if root==None:
            return
        else:
            self.inorder(root.getlChild())
            print str(root.getData())
            self.inorder(root.getrChild())



    def delNode(self,data):
        n, p =self.findNode(self.root, None, Node(data))
        if n==None:
            return
        else:
            #leaf
            if n.getrChild()==None and n.getlChild()==None:
                self.removeLeaf(n,p)
            #two Children
            elif n.getrChild()!=None and n.getlChild()!=None:
                nextNode, parent=self.findNextNode(n)
                nextData=nextNode.getData()
                self.removeLeaf(nextNode,parent)
                n.setData(nextData)      
            #one Child
            else:
                if n.getrChild()!=None:
                    if p==None:
                        self.root=n.getrChild()
                    elif p.getrChild()==n:
                        p.setrChild(n.getrChild())
                    elif p.getlChild()==n:
                        p.setlChild(n.getrChild())
                elif n.getlChild()!=None:
                    if p==None:
                        self.root=n.getlChild()
                    elif p.getrChild()==n:
                        p.setrChild(n.getlChild())
                    elif p.getlChild()==n:
                        p.setlChild(n.getlChild())
            return self.root
                
    def findNextNode(self, node):
        parent=node
        nChild=node.getrChild()
        while nChild.getlChild()!=None:
            parent=nChild
            nChild=nChild.getLeft()
        return nChild, parent

    def findNode(self, root, parent, node):
        if root==None:
            return None, parent
        if root.getData()==node.getData():
            return root, parent
        elif root.getData()<node.getData():
            return self.findNode(root.getrChild(), root, node)
        elif root.getData()>node.getData():
            return self.findNode(root.getlChild(), root, node)

    def removeLeaf(self, node, parent):
        if node==None:
            return
        elif parent==None:
            self.root=None
        elif node.getrChild()==None and node.getlChild()==None:
            if parent.getrChild()==node:
                parent.setrChild(None)
            elif parent.getlChild()==node:
                parent.setlChild(None)
        
            


#Tests
bst=BST()
root=Node(12)
bst.insertNode(root)
bst.insertNode(Node(5))
bst.insertNode(Node(11))
bst.insertNode(Node(17))
bst.insertNode(Node(7))

bst.inorder(root)
root=bst.delNode(11)

print "*********"

bst.inorder(root)
root=bst.delNode(12)
print "*********"

bst.inorder(root)

root=bst.delNode(17)
print "*********"

bst.inorder(root)

root=bst.delNode(7)
print "*********"

bst.inorder(root)

root=bst.delNode(5)
print "*********"

bst.inorder(root)


            
            
            
            
        

        
