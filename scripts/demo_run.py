from knapsack.models.my_models import MyKnapsack

# Builds and optimises
my_knapsack = MyKnapsack.run(v=[1, 1, 2], w=[1, 2, 3], c=4, MIPFocus=1)

my_knapsack.print_solution()
