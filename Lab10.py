# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Name     : Shreyas Keerthi
# Pledge   : I pledge my honor that I have abided by the Stevens honor system.
# Purpose  : 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Power:
#  - Write a RECURSIVE hmmm function that gets two numbers,
#   then prints (No.1 ^ No.2).
#  - Assumptions: No.1 is any integer, No.2 ≥ 0
#  - 0 ^ 0 can either be 0 or 1.
#  - Your function MUST be recursive.
#   No points will be given for solutions that
#   do not use the hmmm recursive/stack structure
#   See week9.pdf for more insight into that.

#reg usage
#r1 n^n
Power = """
00 setn r15 69 #init stack pointa
01 read r2
02 read r3
03 calln r14 6
04 write r1
05 halt

06 jeqzn r3 19

07 addn r15 1
08 storer r3 r15
09 addn r15 1
10 storer r14 r15

11 addn r3 -1
12 calln r14 6

13 loadr r14 r15
14 addn r15 -1
15 loadr r3 r15
16 addn r15 -1

17 mul r1 r1 r2
18 jumpr r14

19 setn r1 1
20 jumpr r14


"""



# ~~~~~ Running ~~~~~~
import hmmm
import importlib

runThis = Power  # Change to the function you want to run
doDebug = False # Change to turn debug mode on/off

# call main() from the command line to run the program again
def main(runArg = runThis, debugArg = doDebug):
    importlib.reload(hmmm)
    hmmm.main(runArg, debugArg)

if __name__ == "__main__" : 
    main()
