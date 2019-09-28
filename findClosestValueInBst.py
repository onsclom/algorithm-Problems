# recursive solution
# def findClosestValueInBst(tree, target):
# 	return findCVhelper(tree, target, tree.value)
	
# def findCVhelper(tree, target, closest):
# 	newClosest = closest
# 	if (abs(closest-target)>abs(tree.value-target)):
# 		newClosest = tree.value
	
#     if (tree.value == target):
# 		return tree.value
# 	elif (tree.value < target):
# 		if (tree.right == None):
# 			return newClosest
# 		return findCVhelper(tree.right, target, newClosest)
# 	else:
# 		if (tree.left == None):
# 			return newClosest
# 		return findCVhelper(tree.left, target, newClosest)

# iterative solution
def findClosestValueInBst(tree, target):
	closest = tree.value
	current = tree
	while (current != None):
		if abs(closest-target) > abs(current.value-target): 
			closest = current.value
		if current.value == target:
			return target
		elif current.value < target:
			current = current.right
		else:
			current = current.left
	return closest