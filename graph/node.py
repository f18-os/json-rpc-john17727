class node:
    def __init__(self, name, children = []):
        self.name = name
        self.children = children
        self.val = 0
    def value(val):
        self.val = val
    def show(self, level=0):
        print("%s%s val=%d:" % (level*"  ", self.name, self.val))
        for c in self.children: 
            c.show(level + 1)

def increment(graph):
    graph.val += 1;
    for c in graph.children:
        increment(c)

def toDict(graph):
    dict = {}
    count = 0
    dict[graph.name] = graph.val
    for c in graph.children:
        if(c.name in dict):
            name = c.name + "_" + str(count)
            count += 1
            dict[name] = c.val
        else:
            dict[c.name] = c.val
    return dict