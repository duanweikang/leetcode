### for this problem, we can keep two pointers, p1 and p2
### since we are looking for the nth node from the end
### we can let p1 goes n first, then let p2 start from the head node.
### thus as we can see, p1 is n nodes ahead of p2
### then after p1 reach the end, p2 reach the nth element from the end 
### this is because p1 is n nodes ahead of p2

def removeNthFromEnd(self, head, n):
	dummy=ListNode(0);
	dummy.next = head
	p1 = dummy
	p2 = dummy
	# p1 move first for n nodes
	for i in range(n):
		p1 = p1.next
    # then move p1 and p2 both, p2 begin from head
    # stop when p1 reach the end node
    while p1.next:
    	p1 = p1.next
    	p2 = p2.next

    # delete the nth node from the end
    p2.next = p2.next.next

    return dummy.next