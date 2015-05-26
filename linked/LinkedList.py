# Implements a Linked List

class Node(object):
  """Node of a Linked List"""
  def __init__(self, value):
    super(Node, self).__init__()
    self.value = value
    self.next = None

  def __str__(self):
    return str(self.value)


class LinkedList(object):
  """LinkedList Implementation"""
  def __init__(self):
    super(LinkedList, self).__init__()
    self.head = None
    self.tail = None

  def addNode(self, value):
    newNode = Node(value)
    if self.head is None:
      self.head = newNode
      self.tail = newNode
    else:
      self.tail.next = newNode
      self.tail = newNode

  def deleteNode(self, value):
    """removes first node when value is found"""
    prev = None
    found = False
    current = self.head
    if current.value == value:
      # head is to be deleted
      self.head = current.next
      return current.value
    prev = current
    current = current.next
    while current is not None and found is False:
      if current.value == value:
        found = True
      else:
        prev = current
        current = current.next
    if current is None:
      raise ValueError('Value not found in List')
    else:
      prev.next = current.next
      return current.value

  def searchNode(self, value):
    """return the first node that has the same value"""
    found = False
    current = self.head
    if current.value == value:
      return current.value
    current = current.next
    while current is not None and found is False:
      if current.value == value:
        found = True
      else:
        current = current.next
    if current is None:
      raise ValueError('Value not present in List')
    else:
      return current.value

  def size(self):
    if self.head is None:
      return 0
    current = self.head
    size = 0
    while current is not None:
      size = size + 1
      current = current.next
    return size

  def __str__(self):
    """ prints a linked list """
    if self.head is not None:
      current = self.head
      nodes = []
      while current is not None:
        nodes.append(str(current.value))
        current = current.next
      return 'LinkedList [ ' + '->'.join(nodes) + ' ]'
    return 'LinkedList []'

  def reverse(self):
    """ reverses a linked list """
    current = self.head
    self.tail = self.head
    prev = None
    while current is not None:
      nextNode = current.next
      current.next = prev
      prev = current
      current  = nextNode
    self.head = prev
    return str(self)
   
def main():
  ll = LinkedList()
  ll.addNode(5)
  print ll.searchNode(5)
  print ll

if __name__ == '__main__':
  main() 

