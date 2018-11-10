class node:
    def __init__(self, name, children = []):
        self.name = name
        self.children = children
        self.val = 0
    def show(self, level=0):
        print("%s%s val=%d:" % (level*"  ", self.name, self.val))
        for c in self.children: 
            c.show(level + 1)

def increment(graph):
    graph.val += 1
    for c in graph.children:
        increment(c)


dictList = []
def toList(graph):
    dictList.append([graph.name, graph.val])
    for c in graph.children:
        toList(c)
    return dictList

def toTree(listDict):
    children = []
    for l in listDict[1:]:
        child = node(l[0])
        child.val = (l[1])
        children.append(child)
    top = listDict[0]
    root = node(top[0], children)
    root.val = top[1]
    return root