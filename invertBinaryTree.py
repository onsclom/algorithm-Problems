def invertBinaryTree(tree):
    queue = [tree]
    while len(queue):
        cur = queue.pop(0)
        cur.left, cur.right = cur.right, cur.left
        if cur.left != None:
            queue.append(cur.left)
        if cur.right != None:
            queue.append(cur.right)
    return tree