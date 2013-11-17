#!/bin/python

class point:
	def __init__(self,name,x,y):
		self.name = name
		self.x = x
		self.y = y

	# returns negative if p1 is left of p2, positive if p1 is right of p2
	def orient(self, p1, p2):
		return ((p1.x  - self.x) * (p2.y - self.y)) - ((p1.y - self.y) * (p2.x - self.x))
	
	def sort(self, points):
		pts = points[:]
		pts.remove(self)
		for i in range(len(pts)):
			for j in range(len(pts)-1):
				if self.orient(pts[j+1], pts[j]) < 0:
					tmp = pts[j+1]
					pts[j+1] = pts[j]
					pts[j] = tmp
		return pts

	def __repr__(self):
		return self.name + "(" + str(self.x) + "," + str(self.y) + ")"

def findBot(points):
	bot  = points[0]
	for i in points:
		if (i.y < bot.y) or (i.y == bot.y and i.x < bot.x):
			bot = i
	return bot


#skips number of points that it goes backwards
def grahmScan(points):
	stack = []
	bottom = findBot(points)
	sort = bottom.sort(points)
	stack.append(bottom)
	stack.append(sort[-1])

	i = len(sort)-1
	while i >= 0:
		if stack[-2].orient(sort[i-1],stack[-1]) < 0:
			stack.append(sort[i-1])
		else:
			stack.pop()
		i -= 1

	return stack

def jarvis(points):
	hull =[]
	current = findBot(points)
	hull.append(current)
	current = current.sort(points)[-1]
	while True:
		if current == hull[0]:
			break
		hull.append(current)
		current = current.sort(points)[-1]
	return hull




ps = [point("A", 0, 0), point("B", -5, -2), point("C", -2, -1), point("D", -6, 0), point("E", -3.5, 1), point("F", -4.5, 1.5), point("G", -2.5, -5), point("H", 1, -2.5), point("I", 2.5, .5), point("J", -2.2, 2.2)]

print("Grahm: " + str(grahmScan(ps)))
print("Jarvis: " + str(jarvis(ps)))

test = []
for i in range(1000):
	i += 1
	test.append(point(str(i), i, i**2))

print("Grahm: " + str(grahmScan(test)))
print("Jarvis: " + str(jarvis(test)))

test += [point("1001", 0, 0), point("1002", 1001, 0), point("1003", 1001, 1002001)]

print("Grahm: " + str(grahmScan(test)))
print("Jarvis: " + str(jarvis(test)))