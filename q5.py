#!/usr/bin/python

import traceback

#is it possible to achieve sum k using first n numbers?
#P is the recursive solution
def P(numbers, n, k):
	if k == 0:
		return True
	if n == 0:
		return False

	return P(numbers, n-1, k) or P(numbers, n-1, k-numbers[n])

#P2 is the dynamic solution
def P2(numbers, n, k):
	if k == 0:
		return (True, numbers)
	if n == 0:
		return (False, numbers)

	notUsed = numbers[:]
	arr = [[False for h in range(k+1)] for g in range(n+1)]
	for i in range(n+1):
		for j in range(k+1):
			if j == 0:
				arr[i][j] = True
			elif i == 0:
				arr[i][j] = False
			else:
				try:
					if arr[i-1][j]:
						arr[i][j] = arr[i-1][j] 
					elif arr[i-1][j-numbers[i-1]]:
						arr[i][j] = arr[i-1][j-numbers[i-1]]
						try:
							notUsed.remove(numbers[i-1])
						except:
							pass
				except IndexError:
					traceback.print_exc()
					arr[i][j] = False

	return (arr[n][k], notUsed)





votes = [3,3,3,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,6,6,6,7,7,7,7,8,8,9,9,9,10,10,10,10,11,11,11,11,12,13,15,15,15,17,20,21,21,27,31,34,55]

target = sum(votes)//2
tup = P2(votes, len(votes), target)

if tup[0] == False:
	print("False")
else:
	vc = votes[:]
	for i in tup[1]:
		vc.remove(i)
	print("Used in first half: " + str(vc))

	tup2 = P2(tup[1], len(tup[1]), target)
	#If there are no leftovers and it returns true then it is true else it is false
	print(tup2[0] and len(tup2[1]) == 0)
	if tup2[0] and len(tup2[1]) == 0:
		print("Used in second half: " + str(tup[1]))