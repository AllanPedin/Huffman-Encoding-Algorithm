import node
#r : radix for huffman encoding (int)
#probability_distribution : probability distribution for huffman encoding (list of decimals b/t 0,1... must add up to 1)

class Huffman_Encoder:
    def __init__(self, r):
        self.r = r
    def encode(self, probability_distribution):
        nodes = list(map(self.probabilty_to_node, probability_distribution))
        while len(nodes)>1:
            nodes.sort(key = self.take_node_value)
            group = nodes[:self.r] #get first r from our list
            new_node = node.node(self.r, group, self.sum_node_probabilities(group)) #new node which contains first r nodes
            nodes = nodes[self.r:] #remove first r items
            nodes.append(new_node) #replace first r items with node containing them as edges
        print_tree(nodes[0])
    def sum_node_probabilities(self, nodes):
        sum = 0
        for node in nodes:
            sum = sum + node.value
        return sum
    def probabilty_to_node(self, probability):
        return node.node(self.r, [], probability)
    def take_node_value(self, node):
        return node.value
def print_tree(base_node):
    print(base_node.value)
    for node in base_node.edges:
        print_tree(node)

encoder = Huffman_Encoder(2)
encoder.encode([.2,.3,.4,.1])
