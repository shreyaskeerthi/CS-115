'''
Name:Shreyas Keerthi
Date:9/23/19
CS115 - HW 2 ~ Recursion
Pledge: I pledge my honor that I have abided by the Stevens Honor System
'''

def makeChange(val, coins):
    
    if val==0:
        return [0,[]]
    if coins==[]:
        return [float("inf"),[]]
    if len(coins)== 1 and val % coins[0] != 0:
        return[float('inf'),[]]
    if val < coins[0]:
        return makeChange(val, coins[1:])

   
    use_it=makeChange((val)-coins[0], coins)
    use_it[0]+=1
    use_it[1] += [coins[0]]
    lose_it = makeChange(val, coins[1:])

    if min(use_it[0],lose_it[0]) == use_it[0]:
        return use_it
    return lose_it
    
    


def LCS (a , b ):
    if not (a and b):
        return ""
    if ( a[0]==b[0]):
        return a[0] + LCS(a[1:], b[1:])
    useIt = LCS(a,b[1:])
    loseIt = LCS(a[1:],b)
    
    if max(len(loseIt),len(useIt))==len(useIt):
        return useIt
    return loseIt



def PLCS(a, b):
    if isinstance(a,str) and isinstance(b,str):
        return [PLCS(a,[LCS(a,b),0]),PLCS(b,[LCS(a,b),0])]
    if isinstance(b,list):

        lcs = b[0]
        if lcs != "":
            index = a.find(lcs[0])
            oindex = index + b[1]
        
            return [oindex] + PLCS(a[index:],[lcs[1:],oindex])
        else:
            return []

    

