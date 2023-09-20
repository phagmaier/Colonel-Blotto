#Basically just brute forcing this 
#converges much faster without learning rate
#with a learning rate of 1 (basically negating it) and 200 iterations it converges on the optimal strategy
class Player:
	def __init__(self,iterations=200,lr=1):
		self.lr = lr
		self.iterations = iterations
		self.gameplans = self.starting_strat()
		self.mixed_strat = [1/len(self.gameplans) for _ in range(len(self.gameplans))]

	def train(self):
		for _ in range(self.iterations):
			self.regrets = self._train()
			self.update()


	def _train(self):
		regrets = []
		for options,percentages in zip(self.gameplans, self.mixed_strat):
			regrets.append(self.regret(options,percentages))
		return regrets

	def regret(self, plan,pct):
		total = 0
		for i,x in zip(self.gameplans,self.mixed_strat):
			total += self.loss_win(i,plan) * pct * x
		return total

	def loss_win(self, mine,opp):
		count = 0
		for i,x in zip(mine,opp):
			if i> x:
				count -=1
			elif x> i:
				count += 1
		if count >0:
			return 1
		elif count < 1:
			return -1
		else:
			return 0

	def update(self):
		temp = []
		for i,x in enumerate(self.regrets):
			temp.append(self.mixed_strat[i] + self.lr * x)
		total = sum(temp)
		self.mixed_strat = [temp[i]/total for i in range(len(self.mixed_strat))]


	def starting_strat(self):
		#function to get all possible strategies
		numbers = [i for i in range(6)]
		valid_permutations = []
		for i in numbers:
		    for j in numbers:
		        for k in numbers:
		            if i + j + k == 5:
		                valid_permutations.append((i, j, k))
		return valid_permutations



if __name__ == "__main__":
	#Basically just brute forcing this 
	#converges much faster without learning rate
	#with a learning rate of 1 (basically negating it) and 200 iterations it converges on the optimal strategy
	p1 = Player(iterations=200,lr=1)
	p1.train()
	saved = [i for i in range(len(p1.gameplans)) if p1.mixed_strat[i] > .009]


	for i in saved:
		print(f" Play {p1.gameplans[i]} this percentage {p1.mixed_strat[i] * 100}%")

