#I pledge my honor that I have abided by the Stevens Honor System
#Shreyas Keerthi

#Create a function which takes in an int called amount and list called coins and return least amount of strings
#use recursion
#use use it or lose it(check notes)
#essentially two paths, find most optimal path






def change(amount, coins):
    if amount==0:
        return 0
    if amount<0 or coins==[]:
        return float("inf")
    use_it=change((amount)-coins[0], coins) + 1
    lose_it=change(amount, coins[1:])
    return(min(use_it, lose_it))
