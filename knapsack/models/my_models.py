from gurobipy import GRB

from knapsack.models.base import GurobiBaseModel


class MyKnapsack(GurobiBaseModel):

    name = "my knapsack"

    def __init__(self, v, w, c, name=None, **kwargs):
        """Initialise a knapsack problem

        Parameters
        ----------
        v : list or array
            The 3 values, corresponding to v1, v2, v3.
        w : list or array
            The 3 weights, corresponding to w1, w2, w3.
        c : int or float
            The capacity.
        name : str, optional
            model name, will default to "my knapsack"
        **kwargs :
            Gurobi model parameters, as keyword arguments
        """
        self.v = v
        self.w = w
        self.c = c
        super().__init__(name, **kwargs)

    def _add_variables(self):
        self.x1 = self.model.addVar(vtype=GRB.BINARY, name="x1")
        self.x2 = self.model.addVar(vtype=GRB.BINARY, name="x2")
        self.x3 = self.model.addVar(vtype=GRB.BINARY, name="x3")

    def _add_constraints(self):
        self.model.addConstr(
            self.w[0] * self.x1 + self.w[1] * self.x2 + self.w[2] * self.x3 <= self.c,
            "c0",
        )

    def _set_objective(self):
        self.model.setObjective(
            self.v[0] * self.x1 + self.v[1] * self.x2 + self.v[2] * self.x3,
            GRB.MAXIMIZE,
        )

    def print_solution(self):
        for v in self.model.getVars():
            print(f"{v.VarName} = {v.X}")


class MyKnapsack2(MyKnapsack):
    def __init__(self, *args, **kwargs):
        self.mipsol_phase = []
        super().__init__(*args, **kwargs)

    def _generate_root_sol_callback(self):
        def callback(model, where):
            if where == GRB.Callback.MIPSOL:
                self.mipsol_phase.append(model.cbGet(GRB.Callback.MIPSOL_PHASE))

        return callback

    def _add_constraints(self):
        super()._add_constraints()
        self.model.addConstr(self.x1 + self.x3 <= 1, "c1")
