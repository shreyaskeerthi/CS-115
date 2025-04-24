#shreyas keerthi
#I pledge my honor that I have abided by the Stevens honor system
import turtle

def svTree(trunkLength, depth):
    if depth>0 and trunkLength>0:
        turtle.forward(trunkLength)
        turtle.left(20)
        svTree(trunkLength/2, depth-1)
        turtle.right(40)
        svTree(trunkLength/2, depth-1)
        turtle.left(20)
        turtle.backward(trunkLength)
        
