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
def valueIteration(U, A, R): 
	# initialize Up, everything equal to 0
	rows = len(U)
	cols = len(U[0])
	Up = [[0 for x in range(rows)] for y in range(cols)]

	i = 0 
	sigma = 1
	while(sigma >= e or i > MAX_ITERS):
		i += 1
		U = Up
		sigma = 0
		# for each state s in S 
		for i in range(0, rows):
			for j in range(0, cols):
				s = (i, j)
				Up[i][j] = R(s) + y*max()*sum(Pr(s, A))*U

				if abs(Up[i][j] - -U[i][j] > sigma):
					sigma = abs(Up[i][j] - -U[i][j])



# transition model Pr (s′ | s, a)
def Pr(s, a):
	

# Reward Function
def R(s):
	if(s[0] == 3 and s[1] == 6):
		return 0
	else
		return -1