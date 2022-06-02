# A knapsack example using cookiecutter-gurobi-poetry

What follows below will aim to achieve two outcomes.  The first is to demonstrate the use of `cookiecutter`, with the `cookiecutter-gurobi-poetry` template to produce a project.  The second is to provide motivation for the template structure and the intent for how it should be used.

This example will be presented as an informal tutorial.  It will assume a familiarity with the [Gurobi Solver](https://www.gurobi.com/), the Python package `gurobipy`, and a basic knowledge of Python - however intermediate concepts will be introduced along the way including classes, inheritance and closures.

To facilitate this tutorial we will consider two knapsack problems.  One is an extension of the other, and both are very similar to the simple Mixed Integer Program (MIP) that is featured in Gurobi's [mip1.py](https://www.gurobi.com/documentation/9.5/examples/mip1_py.html) example.

The following are required for this tutorial

 - Python 3.8+
 - Gurobi Solver installed, with valid license
 - [Cookiecutter](https://github.com/cookiecutter/cookiecutter)
 - [Poetry](https://python-poetry.org/docs/#installation)

## Problem description

Given three items, with values $v_{1}, v_{2}, v_{3}$, and weights $w_{1}, w_{2}, w_{3}$, find the combination with highest total value such that the total weight is less than a value $c$.

To formulate the model, the following binary variables will be used:

- $x_{1} = 1$ if item 1 is chosen, and $0$ otherwise
- $x_{2} = 1$ if item 2 is chosen, and $0$ otherwise
- $x_{3} = 1$ if item 3 is chosen, and $0$ otherwise

The objective function and single constraint is modelled with the following,

$$
\begin{alignat}{2}
  \text{max}\ & v_{1}x_{1} + v_{2}x_{2} + v_{3}x_{3},
  \\
  \text{s.t.}\ & w_{1}x_{1} + w_{2}x_{2} + w_{3}x_{3} \leq c,\\
  & x_{1}, x_{2}, x_{3} \in \{0, 1\}.
\end{alignat}
$$

The steps to building this model with `cookiecutter-gurobi-poetry` will now be detailed.


## Step 1) - Initialise project

Run the following in a terminal:

    cookiecutter https://github.com/venaturum/cookiecutter-gurobi-poetry.git

and provide the following answers to the prompts:

    full_name [George B. Dantzig]: (enter your name)
    email [optimality@extreme.point]: (enter your email)
    project_name [My Gurobi project]: A knapsack example with cookiecutter-gurobi-poetry
    project_slug [A-knapsack-example-with-cookiecutter-gurobi-poetry]: knapsack
    short_description [My organised, modern, reproducible optimisation project.]: A simple Integer Program for a small knapsack problem, made with  cookiecutter-gurobi-poetry
    version [0.1.0]:
    Select command_line_interface:
    1 - none
    2 - argparse
    Choose from 1, 2 [1]: 2
    Select open_source_license:
    1 - MIT license
    2 - Apache Software License 2.0
    3 - GNU General Public License v3.0
    4 - GNU General Public License v2.0
    5 - BSD 3-Clause 'New' or 'Revised' License
    6 - GNU Lesser General Public License v2.1
    7 - BSD 2-Clause 'Simplified' License
    8 - Not open source
    use_gurobipy_exceptions [y]: y
    use_notebooks [n]: n
    use_pandas [n]: n
    use_matplotlib [n]: n
    use_seaborn [n]: n
    use_isort [y]: y
    use_black [y]: y
    use_flake8 [y]: y
    use_precommit [y]: n


## Step 2) - Install dependencies and project

In the terminal, navigate to the folder ("knapsack") that cookiecutter has created.

Assuming Poetry has been installed, run the following command which instructs Poetry to resolve project dependencies, write the lock file (poetry.lock), and install the dependencies in a virtual environment (based off project name)

    poetry install

Then activate the shell (i.e. the virtual environment) with

    poetry shell

and take note of the name that Poetry gives to your virtual environment - it may come in handy for whatever IDE you are using (if you are using an IDE).


## Step 3) - Create your first module

Open the project in your favourite IDE and familiarise yourself with the structure of the project.  

*If you don't have a favourite IDE then VSCode is highly recommended.  Once installed you can open up the project in VSCode by running `code .` in the terminal.*

Create a module called `my_models.py` within the *knapsack/models/* directory.  Next add the `GRB` namespace from `gurobipy` and import the `GurobiBaseModel` that is defined inside `base.py`.

    from gurobipy import GRB

    from knapsack.models.base import GurobiBaseModel

We can refer to the knapsack package in this way because Poetry installs the project (in editable mode) in the virtual environment.


## Step 4) - Create your first class


We'll create a class called `MyKnapsack` by extending the `GurobiBaseModel`.  Add the following to `my_models.py`:

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

The body of the constructor, saves *v*, *w*, and *c* as instance attributes then calls the constructor of the superclass (ie. `GurobiBaseModel`).

A couple of things to note:

- the line `name = "my knapsack"` defines a class attribute for `MyKnapsack`.  Look at the constructor for `GurobiBaseModel` and note that if a name is not defined, then the class default will be used for the underlying `gurobipy.Model` object.
- the `**kwargs` parameter in the constructor allows an arbitrary number of keyword arguments to be specified.  These get passed to the GurobiBaseModel constructor where they are assumed to be parameters on the underlying `gurobipy.Model` object.


## Step 5 - Understand the structure of GurobiBaseModel

Take a look at the `GurobiBaseModel` constructor.  It calls the constructor of its superclass, then possibly sets the `name` instance attribute, then creates and assigns a `gurobipy.Model` object, and then calls its `_build` method.

The `_build` method calls several methods, in order, corresponding to

- adding variables
- updating model
- adding constraints
- setting objective
- setting an initial solution
- updating model

With the exception of the model updates, these methods all belong to the GurobiBaseModel class, however note there is not meaningful definitions for these functions - that is the job of the MyKnapsack class, which inherits these methods.


## Step 6 - Overwrite the inherited functions

Next we will add the following definitions in the `MyKnapsack` class.  In doing so we are overwriting the inherited methods.

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

Note that when using `self.model` we are calling the `GurobiBaseModel.model` method, which returns the underlying `gurobipy.Model` object.  Although a method, it appears as an attribute thanks to the `@property` decorator.

Also note that the *x* variables are assigned as instance attributes, and referred to when adding constraints, and setting the objective.  Be aware there are more efficient ways of adding variables, but is stated in this form for simplicity.


### Step 7 - Add an extra method

We do not have to overwrite every method that is defined in the `GurobiBaseModel` superclass.  For instance, we are not providing an initial solution, so do not define the corresponding method in the `MyKnapsack` class - it will simply inherit the "empty" method.

We are also not resricted to only defining methods which are specified in the superclass.  Add the following to `MyKnapsack` so that we can easily see the solution, if we wish.

    def print_solution(self):
        for v in self.model.getVars():
            print(f"{v.VarName} = {v.X}")


### Step 8 - Give it a spin


Open a Python shell, or Gurobi shell, in your virtual environment.  Run the following:

    >> from knapsack.models.my_models import MyKnapsack
    >> m = MyKnapsack(v=[1,1,2], w=[1,2,3], c=4, MIPFocus=1)

The first line imports the `MyKnapsack` class we defined.
The second line creates an object of this type.  Note that in doing so we are setting the `MIPFocus` parameter of the underlying `gurobipy.Model` to 1.  Alternatively we could have used `m.model.setParam("MIPFocus", 1)` after creating the object.

Creating the `MyKnapsack` object has built the model, so next we run the `optimize` method on our object, which calls the method of the same name on the underlying `gurobipy.Model`.

    >> m.optimize()

You will likely see output from the Gurobi Solver.  Once it has solved the model, use the `print_solution` method that was defined on MyKnapsack.

    >> m.print_solution()

which results in

    x1 = 1.0
    x2 = 0.0
    x3 = 1.0

So the optimal solution is to choose the first and third objects!  Next we will modify the problem by adding a constraint and see how we can achieve this with the project design.


### Step 9 - Another constraint!

For the purposes of demonstration, lets define a second problem by assuming a further restriction to the problem which declares that item 1 and 3 cannot both be chosen together (and the optimal solution found above is no longer valid).  This requirement corresponds to the following constraint

$$ x_{1} + x_{3} \leq 1$$

The simplest implementation is to define a new class `MyKnapsack2`, which extends `MyKnapsack`, and overwrites the function responsible for adding constraints:

    class MyKnapsack2(MyKnapsack):

        def _add_constraints(self):
            super()._add_constraints()
            self.model.addConstr(self.x1 + self.x3 <= 1, "c1")

In this definition, we first call the `_add_constraints` method in the superclass (`MyKnapsack`), which will add the constraint defined in the initial problem, and then we add the new constraint.  Note that we could have written these lines in any order.


### Step 10 - Here we go again

Run the following

    >> from knapsack.models.my_models import MyKnapsack2
    >> m2 = MyKnapsack2(v=[1,1,2], w=[1,2,3], c=4)
    >> m2.optimize()
    >> m2.print_solution()

which (after output from the Gurobi Solver) results in:

    x1 = 1.0
    x2 = 1.0
    x3 = 0.0

The new solution is to choose the first and second item!


### Step 11 - Defining a callback

The `_generate_root_sol_callback` method defined on `GurobiBaseModel` was another empty method that we did not overwrite in the `MyKnapsack` (or `MyKnapsack2`) subclass.  The idea is that the result of this method should be passed into the `optimize` method of the underlying `gurobipy.Model`.  If the function is not defined then it will simpy pass `None` in, which is equivalent to not passing anything at all.  What sort of argument is the `optimize` method expecting, if not `None`?  It is expecting *a function*, specifically ones with parameters *model* and *where*.

Functions are ["first class citizens"](https://en.wikipedia.org/wiki/First-class_function) in Python, which is developer-speak for saying we can do lots of fun stuff with them, including assigning to a variable, or returning them from another function.  The latter is what we will do with the code below.  Specifically, let's define a callback which records the current phase in the MIP solution.  We'll assume we have a list defined as an instance attribute in `MyKnapsack2` called `mipsol_phase1` then define the following:

    def _generate_root_sol_callback(self):
        def callback(model, where):
            if where == GRB.Callback.MIPSOL:
                self.mipsol_phase.append(model.cbGet(GRB.Callback.MIPSOL_PHASE))

        return callback

What we have done here is not trivial, and can be confronting for those new to Python.  We are defining a function called `callback` which gets returned when we call `_generate_root_sol_callback`.  This callback is responsible for querying the MIP solution phase and appending it to a list, but note that the list will be an attribute of `MyKnapsack2` objects.  This construct is called a ["closure"](https://www.learnpython.org/en/Closures) - a function that "remembers" values.  In this case it is the "self" argument, i.e. the `MyKnapsack2` object which is remembered.  This design is very flexible and allows us to access or save data which would not usually be available through just the *model* or *where* parameters.


### Step 12 - Plug the gaps

In the previous step we assumed there was an instance attribute called `mipsol_phase`.  In this step we will make this assumption concrete.

To achieve this we need to create an empty list when initialising `MyKnapsack2` - we will need to do this in a constructor:

    def __init__(self, *args, **kwargs):
        self.mipsol_phase = []
        super().__init__(*args, **kwargs)

This sole responsibility of this constructor is to define the empty list.  It does nothing with whatever positional arguments (`*args`) or keyword arguments (`**kwargs`) are provided, other than pass them onto the superclass.


### Step 13 - One more time

Running the same code from Step 10 results in a single solution found.  After the optimisation has finished, run

    >> m2.mipsol_phase

which results in `[1]`, which indicates the solution was found during the standard MIP search, as opposed to in the *NoRel heuristic* or performing MIP solution improvement.


## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

This package was created with [`Cookiecutter`](https://github.com/cookiecutter/cookiecutter) and the [`cookiecutter-gurobi-poetry`](https://github.com/venaturum/cookiecutter-gurobi-poetry) project template.