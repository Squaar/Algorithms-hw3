import math

class point:
	def __init__(self,name,x,y):
		self.name = name
		self.x = x
		self.y = y

	# returns negative if p1 is left of p2, positive if p1 is right of p2
	def orient(self, p1, p2):
		return ((p1.x  - self.x) * (p2.y - self.y)) - ((p1.y - self.y) * (p2.x - self.x))
	
	#bubble sort
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

	#better sort
	# def sort2(self, points):
	# 	pts = points[:]
	# 	pts.remove(self)
	# 	return sorted(pts, key=lambda point: self.angle(point))

	# def angle(self, point):
	# 	return -math.atan2((self.y - point.y) , (self.x - point.x))

	# def __cmp__(self, x):
	# 	return self.orient(point("", self.x, self.y+1), x)

	def __repr__(self):
		return self.name + "(" + str(self.x) + "," + str(self.y) + ")"
