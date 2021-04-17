class node:
    #r: r-ary node (has r edges)
    #edges: list of other nodes max length should be r
    #probability: probability of this symbol occuring
    #symbol: symbol
    def __init__(self, r, edges, probability, symbol):
        if r < len(edges):
            raise Exception("More edges than r, r=" + r + " edges = ", edges)
        self.r = r
        self.edges = edges
        self.probability = probability
        self.symbol =  symbol
    def to_string(self):
        return self.symbol + "("+str(self.probability) +")"
    def is_leaf(self):
        if len(self.edges) <=0:
            return True
        else:
            return False
def print_tree(base_node, depth):
    tabs = get_tabs(depth)
    print(tabs, base_node.to_string() )

    for sub_node in base_node.edges:
        print_tree(sub_node, depth  + 1)
def get_tabs(num):
    tabs = ""
    for i in range(0, num):
        tabs = tabs + "\t"
    return tabs