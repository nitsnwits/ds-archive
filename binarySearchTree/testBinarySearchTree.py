from BinarySearchTree import BinarySearchTree
import unittest

class TestBST(unittest.TestCase):
  def testTreeInit(self):
    bst = BinarySearchTree()
    self.assertTrue(bst.insert(5))

  def testTreeFind(self):
    bst = BinarySearchTree()
    self.assertFalse(bst.find(5))
    bst.insert(5)
    self.assertTrue(bst.find(5))

suite = unittest.TestLoader().loadTestsFromTestCase(TestBST)
unittest.TextTestRunner(verbosity=2).run(suite)