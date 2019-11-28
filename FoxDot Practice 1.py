# FoxDot Tutorial 1: Basics

print("Hello World")

2+2

# We create a player object and assign the value of the function pluck
# We can pass a single value or a list
# If one of the elements of the list is another list the object will play a sequence
p1 >> pluck([0,1,2,3,[4,5]], chop = 1)

p1 >> pluck(oct=6,[0,1,2,(3,[5,7],9)], chop=1)

p1.stop()

foo = Player()

foo >> pluck()

foo.stop()

print(SynthDefs)

p2 >> blip(oct=4, dur=[1/2, 1/4,1/4])

p2.stop()

Clock.bpm = 120

Clock.clear()

print(Clock.bpm)

Scale.default = 'dorian'

print(Scale.names())

p3 >> play("x-o[--]")

p3 >> play("x-o(-[--])")

p3 >> play("x-o{-[--][-o][-----]}", sample = [1])

p4 >> noise([1,(1,2,1),1,1,1], amp=1/2)

p5 >> bass([2,2,4,4,2,2,6,6], amp=1, dur=1/4)

p6 >> bell([6,4,(2,3),8,6], amp=1/2, dur=1/2)

p.stop()

print (Player.Attributes())
