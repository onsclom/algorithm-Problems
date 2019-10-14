def removeKthNodeFromEnd(head, k):
    scanner = head
	
    count = 0
    while scanner.next != None:
    	scanner = scanner.next
    	count += 1
		
    count = count - k
	
    if count < 0:
    	head.value = head.next.value
    	head.next = head.next.next
    	return
	
    remover = head
    for x in range(count):
    	remover = remover.next
	
    remover.next = remover.next.next
	
    return
    