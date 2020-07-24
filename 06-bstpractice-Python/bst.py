class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # Your code goes here
       return self.driveinsert(self.root,new_val)
    
    def driveinsert(self,start,new_val):
        if (start):
            if (new_val<start.value):
                if (start.left):
                    self.driveinsert(start.left,new_val)
                else:
                    start.left=Node(new_val)
            elif(new_val>start.value):
                if(start.right):
                    self.driveinsert(start.right,new_val)
                else: 
                    start.right=Node(new_val)
        

    def printSelf(self):
        # Your code goes here
        res=""
        traversal=self.preorderprint(self.root,[])
        for i in traversal:
            res=res+str(value)+"_"
        res=res[::-1]
        return res


        pass
    def preorderprint(self,start,traversal):
        if start:
            traversal.append(start.value)
            if start.left:
                traversal=self.preorderprint(start.left,traversal)
            if start.left:
                traversal=self.preorderprint(start.right,traversal)
        return traversal


        
    def search(self, find_val):
        # Your code goes here
        return self.drivesearch(self.root,find_val)
        pass
    
    def drivesearch(self,start,find_val):
        if type(find_val)!=type(1):
            return False
        else:
            if start:
                if (find_val==start.value):
                    return True
                elif(find_val>start.value):
                    return self.drivesearch(start.right,find_val)
                elif(find_val<start.value):
                    return self.drivesearch(start.left,find_val)
        return False 
