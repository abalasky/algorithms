"""

An implementation of DNA sequence alignment using
dynamic programming

"""

import sys
import numpy as np

def seq_align(s1,s2):
    """
    Takes two sequences, returns minimum edit distance
    DP iterative
    """

    #DP table of size n+1 * m+1 where n = len(s1) and m = len(s2)
    #s1 vertical, s2 horizontal

    seq = np.zeros((len(s1)+1, len(s2)+1), dtype = int)

    #Fill out base cases in DP table
    for j in range(len(s2)):
        #Bottom Row: How many left in s2?
        seq[len(s1)][j] = len(s2) - j

    for i in range(len(s1)):
        #Far Right Col: How many left in s1?
        seq[i][len(s2)] = len(s1) - i

    seq[len(s1)][len(s2)] = 0


    #Fill out remaining table
    #Bottom to Top, Right to Left
    for i in reversed(range(0,len(s1))):
        for j in reversed(range(0,len(s2))):
            if s1[i] == s2[j]:
                seq[i][j] = seq[i+1][j+1]
            else:
                seq[i][j] = 1 + min (
                        seq[i+1][j+1],
                        seq[i+1][j],
                        seq[i][j+1]
                    )

    # #Reconstruct Sequence
    # s1match = []
    # s2match = []
    # i = len(s1)
    # j = len(s2)
    # while i != 0 && j != 0:
    #     up =
    #     left
    #     diag


    return seq[0][0]

def seq_helper(s1,s2, i, j):
    """
    Recursive formulation for seq_align
    """
    if (i == len(s1)):
        return (len(s2) - j) * -2
    if (j == len(s2)):
        return (len(s1) - i)*-2

    if (s1[i] == s2[j] ):
        return seq_helper(s1,s2,i+1, j+1)
    else:
        return 1 + min(
            seq_helper(s1,s2,i+1,j+1),
            seq_helper(s1,s2,i+1,j),
            seq_helper(s1,s2,i, j+1)
        )

def main():
    s1 = input('Supply first sequence:')
    s2 = input('Supply second sequence:')
    print('Minimum edit distance:')
    print(seq_align(s1,s2))




if __name__ == '__main__':
    main()
