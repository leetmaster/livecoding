# FoxDot Tutorial 2: Patterns and TimeVars

a=[0,1,2] * 2

# List comprehension
a = [i * 2 for i in [0,1,2]]

# Creating patterns
# Like lists but an operation affects the whole list
a = Pattern([0,1,2])

b = P[0,1,2,3:9]
# Add a number to each item
b = P[0,1,2,3] + 100

# Add a new number to the end
b = P[0,1,2,3] | 100

help(Pattern)
 
print(b)

print(P[0,1,2].stretch(8))

b = P[0,1,2] * 2
p1 >> pluck(b.stretch([5,3]), dur=PDur(3,8), amp=1/4)

p2 >> bass(PTri([2,6],8), amp=1/2, dur=PDur(4,8,3))

p1 >> pluck(PDur(3,8))

p3 >> play("(x-)(-x)o-", amp=1/2, dur=1/2) 

#  a list of values and a list of durations (in beats)
a = var([0,1,2,3],[4,2,1,1])

b1 >> bass(var.chords, dur=1/2)

#Creating a chord
var.chords = var([0,4,5,3], 4)

p1.stop()
