from math import inf

def validateBst(tree, min = -inf, max = inf):
	if tree == None:
		return True
	
	if tree.value >= min and tree.value < max:
		return validateBst(tree.left, min, tree.value) and validateBst(tree.right, tree.value, max)
	
	return False