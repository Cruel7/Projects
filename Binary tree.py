class TreeNode:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.value=value

class BST:
    def __init__(self):
        self.root=None

    def add(self,current,value):
        if self.root==None:
            self.root=TreeNode(value)
        else:
            if value<current.value:
                if current.left==None:
                    current.left=TreeNode(value)
                else:
                    self.add(current.left,value)
            else:
                if current.right==None:
                    current.right=TreeNode(value)
                else:
                    self.add(current.right,value)

    def visit(self,TreeNode):
        print(TreeNode.value)

    def preorder(self,current):
        self.visit(current)
        self.preorder(current.left)
        self.preorder(current.right)


