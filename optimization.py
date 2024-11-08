from scipy.optimize import minimize

import objectiveFunction

def optimize():
    x=[0,0,0,0,0,0]
    fun = objectiveFunction.objective_function
    result = minimize(fun,x)

    return result