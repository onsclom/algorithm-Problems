def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    seen = set()
    seen.add(descendantOne)
    seen.add(descendantTwo)
    while (descendantOne != None or descendantTwo != None):
            if descendantOne != None:
                descendantOne = descendantOne.ancestor
                if descendantOne in seen:
                    return descendantOne
                else:
                    seen.add(descendantOne)
            if descendantTwo != None:
                descendantTwo = descendantTwo.ancestor
                if descendantTwo in seen:
                    return descendantTwo
                else:
                    seen.add(descendantTwo)

			
