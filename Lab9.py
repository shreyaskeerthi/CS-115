# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Name    : Shreyas Keerthi
# Pledge  : I pledge my honor that I have abided by the Stevens Honor System
# Purpose : To enhance my understanding of machine code, assembly language, and the basics of computers
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Max:
#  Write a hmmm function that gets two numbers,
#   then prints the larger of the two.
#  Assumptions: Both inputs are any integers
Max = """
00	read r1
01	read r2
02	sub r3 r1 r2
03	sub r4 r2 r1
04	jltzn r4 06
05	jltzn r3 08
06	write r1
07	halt
08	write r2
09	halt


"""


# Power:
#  Write a hmmm function that gets two numbers,
#   then prints (No.1 ^ No.2).
#  Assumptions: No.1 is any integer, No.2 ≥ 0
Power = """
00 read r1
01 read r2
02 setn r3 1
03 mul r3 r3 r1
04 addn r2 -1
05 jgtzn r2 03
06 write r3
07 halt

"""


# Fibonacci
#  Write a hmmm function that gets one numner,
#   then prints the No.1st fibonacci number.
#  Assumptions: No.1 ≥ 0
#  Hint: You really don't want to implement
#   recursion in hmmm, try to find an
#   iterative method to compute your goal.
#  Tests: f(2) = 1
#         f(5) = 3
#         f(9) = 34
Fibonacci = """
00 read r1
01 setn r12 0
02 setn r13 1
03 setn r14 0
04 jeqzn r1 10
05 add r14 r13 r12
06 copy r12 r13
07 copy r13 r14
08 addn r1 -1
09 jumpn 4
10 write r12
11 halt


"""


# ~~~~~ Running ~~~~~~
RunThis = Fibonacci
doDebug = False

if __name__ == "__main__" : 
    import hmmm
    hmmm.main(RunThis, doDebug)


