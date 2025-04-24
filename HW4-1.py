from importlib import reload as Rfrsh
import hmmm

# Fibonacci! You've already done it in Lab 9
# Now however, you are to do hmmmonacci with
# recursion, & you MUST do so for any credit
# The tests are still the same as from Lab 9
# Tests: f(2) = 1 ■■■ f(5) = 5 ■■■ f(9) = 34


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Name     : Shreyas Keerthi
# Pledge   : I pledge my honor that I have abided by the Stevens Honor System.
# Purpose  : To understand recursion in assembly and HMMM
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#i'm sorry, I've been reworking this so many times, I just want to have fun)

RecFibSeq = """ # You may not need all lines
00 setn r15 69 #init da stack pointa
01 read r1 #read input
02 setn r3 0 #set sum

03 jeqzn r1 5 # check basecase
04 calln r6 7 #jump
05 write r3 # print ans
06 halt #WHY ARE YOU RUNNING


07 setn r2 0
08 setn r3 1
09 addn r1 -1

10 jnezn r1 12
11 jumpr r6

12 pushr r6 r5
13 calln r6 9

14 copy r4 r3
15 add r3 r3 r2
16 copy r2 r4
17 popr r6 r5
18 jumpr r6

"""

# Change doDebug to false to turn off debugs
runThis = RecFibSeq
doDebug = True

# Note: main() in the shell to easily reload
def main(runArg=runThis,  debugArg=doDebug):
    Rfrsh(hmmm); hmmm.main(runArg, debugArg)

if __name__ == "__main__" :
    main()
