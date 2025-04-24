from functools import reduce

def longestString(ListOfWords):
    def newList(strng):
        return [len(strng), strng]
    def check(prev):
        return reduce(max, map(newList, prev))
    return check(ListOfWords)[1]

#I pledge my honor that I have abided by the Stevens Honor System
#Shreyas Keerthi
