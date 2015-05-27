# Implements a binary search tree

class Node(object):
  """Node of a binary search tree"""
  def __init__(self, val):
    super(Node, self).__init__()
    self.val = val
    self.lchild = None
    self.rchild = None

  def insert(self, val):
    if self.val == val:
      return False
    elif self.val > val:
      if self.lchild:
        return self.lchild.insert(val)
      else:
        lchild = Node(val)
        self.lchild = lchild
    else:
      if self.rchild:
        return self.rchild.insert(val)
      else:
        rchild = Node(val)
        self.rchild = rchild

  def find(self, val):
    if self.val == val:
      return True
    elif self.val > val:
      if self.lchild:
        return self.lchild.find(val)
      else:
        return False
    else:
      if self.rchild:
        return self.rchild.find(data)
      else:
        return False

  def preorder(self):
    if self:
      print 'Node-> ' + str(self.val)
      if self.lchild:
        self.lchild.preorder()
      if self.rchild:
        self.rchild.preorder()

  def inorder(self):
    if self:
      if self.lchild:
        self.lchild.inorder()
      print 'Node-> ' + str(self.val)
      if self.rchild:
        self.rchild.inorder()

  def postorder(self):
    if self:
      if self.lchild:
        self.lchild.postorder()
      if self.rchild:
        self.rchild.postorder()
      print 'Node-> ' + str(self.val)  



class BinarySearchTree(object):
  """Implements binary search tree, uses Node class for one node of a tree"""
  def __init__(self):
    self.root = None

  def insert(self, val):
    if self.root:
      return self.root.insert(val)
    else:
      self.root = Node(val)
      return True

  def find(self, val):
    if self.root:
      return self.root.find(val)
    else:
      return False

  def preorder(self):
    print "Preorder"
    self.root.preorder()

  def inorder(self):
    print "Inorder"
    self.root.inorder()

  def postorder(self):
    print "Postorder"
    self.root.postorder()


def main():
  bst = BinarySearchTree()
  bst.insert(5)
  bst.insert(2)
  bst.insert(15)
  bst.preorder()
  bst.inorder()
  bst.postorder()

if __name__ == '__main__':
  main()