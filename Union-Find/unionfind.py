"""
Implementing union find data structure
"""

class UnionFind:
    """
    Union Find (Disjoint Set) Data Structure with Weighting & Path Compression

    Weighting: always connect smaller tree (by number of nodes) to bigger tree
    during union operation guarantees O(logn) find and union

    Path Compression: during each find, point all nodes along traversed path directly
    to root, improves algorithm to O(1) amortized
    """

    def __init__(self, numNodes):

        #parent[nodeNum] = root of nodeNums connected componenent
        self.parent = []
        self.numComponents = numNodes


        #Stores size of each connected component
        self.size = []

        #Assign all nodes to individual components at init
        for i in range(numNodes):
            self.parent.append(i)
            self.size.append(1)


    def connected(self, nodeA, nodeB):

        return self.find(nodeA) == self.find(nodeB)

    def union(self, nodeA, nodeB):
        """
        Merge set containing nodeA and nodeB
        Point smaller tree to larger tree
        """

        if self.connected(nodeA,nodeB):
            print('Already connected')
            return


        aRoot = self.find(nodeA)
        bRoot = self.find(nodeB)

        if self.size[aRoot] > self.size[bRoot]:
            self.parent[bRoot] = aRoot

            self.size[bRoot] += self.size[aRoot]

        else:
            self.parent[aRoot] = bRoot

            self.size[aRoot] += self.size[bRoot]


        self.numComponents -= 1

        #Debug
        print(nodeA, "and", nodeB, "now belong to group", self.find(nodeA))


    def find(self, node):
        """
        Return id of targetNode set
        """

        #id[i] is the parent of node i
        #when id[i] == i you are at the root of a connected componenet

        currNode = node

        while (self.parent[currNode] != currNode):
            """
            Traverse up the tree until root is reached
            """

            #Update node / Traverse upwards
            currNode = self.parent[currNode]

        #Once complete currNode is the root of the component

        #Complete path compression before return
        while (node != currNode):
            nextNode = self.parent[node]
            self.parent[node] = currNode
            node = nextNode




        return currNode








def main():

    myUF = UnionFind(10)


    myUF.union(1,2)
    myUF.union(3,4)
    myUF.union(5,6)
    myUF.union(7,8)

    print(myUF.numComponents)





if __name__ == '__main__':
    main()






