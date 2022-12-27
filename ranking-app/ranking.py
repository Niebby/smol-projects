from itertools import combinations
from random import shuffle
import sys

with open("in-file.txt", "r") as infile:
    # infile = ["borgar", "hotdog", "kebab", "taco"]
    contenders = {k.rstrip():0 for k in infile}

# print(contenders)
pairings = list(combinations(contenders.keys(), 2))
shuffle(pairings)
# print(pairings)
for i, matchup in enumerate(pairings):
    print()
    print("\n\n-----   " + matchup[0] + "   VS   " + matchup[1] + "   ----- (" + str(i+1) + "/" + str(len(pairings)) + ")")
    print("Choose 1 to vote for " + matchup[0])
    print("Choose 2 to vote for " + matchup[1])
    user_choice = None
    while user_choice not in [1, 2]:
        try:
            user_choice = int(input().strip())
        except KeyboardInterrupt:
            sys.exit()
        except:
            pass
    print("Voted for " + matchup[user_choice-1])
    contenders[matchup[user_choice-1]] += 1
        
with open("out-file.txt", "w") as outfile:
    print("\n\n\n")
    placement = 1
    for k, v in sorted(contenders.items(), key=lambda k: -k[1]):
        print_string = str(placement) + ". " + k + "   ("+ str(v) +  " wins - " + "{:.2f}".format(100*((len(contenders.keys())-1) and v / (len(contenders.keys())-1) or 0)) + "% won)\n"
        outfile.write(print_string)
        print(print_string, end='')
        
        placement += 1
