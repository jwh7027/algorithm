##연결리스트
class Node :
    def __init__(self,value = 0,next = None):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 맨 뒤의 node가 new_node를 가리켜야 한다
        else:
            # O(1) 구현
            self.tail.next = new_node
            self.tail = self.tail.next 

            # O(n) 구현
            # current = self.head
            # while(current.next):
            #     current = current.next
            # current.next = new_node
            
    def get(self,idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value
    def insert_at(self,idx,value):
        new_node = Node(value)
        if(idx == 0):
            new_node.next = self.head
            self.head = new_node
        else:
            pre_node = self.head
            for _ in range(idx-1):
                pre_node = pre_node.next
            new_node.next = pre_node.next
            pre_node = new_node

    def remove_at(self,idx):
        if(idx == 0):
            self.head = self.head.next
        else:
            pre_node = self.head
            current = self.head
            for _ in range(idx-1):
                pre_node = pre_node.next
                current = current.next
            current = current.next    
            pre_node.next = current.next
    
    def print_all(self):
        current = self.head
        while current.next:
            print(current.value,"->", end=" ")
            current = current.next
        print(current.value)    


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.remove_at(3)
ll.print_all()
