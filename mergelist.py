class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def Merge(self, pHead1, pHead2):
        count = 0
        res = ListNode(0)
        head = res
        while(pHead1 != None and pHead2 != None):
            if pHead1.val > pHead2.val:
                count += 1
                res.next = pHead2
                pHead2 = pHead2.next
                res = res.next
            else:
                count += 1
                res.next = pHead1
                pHead1 = pHead1.next
                res = res.next
        if pHead1 == None:
           res.next = pHead2
        if pHead2 == None:
           res.next = pHead1

        return head.next

solution = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)
node8 = ListNode(8)
node9 = ListNode(9)
node1.next = node2
node2.next = node4
node4.next = node8


node3.next = node5
node5.next = node6
node6.next = node7
node7.next = node9

pMerge = solution.Merge(node1, node3)

print "------------------------"
while pMerge != None:
    print pMerge.val
    pMerge = pMerge.next

