#!/usr/bin/python

from point import point

def recursiveHull(points):
	if len(points) <= 3:
		return points
	pts = sorted(points, key=lambda point: point.x)
	leftHull = recursiveHull(pts[:len(points)/2])
	rightHull = recursiveHull(pts[len(points)/2:])

	x = leftHull[0]
	for p in leftHull:
		if x.x < p.x:
			x = p

	y = rightHull[0]
	for p in rightHull:
		if y.x > p.x:
			y = p

	# While the line x-y is not tangent to both hulls (on the bottom) do  {
	# 	While x-y is not tangent to the left hull, let x be the next clockwise point in the left hull.
	# 	While x-y is not tangent to the right hull, let y be the next counterclockwise point in the right hull.
	# }
	# When this loop is finished, x will be Bottom_left and y will be Bottom_right.  A similar method can be used to determine Top_left and Top_right. 


	

ps = [point("A", 0, 0), point("B", -5, -2), point("C", -2, -1), point("D", -6, 0), point("E", -3.5, 1), point("F", -4.5, 1.5), point("G", -2.5, -5), point("H", 1, -2.5), point("I", 2.5, .5), point("J", -2.2, 2.2)]

print(recursiveHull(ps))