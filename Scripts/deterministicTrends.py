from scipy.optimize import curve_fit

def objective_linear(x,a,b):
    return a*x + b

def objective_cuadratic(x,a,b,c):
    return a*x*2 + b*x + c

def objective_cubic(x,a,b,c,d):
    return a*x**3 + b*x**2 + c*x + d
