import huffman
import node

def testHuffman(r, probability_distribution):
    encoder = huffman.Huffman_Encoder(r)
    encoder.buildTree(probability_distribution)
    print("Generated Tree:")
    node.print_tree(encoder.tree_base, 0) 
    encoder.encode()
    print("Encoding:")
    print(encoder.encoding)

def print_new_test_case(test_num , r, probability_distribution):
    print("-------TEST CASE "+str(test_num) +"-------")
    print("r = ", r)
    print("pdist = ", probability_distribution, "Length = ", len(probability_distribution))
tests = [
    #(r, probability_distribution)
    (2,[0.44,0.21,0.12,0.1,0.07]),
    (3,[0.44,0.21,0.12,0.1,0.07]),
    (2,[0.008,0.002,0.01,0.02,0.03,0.044,0.05,0.05,0.06,0.07,0.088,0.09,0.12,0.1,0.22,0.004,0.033,0.001]),
    (3,[0.008,0.002,0.01,0.02,0.03,0.044,0.05,0.05,0.06,0.07,0.088,0.09,0.12,0.1,0.22,0.004,0.033,0.001]),
    (2,[0.1859,0.1031,0.0796,0.0642,0.0632,0.0575,0.0574,0.0514,0.0484,0.0467,0.0321,0.0317,0.0228,0.0218,0.0208,0.0198,0.0175,0.0164,0.0152,0.0152,0.0127,0.0083,0.0049,0.0013,0.0008,0.0008,0.0005]),
    (3,[0.1859,0.1031,0.0796,0.0642,0.0632,0.0575,0.0574,0.0514,0.0484,0.0467,0.0321,0.0317,0.0228,0.0218,0.0208,0.0198,0.0175,0.0164,0.0152,0.0152,0.0127,0.0083,0.0049,0.0013,0.0008,0.0008,0.0005]),
    (4,[0.1859,0.1031,0.0796,0.0642,0.0632,0.0575,0.0574,0.0514,0.0484,0.0467,0.0321,0.0317,0.0228,0.0218,0.0208,0.0198,0.0175,0.0164,0.0152,0.0152,0.0127,0.0083,0.0049,0.0013,0.0008,0.0008,0.0005]),
    (5,[0.1859,0.1031,0.0796,0.0642,0.0632,0.0575,0.0574,0.0514,0.0484,0.0467,0.0321,0.0317,0.0228,0.0218,0.0208,0.0198,0.0175,0.0164,0.0152,0.0152,0.0127,0.0083,0.0049,0.0013,0.0008,0.0008,0.0005])
] 
for i in range(0, len(tests)):
    r, probability_distribution = tests[i]
    print_new_test_case(i, r, probability_distribution)
    testHuffman(r, probability_distribution)
