import node
#r : radix for huffman encoding (int)
#probability_distribution : probability distribution for huffman encoding (list of decimals b/t 0,1... must add up to 1)

class Huffman_Encoder:
    def __init__(self, r):
        self.r = r
        self.tree_base = None
    def buildTree(self, probability_distribution):
        nodes = self.convert_to_nodes(probability_distribution)
        while len(nodes)>1:
            nodes.sort(key = self.take_node_value)
            group = nodes[:self.r] #get first r from our list
            new_node = node.node(self.r, group, self.sum_node_probabilities(group), "P") #new node which contains first r nodes
            nodes = nodes[self.r:] #remove first r items
            nodes.append(new_node) #replace first r items with node containing them as edges
        self.tree_base = nodes[0]
        # print(self.encode_tree(nodes[0], ""))
    #base_node : base of your tree
    #path : path so to base_node so far (empty string at stump)
    #returns: encoding for tree
    def encode_tree(self, base_node, path):
        if base_node.is_leaf():
            return [path]
        else:
            encoding = []
            edges = base_node.edges
            for i in range(len(edges)):
                subtree = self.encode_tree(edges[i], path + str(i))
                encoding.extend(subtree)
            return encoding
    def sum_node_probabilities(self, nodes):
        sum = 0
        for node in nodes:
            sum = sum + node.probability
        return sum
    def convert_to_nodes(self, probability_distribution):
        nodes = []
        for i in range(0,len(probability_distribution)):
            nodes.append(node.node(self.r, [], probability_distribution[i],"S"+str(i+1)))
        return nodes
    def take_node_value(self, node):
        return node.probability
