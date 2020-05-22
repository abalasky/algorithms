"""
Implementation of Gale/Shapley Algorithm to produce stable matching

Using problem statement and input data from :
http://rosettacode.org/wiki/Stable_marriage_problem#Python

"""


def gs(men, women, prefs):
    """
    Takes a list of men & women and individual complete preference lists
    and returns a stable matching of all men to all women
    """

    """
    The G-S algorithm generates ONE men-optimal stable matching
    by allow unmatched men to continuously propose to women (matched or unmatched)
    in order of their preference list. A woman accepts if she is unmatched or if the man is
    higher on her preference list then her current match. The algorithm temrinates when all men are matched
    """

    #List of unmatched men (men)
    #List of all women (women)
    #Preference list for each man will contain ONLY women to whom he has not propsed(prefs)

    #Dictionary of current pairings, key = woman name
    pairs = {}

    #Men is a list of unmatched men
    print(men)

    for man in men:

        print('On man', man)

        #Propose to women in order of his preference list
        for woman in prefs[man]:

            #Woman immediatly accepts if not already paired
            if woman not in pairs:
                # Add pairing between woman and main to pairs dict
                pairs[woman] = man
                break
            else:
                #Woman is paired and decides using her preference list

                womPrefs = prefs[woman]
                curr = womPrefs.index(pairs[woman])

                #If current man is lower on womans preference list she switches
                if curr < womPrefs.index(man):
                    currMan = pairs[woman]
                    pairs[woman] = man
                    #Remove the man who paired from the list and add the man
                    #who unpaired to the list
                    men.append(currMan)
                    break


    return pairs


import sys

def main():
    """
    Read input from files supplied in command line, run G-S algorithm, output results
    """

    #Get list of men
    with open(sys.argv[1]) as f:
        men = f.read()
        men = men[:-1].split(',') #remove /n
        men = [man.strip() for man in men]

    #Get list of women
    with open(sys.argv[2]) as f:
        women = f.read()
        women = women[:-1].split(',')
        women = [woman.strip() for woman in women]

    #Get dictionary format of preference lists
    prefs = {}
    with open(sys.argv[3]) as f:
        for line in f:
            prefList = line[:-1].split(':')

            #Get list of all names in current pref list
            names = prefList[1].split(',')
            names = [name.strip() for name in names]
            #Map preference list to person
            prefs[prefList[0]] = names


    #Run G-S algorithm
    pairings = gs(men, women, prefs)

    #Print out the pairings
    print(pairings)



if __name__ == '__main__':
    """
    python3 gs.py men.txt women.txt preferences.txt
    """
    main()












