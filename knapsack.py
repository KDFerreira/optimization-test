# By: Kevin D. Ferreira
# Date: May 4, 2019
#
# references:
# [1] https://www.cvxpy.org/index.html
# [2] https://towardsdatascience.com/integer-programming-in-python-1cbdfa240df2
# [3] https://www.programcreek.com/python/example/96863/cvxpy.Variable


import cvxpy as cp
import numpy as np

# The data for the Knapsack problem
# P is total weight capacity of sack
# weights and utilities are also specified
P = 165
weights = np.array([23, 31, 29, 44, 53, 38, 63, 85, 89, 82])
utilities = np.array([92, 57, 49, 68, 60, 43, 67, 84, 87, 72])

# The variable we are solving for
selection = cp.Variable(len(weights), boolean=True)

# The sum of the weights should be less than or equal to P
weight_constraint = weights * selection <= P

# We require exactly one item
selection_constraint = cp.sum(selection) == 1

# Our total utility is the sum of the item utilities
total_utility = utilities * selection

# We tell cvxpy that we want to maximize total utility
# subject to weight_constraint. All constraints in
# cvxpy must be passed as a list
knapsack_problem = cp.Problem(cp.Maximize(total_utility), [weight_constraint, selection_constraint])

# Solving the problem
knapsack_problem.solve(solver=cp.GLPK_MI)

print(selection.value)