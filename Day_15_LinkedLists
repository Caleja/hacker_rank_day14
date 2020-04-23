class Node:
  def __init__(self,data):
    self.data = data
    self.next = None 

class Solution: 
  def display(self,head):
    current = head
    while current:
      print(current.data,end=' ')
      current = current.next

  def insert(self,head,data):
    new_node=Node(data)
    if head is None: 
      self.head=new_node
      return self.head      
    last_node=self.head 
    while last_node.next: #as long as next node exits->
      last_node=last_node.next
    last_node.next=new_node
    return self.head

mylist=Solution()
T=[3,7,9,5,0,1]
head=None
for data in T:
  print("data:",data)
  head=mylist.insert(head,data)    
mylist.display(head) 
