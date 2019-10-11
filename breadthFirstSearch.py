class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
        while (len(queue)>0):
            cur = queue.pop(0)
            array.append(cur.name)
            for x in cur.children:
                queue.append(x)
        return array