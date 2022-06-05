from abc import ABC
from datetime import datetime

import gurobipy as gp
import gurobipy_exceptions as gp_exc

from knapsack import root_dir


class GurobiBaseModel(ABC):

    name = None

    def __init__(self, *args, name=None, **kwargs):
        super().__init__()

        if name:
            self.name = name

        self._m = gp.Model(self.name)
        self._build()

        for param, value in kwargs.items():
            self._m.setParam(param, value)

        if self._m.Params.LogFile == "":
            now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            logfile_name = (self.name + "-" if name else "") + now + ".log"
            self._m.Params.LogFile = str(root_dir / "logs" / logfile_name)

    @property
    def model(self):
        return self._m

    def _add_variables(self):
        pass

    def _add_constraints(self):
        pass

    def _set_objective(self):
        pass

    def _set_start_solution(self):
        pass

    def _build(self):
        self._add_variables()
        self._m.update()
        self._add_constraints()
        self._set_objective()
        self._set_start_solution()
        self._m.update()

    def _generate_root_sol_callback(self):
        pass

    @gp_exc.patch_error_message
    def optimize(self):
        self._m.optimize(self._generate_root_sol_callback())

    @classmethod
    def run(cls, *args, name=None, **kwargs):
        instance = cls(*args, name=name, **kwargs)
        instance.optimize()
        return instance

    @classmethod
    def make_model(cls, *args, name=None, **kwargs):
        return cls(*args, name=name, **kwargs).model
