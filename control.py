from sys import stdin
from subprocess import call

def begin(tagId):
	call(["./first", tagId])

while True:
	print "Enter a number: "
	uinput = stdin.readline()
	begin(uinput)




