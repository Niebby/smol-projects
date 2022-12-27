from itertools import combinations
from random import shuffle
import sys

with open("in-file.txt", "r") as infile:
    # infile = ["a", "b", "c", "d"]
    contenders = {k.rstrip():0 for k in infile}
    print(contenders)
    pairings = list(combinations(contenders.keys(), 2))
    shuffle(pairings)
    print(pairings)
    for num, i in enumerate(pairings):
        print()
        print("\n\n-----   " + i[0] + "   VS   " + i[1] + "   ----- (" + str(num+1) + "/" + str(len(pairings)) + ")")
        print("Choose 1 to vote for " + i[0])
        print("Choose 2 to vote for " + i[1])
        user_choice = None
        while user_choice not in [1, 2]:
            try:
                user_choice = int(input().strip())
            except KeyboardInterrupt:
                sys.exit()
            except:
                pass
        print("Voted for " + i[user_choice-1])
        contenders[i[user_choice-1]] += 1
        
    print("\n\n\n")
    placement = 1
    for k, v in sorted(contenders.items(), key=lambda k: -k[1]):
        print(str(placement) + ".", k + "   ("+ str(v) +  " wins - " + "{:.2f}".format(100*((len(contenders.keys())-1) and v / (len(contenders.keys())-1) or 0)) + "% won)")
        placement += 1