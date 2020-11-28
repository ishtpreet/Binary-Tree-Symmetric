class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
class BinaryTree(object):
  def __init__(self, root):
    self.root = Node(root)

#Initialising BinaryTree with Root Node 10
tree = BinaryTree(10)
#Setting Up BinaryTree
'''
              10
            /    \
           5      5
         /  \    /  \
        3    4  4    3
'''
tree.root.left = Node(5)
tree.root.right = Node(5)
tree.root.left.left = Node(3)
tree.root.left.right = Node(4)
tree.root.right.left = Node(4)
tree.root.right.right = Node(3)

#Checking if Binary tree is Symmetric or Not
def mirror(root1, root2):
  if root1 is None and root2 is None:
    return True
  if root1 is not None and root2 is not None:
    if root1.value == root2.value:
      return ((mirror(root1.left, root2.right)) and (mirror(root1.right, root2.left)))
  return False
def symmetric(root):
  return mirror(root, root)

#Calling the Symmetric Function with the above BinaryTree
x = symmetric(tree.root)
if x:
  print("Tree is symmetric")
else:
  print("Tree is not symmetric")