# FoxDot Tutorial 2: Patterns and TimeVars

a=[0,1,2] * 2

# List comprehension
a = [i * 2 for i in [0,1,2]]

# Creating patterns
a = Pattern([0,1,2])

b = P[0,1,2,3:9]
# Add a number to each item
b = P[0,1,2,3] + 100

# Add a new number to the end
b = P[0,1,2,3] | 100

help(Pattern)

print(b)

print(P[0,1,2].stretch(8))

p1 >> pluck(P[0,1,2].stretch([5,3]), dur=PDur(3,8))

p1 >> pluck(PTri(10))

p1 >> pluck(PDur(3,8))

print(Scale.names())

print(Scale.default) 

Scale = 'major'
print(PTri(10))

p1.stop()
