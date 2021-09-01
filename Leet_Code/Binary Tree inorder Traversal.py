from random import randint
class Node:
    def __init__(self,value=None):
        self.value = value
        self.left_child = None #smaller
        self.right_child = None #bigger
class Binary_tree:
    def __init__(self):
        self.root = None
    def insert(self,value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value,self.root)
    def _insert(self,value,cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = Node(value)
            else:
                self._insert(value,cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
            else:
                self._insert(value,cur_node.right_child)
        else:
            print("This value has existed")
    def inorder_Traversal(self):
        res = []
        self.inorder(self.root,res)
        print(res)
    def inorder(self,root,res):
        if not root:return
        self.inorder(root.left_child,res)
        res.append(root.value)
        self.inorder(root.right_child,res)
    def preorder_Traversal(self):
        res = []
        self.preorder(self.root,res)
        print(res)
    def preorder(self,root,res):
        if not root:return
        res.append(root.value)
        self.preorder(root.left_child,res)
        self.preorder(root.right_child,res)
    def postorder_Traversal(self):
        res = []
        self.postorder(self.root,res)
        print(res)
    def postorder(self,root,res):
        if not root:return
        self.postorder(root.left_child,res)
        self.postorder(root.right_child,res)
        res.append(root.value)
def fill_tree(tree,num_elems = 10,max_int=50):
    for _ in range(num_elems):
        cur_elem = randint(0,max_int) #隨機0~50(不含50)的值
        tree.insert(cur_elem)
    return tree
tree = Binary_tree()
tree = fill_tree(tree)
tree.inorder_Traversal()