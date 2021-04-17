import node
#r : radix for huffman encoding (int)
#probability_distribution : probability distribution for huffman encoding (list of decimals b/t 0,1... must add up to 1)

class Huffman_Encoder:
    def __init__(self, r):
        self.r = r
        self.tree_base = None
        self.encoding = None
    def buildTree(self, probability_distribution):
        nodes = self.convert_to_nodes(probability_distribution)
        while len(nodes)>1:
            nodes.sort(key = self.take_node_value)
            group = nodes[:self.r] #get first r from our list
            new_node = node.node( group, self.sum_node_probabilities(group), "P") #new node which contains first r nodes
            nodes = nodes[self.r:] #remove first r items
            nodes.append(new_node) #replace first r items with node containing them as edges
        self.tree_base = nodes[0]
        # print(self.encode_tree(nodes[0], ""))
    #base_node : base of your tree
    #path : path so to base_node so far (empty string at stump)
    #returns: encoding for tree
    def encode(self):
        self.encoding = []    
        self.encode_recursive(self.tree_base, "")


    def encode_recursive(self, node, path):
        if node.is_leaf():
            self.encoding.append((path, node.to_string()))
        else:
            edges = node.edges
            for i in range(0,len(edges)):
                self.encode_recursive(edges[i], path + str(i))

    def sum_node_probabilities(self, nodes):
        sum = 0
        for node in nodes:
            sum = sum + node.probability
        return sum
    def convert_to_nodes(self, probability_distribution):
        nodes = []
        for i in range(0,len(probability_distribution)):
            nodes.append(node.node([], probability_distribution[i],"S"+str(i+1)))
        return nodes
    def take_node_value(self, node):
        return node.probability
