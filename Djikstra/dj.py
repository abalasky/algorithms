"""
An implementation of djiktra's single source shortest path algorithm

"""

from queue import PriorityQueue
import random

def generateGraph(nodes, success):
    """
    Implements Erdos-Renyi Model for Random Graph Construction with numNodes nodes
    and probability = success

    Given a set of k nodes {n_1, ..., n_k}  each edge (n_i, n_j) for all i & j <= k
    where i != j is included with a uniform random probability

    More info: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model
    Implementation: https://www.youtube.com/watch?v=0SdzPJksV3Q

    @params: nodes is a list containing name of each node

    @returns list of edges with weights defaulted to 1

    @todo: modify to fit power law instead of uniform distribution

    """
    edges = []

    for i in range(0,len(nodes)):
        for j in range(i+1,len(nodes)):
            #No self loops
            if i != j:
                r = random.random()
                if r >= success:
                    # Add edge
                    edge = (nodes[i],nodes[j],1)
                    edges.append(edge)


    return edges



def makeAdjList(edges):
    """
    Takes list of edges in form: ("NodeA", "NodeB", int(weight))
    Converts to adjList wheren adjList['NodeID'] = [('NodeID', int(weight))]

    @returns dictionary adjList
    """

    # Init empty dict
    adjList = {}

    for edge in edges:
        start = edge[0]
        end = edge[1]
        weight = edge[2]

        if start in adjList and end in adjList:
            #Set already exists, add a new edge

            # Add to adj lists
            adjList[start][end] = weight
            adjList[end][start] = weight

        else:

            if start not in adjList and end not in adjList:
                adjList[start] = {}
                adjList[end] = {}
                adjList[start][end] = weight
                adjList[end][start] = weight

            elif start not in adjList:
                adjList[start] = {}
                adjList[start][end] = weight
                adjList[end][start] = weight

            else:
                adjList[end] = {}
                adjList[end][start] = weight
                adjList[start][end] = weight



    return adjList


def djikstra(adjList, start):
    """
    Executes djikstras algorithm to find the shortest path to all nodes from
    "start" node in graph adjList of size n

    Returns a list of events that show the exploration path taken by djikstra's
    algorithm
    """

    events = []

    #Declare visited set, distance dictionary, predecssor dictionary
    visited = set()
    dist = {key: None for key in adjList.keys()}
    pred = {key: None for key in adjList.keys()}

    # Add the start node to the visited set, set distance and pred
    dist[start] = 0

    #Python priority queue, takes tuples (priority, 'value')

    #Contains tuples of (d(v) - distance to vertex v, v - name of vertex v)
    #Push new tuple to PQ every time shorter path than current path in dist[v]
    #is found
    pq = PriorityQueue()
    pq.put((0,start))

    event = (f'Starting at {start}')
    events.append(event)

    while not pq.empty():

        #Pop and front, get actual node name from tuple
        currNode = pq.get()[1]

        print(f'On node {currNode}')

        #Skip this iteration of the loop
        if currNode in visited:
            continue

        #Generate event
        event = f'Traveled to {currNode} from {pred[currNode]}'
        events.append(event)



        for neighbor in adjList[currNode].keys():

            print(f"Checking {neighbor}")



            if neighbor not in visited:
                #Check if there is a better path

                #Distance to curr + w(curr, neighbor)
                newDist = dist[currNode] + adjList[currNode][neighbor]

                if dist[neighbor] == None or newDist < dist[neighbor]:
                    #We found a shorter distance
                    #Update dist, set pred, push to PQ
                    dist[neighbor] = newDist
                    pred[neighbor] = currNode
                    pq.put((dist[neighbor], neighbor))


        #Mark as visited
        visited.add(currNode)

    return events







def main():

    # nodes = []
    # for i in range(5):
    #     node = 'Node' + str(i)
    #     nodes.append(node)


    # #Create random graph using E-R model
    # edges = generateGraph(nodes, .5)

    # #Create adj list from list of edges
    # adjList = makeAdjList(edges)

    adjList = {
    'Node0': {'Node1': 4,'Node2': 1},
    'Node1':{'Node0': 4, 'Node2': 2, 'Node3': 1},
    'Node2':{'Node0':1, 'Node1': 2, 'Node3': 5},
    'Node3':{'Node1': 1, 'Node2': 5, 'Node4': 3},
    'Node4':{'Node3': 3}
    }


    import pprint
    pprint.pprint(adjList)

    start = 'Node0'
    events = djikstra(adjList, start)

    print(events)



if __name__ == '__main__':
    main()









