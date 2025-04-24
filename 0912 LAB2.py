'''I pledge my honor that I have abided by the Stevens Honor System'''
'''Shreyas Keerthi'''

def myLen(x):
    if(x==[] or x==""):
        return 0
    else:
        return 1+myLen(x[1:])

def dotProduct(L,K):
    if(L==[] or K==[]):
        return 0
    return L[0]*K[0]+dotProduct(L[1:],K[1:])

def expand(S):
    if S=="":
        return []
    return [S[0] + expand(S[1:])]
    

def deepMember(e,L):
    if L ==[]:
        return False
    if isinstance(L[0], list):
        if deepMember(e,L[0])==True:
            return True
        else:
            return deepMember(e,L[1:])
        if e==L[0]:
            return deepMember(e,L[1:])
    
    

def removeAll(e,L):

    if L==[]:
        return []
    if e==L[0]:
        return removeAll(e, L[1:])

def deepReverse(L):
    if L==[]:
        return []
    if isinstance(L[-1], list):
        return[deepReverse(L[-1])] + deepReverse(L[0:len(L)-1])
    return [L[-1]] + deepReverse(L[0:len(L)-1])
