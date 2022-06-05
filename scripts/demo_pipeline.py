from knapsack.models.my_models import MyKnapsack

my_gurobi_model = MyKnapsack.make_model(  # returns gurobipy.Model
    v=[1, 1, 2], w=[1, 2, 3], c=4
)

my_gurobi_model.setParam("MIPFocus", 1)

my_gurobi_model.optimize()

print("Solution:")

for v in my_gurobi_model.model.getVars():
    print(f"{v.VarName} = {v.X}")
