#!/usr/bin/python
import gevent
import gevent.select
import sys

# gevent replacement for input()
def ginput( prompt ):
	sys.stdout.write( prompt )
	sys.stdout.flush()
	gevent.select.select([sys.stdin], [], [])
	return sys.stdin.readline()

# Test the gInput function
def getInput():
	while True:
		print("received: " + ginput( "give me data: "))

# Prove that the reactor is running
def count():
	x = 1
	while True:
		gevent.sleep(5)
		x = x + 1
		print("count: %d" % x)

gevent.spawn( getInput )
count()