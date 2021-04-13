class node:
    #r : r-ary node (has r edges)
    #edges: list of other nodes max length should be r
    def __init__(self, r, edges, value):
        if r < len(edges):
            raise Exception("More edges than r, r=" + r + " edges = ", edges)
        self.r = r
        self.edges = edges
        self.value = value