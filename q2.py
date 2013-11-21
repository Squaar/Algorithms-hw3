#!/usr/bin/python

from point import point

def recursiveHull(points):
	if len(points) <= 3:
		return points
	pts = sorted(points, key=lambda point: point.x)
	leftHull = recursiveHull(pts[:len(points)//2])
	rightHull = recursiveHull(pts[len(points)//2:])

	x = 0
	for p in range(len(leftHull)):
		if leftHull[x].x < leftHull[p].x:
			x = p

	y = 0
	for p in range(len(rightHull)):
		if rightHull[y].x > rightHull[p].x:
			y = p
	
	zRight = y - 1
	zLeft = x - 1
	while leftHull[x].orient(rightHull[zRight], rightHull[y]) < 1 and rightHull[y].orient(leftHull[zLeft], leftHull[x]) > 1:
		while leftHull[x].orient(rightHull[zRight], rightHull[y]) < 1:
			x = x - 1 if x - 1 >= 0 else len(leftHull) - 1
		while rightHull[y].orient(leftHull[zLeft], leftHull[x]) > 1:
			y = y - 1 if y - 1 >= 0 else len(rightHull) - 1

	botLeft = x
	botRight = y

	x = 0
	for p in range(len(leftHull)):
		if leftHull[x].x < leftHull[p].x:
			x = p

	y = 0
	for p in range(len(rightHull)):
		if rightHull[y].x > rightHull[p].x:
			y = p

	zRight = y - 1
	zLeft = x - 1
	while leftHull[x].orient(rightHull[zRight], rightHull[y]) > 1 and rightHull[y].orient(leftHull[zLeft], leftHull[x]) < 1:
		while leftHull[x].orient(rightHull[zRight], rightHull[y]) > 1:
			x = x + 1 if x + 1 < len(leftHull) else 0
		while rightHull[y].orient(leftHull[zLeft], leftHull[x]) < 1:
			y = y + 1 if y + 1 < len(rightHull) else 0

	topLeft = x
	topRight = y

	hull = []
	hull.append(leftHull[topLeft])
	hull.append(rightHull[topRight])
	current = topRight
	while current is not botRight:
		hull.append(rightHull[current])
		curent += 1 if current + 1 < len(rightHull) else 0
	hull.append(rightHull[botRight])
	current = botLeft
	while current is not topLeft:
		hull.append(leftHull[current])
		current += 1 if current + 1 < len(leftHull) else 0

	return hull


	# While the line x-y is not tangent to both hulls (on the bottom) do  {
	# 	While x-y is not tangent to the left hull, let x be the next clockwise point in the left hull.
	# 	While x-y is not tangent to the right hull, let y be the next counterclockwise point in the right hull.
	# }
	# When this loop is finished, x will be Bottom_left and y will be Bottom_right.  A similar method can be used to determine Top_left and Top_right. 


	

ps = [point("A", 0, 0), point("B", -5, -2), point("C", -2, -1), point("D", -6, 0), point("E", -3.5, 1), point("F", -4.5, 1.5), point("G", -2.5, -5), point("H", 1, -2.5), point("I", 2.5, .5), point("J", -2.2, 2.2)]

print(recursiveHull(ps))
