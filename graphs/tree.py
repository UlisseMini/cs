class TreeNode:
    def __init__(self, id, parent=None, children=[]):
        self.id = id
        self.depth = 0
        self.parent = parent
        for child in children:
            child.parent = self
            child.inc_depth()
        self.children = children

    def inc_depth(self):
        self.depth += 1

        for child in self.children:
            child.inc_depth()


    def add_children(self, *children):
        self.children += children

    def dfs(self):
        yield self

        for child in self.children:
            yield from child.dfs()

    def __repr__(self):
        buf = '  ' * self.depth
        if self.children != []:
            children = "\n"+"\n".join(map(repr, self.children)) + "\n" + buf
            return buf + f'{self.id} {children}'
        else:
            return buf + f'{self.id}'


tree = TreeNode(1, children=[
    TreeNode(2, children=[
        TreeNode(4),
        TreeNode(5)
    ]),
    TreeNode(3),
])
