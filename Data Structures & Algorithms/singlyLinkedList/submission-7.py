class ListNode : 
    def __init__(self,val: int, next=None) : 
        self.val = val
        self.next = next


class LinkedList:
 
    def __init__(self):
      self.head = None
      self.tail = None
    
    def get(self, index: int) -> int:
        curr, idx = self.head,0
        while curr:
            if index == idx : 
                return curr.val
            curr = curr.next
            idx = idx +1
        return -1


    def insertHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head
        self.head =node
        if self.tail is None :
            self.tail = node



    def insertTail(self, val: int) -> None:
        node = ListNode(val)
        if self.tail == None: 
            self.head =node
            self.tail =node
        else : 
            self.tail.next = node
            self.tail = node

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False

        if index == 0:
            self.head = self.head.next
            if self.head is None:        # list just emptied
                self.tail = None         # <-- the missing line
            return True

        curr, prev, idx = self.head, None, 0
        while curr:
            if idx == index:
                prev.next = curr.next        # splice: ALWAYS, for any matched index
                if curr is self.tail:        # tail update: ONLY if we removed the last node
                    self.tail = prev
                return True
            prev = curr
            curr = curr.next
            idx += 1
        return False

    def getValues(self) -> List[int]:
        curr,values = self.head,[]
        while curr:
            values.append(curr.val)
            curr=curr.next
        return values

