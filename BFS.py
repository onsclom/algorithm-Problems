class treeNode:
    def __init__(self, value):
        self.val = value
        self.leftChild = 0
        self.rightChild = 0

    def BFS(self, root, value):
        curQueue = []

        if root.val == value:
            return root

        if root.leftChild != 0:
            if root.leftChild.val == value:
                return root.leftChild
            else:
                curQueue.append(root.leftChild)
            curQueue.append(root.leftChild)
        if root.rightChild != 0:
            if root.rightChild.val == value:
                return root.rightChild
            else:
                curQueue.append(root.rightChild)

        while (len(curQueue)>0):
            curPointer = curQueue.pop(0)

            if curPointer.leftChild != 0:
                if curPointer.leftChild.val == value:
                    return curPointer.leftChild
                else:
                    curQueue.append(curPointer.leftChild)
                    curQueue.append(curPointer.rightChild)

            if curPointer.rightChild != 0:
                if curPointer.rightChild.val == value:
                    return curPointer.rightChild
                else:
                    curQueue.append(curPointer.rightChild)
                    curQueue.append(curPointer.leftChild)

        return -1



#making tree
dTree = treeNode("D")
dTree.rightChild=treeNode("I")
dTree.leftChild=treeNode("H")

eTree = treeNode("E")
eTree.rightChild=treeNode("K")
eTree.leftChild=treeNode("J")

fTree = treeNode("F")
fTree.rightChild=treeNode("M")
fTree.leftChild=treeNode("L")

gTree = treeNode("G")
gTree.rightChild=treeNode("O")
gTree.leftChild=treeNode("N")

bTree = treeNode("B")
bTree.rightChild=eTree
bTree.leftChild=dTree

cTree = treeNode("C")
cTree.rightChild=gTree
cTree.leftChild=fTree

root = treeNode("A")
root.rightChild=cTree
root.leftChild=bTree




#testing
print(root.BFS(root, "E").val)
print(root.BFS(root, "T"))
