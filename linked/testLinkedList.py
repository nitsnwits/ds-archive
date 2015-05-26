from LinkedList import LinkedList
import unittest
from random import randint

class TestLinkedList(unittest.TestCase):
  def testAddedNode(self):
    ll = LinkedList()
    ll.addNode(5)
    self.assertEqual(ll.searchNode(5), 5)

  def testMultipleAdditions(self):
    ll = LinkedList()
    ll.addNode(5)
    ll.addNode(10)
    ll.addNode(2)
    ll.addNode(1)
    self.assertEqual(ll.searchNode(2), 2)

  def testNonExistentElement(self):
    ll = LinkedList()
    ll.addNode(2)
    with self.assertRaises(ValueError):
      ll.searchNode(1)

  def testDeletedNode(self):
    ll = LinkedList()
    ll.addNode(2)
    ll.addNode(5)
    self.assertEqual(ll.deleteNode(5), 5)
    with self.assertRaises(ValueError):
      ll.searchNode(5)
    self.assertEqual(ll.searchNode(2), 2)

  def testPrintList(self):
    ll = LinkedList()
    ll.addNode(1)
    ll.addNode(2)
    self.assertEqual(str(ll), 'LinkedList [ 1->2 ]')

  def testSize(self):
    ll = LinkedList()
    ll.addNode(1)
    self.assertEqual(ll.size(), 1)

  def testLargeSize(self):
    ll = LinkedList()
    for i in range(0, 10000):
      ll.addNode(randint(1, 10))
    self.assertEqual(ll.size(), 10000)

  def testReverse(self):
    ll = LinkedList()
    ll.addNode(1)
    ll.addNode(2)
    ll.addNode(3)
    ll.addNode(4)
    self.assertEqual(str(ll), 'LinkedList [ 1->2->3->4 ]')
    self.assertEqual(ll.reverse(), 'LinkedList [ 4->3->2->1 ]')



suite = unittest.TestLoader().loadTestsFromTestCase(TestLinkedList)
unittest.TextTestRunner(verbosity=2).run(suite)