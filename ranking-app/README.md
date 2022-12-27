# Ranking list script
Short Python script that takes entries from a file, pairs all of them and asks the user which one of the two wins. Then it prints the entries ranked, sorted by the number of wins.

Right now it matches each entry against all other entries, resulting in the match count being the *n*-th triangular number with the number of entries being *n+1*. This makes the number of choices the user has to make unreasonably high for higher numbers of entries - for example with 5 entries there are 10 choices to make, but having 15 choices you need to resolve 105 match-ups.

### TODO (may or may not ever implement)
* Printing the results to file
* Option to reduce the number of matches in a fair way
* Make ties take the same place in ranking
* Option to go back and change an answer 
* Pretty up the prompts
* Add usage description to this README


