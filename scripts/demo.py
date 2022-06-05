from knapsack.models.my_models import MyKnapsack

my_knapsack = MyKnapsack(v=[1, 1, 2], w=[1, 2, 3], c=4, MIPFocus=1)

my_knapsack.optimize()

print("Solution:")
my_knapsack.print_solution()
