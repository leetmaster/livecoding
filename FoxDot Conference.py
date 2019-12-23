# dur changes the duration of the note
# every n beats calls a function performed x times
# chop and room effects make it sound cooler

p1 >> blip([0,4], dur=PDur(3,8), sus=2, chop=4, room=0.5).every(3, "offadd", 2).every(5, "stutter", 4, dur=3, oct=5)

# some background ambient
p2 >> klank(var([0,2],8))

# some chords
p3 >> piano(var([0,3,5,4]) + (0,2,4,const(7),const(9)), dur=PDur(3,8)*2, oct=4)

p1 >> blip([1,2], dur=PDur(1,2), sus=2, chop=1).every(4, "offadd", 2).every(7, "stutter", 4, dur=2, oct=4)

# Some percussion to add things together
d1 >> play("X O ")
