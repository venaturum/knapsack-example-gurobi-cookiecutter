from abc import ABC

import gurobipy as gp
import gurobipy_exceptions as gp_exc


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
