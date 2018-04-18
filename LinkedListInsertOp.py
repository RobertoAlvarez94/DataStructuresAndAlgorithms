class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data=data
    
    def get_next(self):
        return self.__next
    
    def set_next(self,next_node):
        self.__next=next_node
    
class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self,data):
      new_node=Node(data)
      new_node.set_next(self.__head)
      self.__head=new_node
      
    def display(self):
        curr = self.__head
        last = False
        while curr and last is False:
          if curr is None:
            last = True
          else:
            print(curr.get_data())
            curr=curr.get_next()
    
    def find_node(self,data):
        curr = self.__head
        found = False
        while curr and found is False:
          if curr.get_data()==data:
            found=True
          else:
            curr=curr.get_next()
          if curr is None:
            raise ValueError("data problem")
        return curr
  
    def insert(self, data, data_before):
      new_node=Node(data)
      if data_before is None:
        new_node.set_next(self.__head)
        self.__head=new_node
      elif data_before is not None:
        node_before=self.find_node(data_before)
        new_node.set_next(node_before)
        node_before.set_next(new_node)
        if new_node.get_next() is None:
          new_node.set_next(self.__tail)
          self.__tail=new_node
      else:
        print("please select something from list")
          

list1=LinkedList()
list1.add("Milk")
list1.add("Eggs")
list1.add("Sugar")
list1.add("Creackers")

list2=LinkedList()
list2.add("Sugar")
list2.add("Huevos")
list2.add("Pan")
node=list1.find_node("Sugar")
if(node!=None):
    print("Node found")
else:
    print("Node not found") 
    
list2.insert("Ostias", "Huevos")
node=list2.find_node("Ostias")
if(node!=None):
    print("Node found")
else:
    print("Node not found") 
