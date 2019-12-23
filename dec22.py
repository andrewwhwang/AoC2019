import numpy as np

inputs="""cut 9002
deal with increment 17
cut -4844
deal with increment 26
cut -4847
deal with increment 74
deal into new stack
deal with increment 75
deal into new stack
deal with increment 64
cut 9628
deal with increment 41
cut 9626
deal with increment 40
cut -7273
deal into new stack
deal with increment 20
deal into new stack
cut 2146
deal with increment 7
cut -3541
deal with increment 25
cut -1343
deal with increment 42
cut -2608
deal with increment 75
cut -9258
deal into new stack
cut -2556
deal into new stack
cut -5363
deal into new stack
cut -8143
deal with increment 15
cut -9309
deal with increment 65
cut -5470
deal with increment 9
deal into new stack
deal with increment 64
cut 137
deal with increment 40
deal into new stack
cut 5042
deal with increment 74
cut 4021
deal with increment 39
cut -5108
deal with increment 50
cut -6608
deal with increment 64
cut 4438
deal with increment 48
cut 7916
deal with increment 23
cut -6677
deal with increment 27
cut -1758
deal with increment 32
cut -3104
deal with increment 37
cut 9453
deal with increment 20
deal into new stack
deal with increment 6
cut 8168
deal with increment 69
cut 6704
deal with increment 45
cut -9423
deal with increment 2
cut -3498
deal with increment 39
deal into new stack
cut 6051
deal with increment 42
cut 7140
deal into new stack
deal with increment 73
cut -8201
deal into new stack
deal with increment 13
cut 2737
deal with increment 3
cut -4651
deal into new stack
deal with increment 30
cut -1505
deal with increment 59
deal into new stack
deal with increment 55
cut 8899
deal with increment 39
cut 8775
deal with increment 57
cut -1919
deal with increment 39
cut -3845
deal with increment 8
cut -4202"""

# inputs = """deal with increment 3"""

# part 1
def increment(deck, inc):
    newDeck = [None] * len(deck)
    for i, card in enumerate(deck):
        newDeck[(i*inc)%len(deck)] = card
    return newDeck

def newStack(deck):
    return deck[::-1]

def cut(deck, loc):
    return deck[loc:] + deck[:loc]

def parse(inputs, deck):
    lines =  inputs.split("\n")
    for line in lines:
        words = line.split(" ")
        if words[0] == "cut":
            deck = cut(deck, int(words[1]))
        elif words[1] == "with":
            deck = increment(deck, int(words[3]))
        elif words[1] == "into":
            deck = newStack(deck)
    return deck

deck = list(range(10007))
deck = parse(inputs,deck)
print(deck.index(2019))

# part 2
iterations = 101741582076661
deckSize = 119315717514047
pos = 2020

# multiply two matrices with modulo
def matrix_mult(matA, matB):
    return ((matA[0]*matB[0] + matA[1]*matB[2]) % deckSize,
            (matA[0]*matB[1] + matA[1]*matB[3]) % deckSize,
            (matA[2]*matB[0] + matA[3]*matB[2]) % deckSize,
            (matA[2]*matB[1] + matA[3]*matB[3]) % deckSize)

# matrix logaritmic exponentiation
def matrix_power(mat, exp):
    mul = mat
    ans = (1,0,0,1)
    while exp > 0:
        if exp % 2 == 1:
            ans = matrix_mult(mul, ans)
        exp //= 2
        mul = matrix_mult(mul, mul)
    return ans

def getSinglePass(inputs):
    increment, offset = 1, 0
    lines =  inputs.split("\n")
    for line in lines:
        words = line.split(" ")
        if words[0] == "cut":
            offset -= int(words[1])
            offset %= deckSize
        elif words[1] == "with":
            increment *= int(words[3])
            increment %= deckSize
            offset *= int(words[3])
            offset %= deckSize
        elif words[1] == "into":
            increment *= -1
            increment %= deckSize
            offset = -1 * (offset+1)
            offset %= deckSize
    return increment, offset

# Ai + B = pos
# where A = increment, B = offset
#
# [A B]  *  [i]   =    Ai + B = pos
# [0 1]     [1]
# transformation matrix * initial values = final values
# singlePass = A and B for 1 pass of instructions
# exponentiate for multiple passes
increment, offset = getSinglePass(inputs)
incTotal, offTotal = matrix_power((increment,offset,0,1), iterations)[:2]

# Ai + B = pos
# (incTotal)i + (offTotal) = pos
# (incTotal)i = pos - offTotal
# i = (pos - offTotal) * inv(incTotal)
#
# where inv = a^(p-2) % p (fermat's little theorem)
inv = pow(incTotal, deckSize-2, deckSize)
print((inv*(pos-offTotal))%deckSize)