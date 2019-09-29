# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

	#this problem looks for a function called depthFirstSearch() 
	#so rename one of these for answer
    def iterativeDepthFirstSearch(self, array):
        stack = []
        stack.append(self)
        while (len(stack) > 0):
            current = stack.pop()
            array.append(current.name)
            for x in reversed(current.children):
                stack.append(x)
        return array

    def recursiveDepthFirstSearch(self, array):
        array.append(self.name)
        for x in self.children:
            x.recursiveDepthFirstSearch(array)
        return array
	