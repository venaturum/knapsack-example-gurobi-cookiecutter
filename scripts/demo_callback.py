from knapsack.models.my_models import MyKnapsack2

my_knapsack = MyKnapsack2(
    v=[1, 1, 2], w=[1, 2, 3], c=4, Presolve=0, Cuts=0, Heuristics=0
)
my_knapsack.optimize()

print("mipsol_phase", my_knapsack.mipsol_phase)
