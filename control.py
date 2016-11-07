from sys import stdin
from subprocess import call

def begin(tagId):
	call(["./display", tagId])

while True:
	print "Enter a number: "
	uinput = stdin.readline()
	begin(uinput)




