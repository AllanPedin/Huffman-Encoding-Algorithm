class node:
    #edges: list of other nodes max length should be r
    #probability: probability of this symbol occuring
    #symbol: symbol
    def __init__(self, edges, probability, symbol):
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