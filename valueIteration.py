# AI - Homework 3
# Value Iteration
# Kathy Xie, Monica Kuo

y = 1
e = 0.001
MAX_ITERS = 1000

# input - an MDP with states s (2D array)
#       - actions A (N, NE, E, SE, S, SW, W, NW, stay)
#       - transition model Pr (s′ | s, a)
# output - the value (utility) of each state s in S
def valueIteration(U, case):
	# initialize Up, everything equal to 0
	rows = len(U)
	cols = len(U[0])
	Up = [[0 for x in range(rows)] for y in range(cols)]

	iterator = 0
	sigma = 1
	while(sigma >= e or iterator < MAX_ITERS):
		iterator += 1
		U = Up
		sigma = 0
		# for each state s in S
		for i in range(0, rows):
			for j in range(0, cols):
				s = (i, j)
				# find all the states that can result from all possible actions at current state
				#A = possibleActions(s, case)
				A = [(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1,1)]
				# Up[i][j] = R(s) + y*max(sum(Pr(sp, s, A)*U[ip][jp]))
				maxValue = None
				for a in A:
					if case == 1:
						sp = ( (a[0] + s[0]), (a[1] + s[1]) )
					elif case == 2:
						if(s[1] in range(3, 6)):
							sp = ( (a[0] + s[0]-1), (a[1] + s[1]) )
						else:
							sp = ( (a[0] + s[0]), (a[1] + s[1]) )
					elif case == 3:
						if(s[1] in range(3, 6)):
							sp = ( (a[0] + s[0]-2), (a[1] + s[1]) )
						else:
							sp = ( (a[0] + s[0]), (a[1] + s[1]) )

					#bounds checking
					if (sp[0] > 6):
						sp = (6, sp[1])
					if (sp[0] < 0):
						sp = (0, sp[1])
					if (sp[1] > 6):
						sp = (sp[0], 6)
					if (sp[1] < 0):
						sp = (sp[0], 0)

					probability = U[sp[0]][sp[1]]#Pr(sp, s, a)*
					if(maxValue == None):
						maxValue = probability
					else:
						maxValue = max(maxValue, probability)

				if(maxValue != None):
					Up[i][j] = R(s) + y*maxValue

				if (abs(Up[i][j] - U[i][j]) > sigma):
					sigma = abs(Up[i][j] - U[i][j])
	return Up


# transition model Pr (s′ | s, a)
def Pr(sp, s, a):
	sa = ( (a[0] + s[0]), (a[1] + s[1]) )
	if(sp == sa):
		return 1
	else:
		return 0

# possible actions A at a certain state s
def possibleActions(s, case):
	size = 7
	directions = [(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1,1)]
	A = []

	# consider actions in all 9 directions
	for i in range(0, len(directions)):
		direction = directions[i]

		# case I - no wind, no change
		if(case == 1):
			sp = ( (direction[0] + s[0]), (direction[1] + s[1]) )
			# valid only when location is in bounds
			inBounds = isValid(sp)
			if(inBounds):
				A.append(direction)

		# case II - light wind
		# wind blows along columns 3-5 from south to north, row reduced by 1
		if(case == 2):
			wind = False
			if(s[1] in range(3, 6)):
				wind = True
				direction = ( direction[0] - 1, direction[1] )

			sp = ( (direction[0] + s[0]), (direction[1] + s[1]) )
			# valid only when location is in bounds
			if(isValid(sp)):
				A.append(direction)
			else:
				if (sp[0] > 6):
					sp = (6, sp[1])
				if (sp[0] < 0):
					sp = (0, sp[1])
				if (sp[1] > 6):
					sp = (sp[0], 6)
				if (sp[1] < 0):
					sp = (sp[0], 0)
				#if (isValid(sp)):
					#A.append(direction)
			'''
			# if wind blew us out of map, push us back onto map
			elif(wind == True):
				sp = ( (sp[0] + 1), sp[1] )
				if(isValid(sp)):
					A.append(direction)
			'''

		# case III - strong wind
		# wind blows along columns 3-5 from south to north, row reduced by 2
		if(case == 3):
			wind = False
			if(s[1] in range(3, 6)):
				wind = True
				direction = ( direction[0] - 2, direction[1] )

			sp = ( (direction[0] + s[0]), (direction[1] + s[1]) )
			# valid only when location is in bounds
			if(isValid(sp)):
				A.append(direction)
			else:
				if (sp[0] > 6):
					sp = (6, sp[1])
				if (sp[0] < 0):
					sp = (0, sp[1])
				if (sp[1] > 6):
					sp = (sp[0], 6)
				if (sp[1] < 0):
					sp = (sp[0], 0)

			'''
			# if wind blew us out of map, push us back onto map
			elif(wind == True):
				sp = ( (sp[0] + 1), sp[1] )
				if(isValid(sp)):
					A.append(direction)
				else:
					sp = ( (sp[0] + 1), sp[1] )
					if(isValid(sp)):
						A.append(direction)
			'''
	return A

# Reward Function
def R(s):
	if(s[0] == 3 and s[1] == 6):
		return 0
	else:
		return -1

# is state on map
def isValid(s):
	if(0 <= s[0] and s[0] < 7 and 0 <= s[1] and s[1] < 7):
		return True
	else:
		return False

if __name__ == "__main__":
	# call value Iteration function for three cases
	for i in range(1, 4):
		U = [[0 for x in range(7)] for y in range(7)]
		Up = valueIteration(U, i)
		print("case " + str(i))
		for row in Up:
			print(row)
		print()
