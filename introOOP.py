class ChanceNode:
    def __init__(self,probs,costs):
        self.probs = probs
        self.costs = costs

    def get_expected_cost(self):
        num_outcomes=len(self.costs)
        exp_cost = 0 #expected cost
        for i in range(num_outcomes):
            exp_cost += self.costs[i]*self.probs[i]
        return exp_cost


#create object

myChanceNode = ChanceNode([0.1,0.2,0.7],[10,20,30])
print(myChanceNode.get_expected_cost())

