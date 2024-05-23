class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next
  
class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    node = Node(data, self.head)
    self.head = node

  def print(self):
    if self.head is None:
      print('Linked list is empty')
      return
    
    itr = self.head
    llstr = ''

    while itr:
      llstr += str(itr.data) + '-->'
      itr = itr.next
    print(llstr)
  
  def insert_at_end(self, data):
    itr = self.head
    while itr.next:
      itr = itr.next
    node = Node(data, None)
    itr.next = node
    pass


if __name__ == '__main__':
  ll = LinkedList()
  ll.insert_at_beginning(5)
  ll.insert_at_beginning(89)
  ll.insert_at_end(100)
  ll.print()
  print(ll.head.next.next.next)
  
  print(ll.head.value)
  