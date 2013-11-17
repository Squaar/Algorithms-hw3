#!/usr/bin/python

from point import point

def recursiveHull(points):
	if len(points) <= 3:
		

ps = [point("A", 0, 0), point("B", -5, -2), point("C", -2, -1), point("D", -6, 0), point("E", -3.5, 1), point("F", -4.5, 1.5), point("G", -2.5, -5), point("H", 1, -2.5), point("I", 2.5, .5), point("J", -2.2, 2.2)]

print(recursiveHull(ps))