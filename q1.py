#!/usr/bin/python

from point import point

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

	i = len(sort)-2
	while i >= 0:
		#print(stack)
		if stack[-2].orient(sort[i],stack[-1]) < 0:
			stack.append(sort[i])
		else:
			stack.pop()
			i +=1
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
ps = [point("A", 0, 0), point("B", -5, -2), point("C", -2, -1), point("D", -6, 0), point("E", -3.5, 1), point("F", -4.5, 1.5), point("G", -2.5, -5), point("H", 1, -2.5), point("I", 2.5, .5), point("J", -2.2, 2.2)]
# print(ps)
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