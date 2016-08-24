### for this question, we can just compare elements of two link list, and always add the smallest one
### to the new one, if one linked list finished, we can just link the new list with the left over linked list

def mergeTwoLists(self, l1, l2):
	dummy = ListNode(0)
	tmp = dummy
	while l1 != None and l2 != None:
	    if l1.val < l2.val:
	       tmp.next = l1
	       l1 = l1.next
	    else:
	       tmp.next = l2
	       l2 = l2.next
	    tmp = tmp.next
	if l1 != None:
	    tmp.next = l1
	else:
	    tmp.next = l2
	return dummy.next 