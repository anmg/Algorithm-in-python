class Node(object):
    '''node'''
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleLinkList(object):
    def __init__(self, node = None):
        self.__head = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        cur = self.__head

        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur != None:
            print cur.elem, " "
            cur = cur.next

    def add(self, item):
        '''O(1)'''
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item)
        '''O(n)'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
           cur = self.__head
           while cur.next != None:
               cur = cur.next
           cur.next = node

    def insert(self, pos. item):
        if pos < 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos - 1)
                pre = pre.next
                count += 1
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        pre = self.__head

        if pre.elem == item:
           self.__head = pre.next
        else:
           while pre.next != None:
               if pre.next.elem == item:
                   pre.next = pre.next.next
               else:
                   pre = pre.next


