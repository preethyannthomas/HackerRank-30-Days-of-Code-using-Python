class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        depth = 0
        q = []
        q.append(root)
        q.append(None)
        while(len(q) > 0):
            temp = q[0]
            q = q[1:]
            if(temp == None):
                depth += 1

            if(temp != None):
                if(temp.left):
                    q.append(temp.left)
     
                if(temp.right):
                    q.append(temp.right)
            elif(len(q) > 0):
                q.append(None)
        return depth-1

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       
