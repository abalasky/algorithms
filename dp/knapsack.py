"""
Dynamic programming solution to 0/1 knapsack
"""
import numpy as np


def knapsack(items, weight):
    """
    Maximizes value of items given a weight limit
    """

    #Init DP Table x: 0->items y: 0 ->weight
    opt = np.zeros((len(items)+1, weight+1), dtype = int)

    #Fill out base cases i.e. first row/first column
    for w in range(weight+1):
        opt[0][w] = 0

    for i in range(1,len(items)+1):

        for w in range(weight+1):

            if items[i-1][1] > w:
                opt[i][w] = opt[i-1][w]

            else:

                opt[i][w] = max(
                        opt[i-1][w],
                        items[i-1][2] + opt[i-1][w-items[i-1][1]]
                )

    print(opt)

    #Find optimal solution
    knapsackItems = []
    currWeight = weight
    currItem = len(items)
    for i in range(len(items)):
        if opt[currItem][w] == opt[currItem-1][currWeight]:
            currItem -= 1
            continue

        weightNew = currWeight - items[currItem][1]
        if opt[currItem][w] - items[currItem][1] == opt[currItem-1][weightNew]:
            knapsackItems.append(items[0][0])
            currItem -= 1
            currWeight -= items[currItem][1]

    print(knapsackItems)

    return opt[len(items)][weight]


def main():

    #List of tuples itemName-weight-value
    items = [
        ("map", 9, 150), ("compass", 13, 35), ("water", 153, 200), ("sandwich", 50, 160),
        ("glucose", 15, 60), ("tin", 68, 45), ("banana", 27, 60), ("apple", 39, 40),
        ("cheese", 23, 30), ("beer", 52, 10), ("suntan cream", 11, 70), ("camera", 32, 30),
        ("t-shirt", 24, 15), ("trousers", 48, 10), ("umbrella", 73, 40),
        ("waterproof trousers", 42, 70), ("waterproof overclothes", 43, 75),
        ("note-case", 22, 80), ("sunglasses", 7, 20), ("towel", 18, 12),
        ("socks", 4, 50), ("book", 30, 10),
    ]

    value = knapsack(items,400)
    print('Knapsack returned:', value)

if __name__ == '__main__':
    main()
