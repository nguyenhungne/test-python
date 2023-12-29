import math
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
def golden_search(f, a, b, tol):
    phi = (np.sqrt(5) - 1) / 2
    c = b - phi * (b - a)
    d = a + phi * (b - a)
    while abs(b - a) > tol:
        if f(c) < f(d):
            b = d
        else:
            a = c
        c = b - phi * (b - a)
        d = a + phi * (b - a)
    min_x = (b + a) / 2
    return min_x

def fibonacci_search(f, a, b, tol):
    F1, F2 = 2, 3  
    n = 2  
    while abs(b - a) >= tol:
        d = b - a
        x1 = b - d * F1 / F2
        x2 = a + d * F1 / F2
        if f(x1) <= f(x2):
            b = x2
        else:
            a = x1
        n += 1
        F1, F2 = F2, F1 + F2
    min_x = (b + a) / 2
    return min_x

def plot_function(f, a, b, min_x):
    x = np.linspace(a, b, 400)
    y = f(x)
    plt.plot(x, y, label='f(x) = x^2')
    plt.plot(min_x, f(min_x), 'ro')
    plt.legend()
    plt.show()
def optimize_and_plot(f, x_range, tol, label):
    x = np.linspace(x_range[0], x_range[1], 400)
    y = f(x)
    min_y_index = np.argmin(y)
    min_x = x[min_y_index]
    print(f"The minimum value of {label} is at x =", min_x)
    plt.plot(x, y, label=label)
    plt.plot(min_x, y[min_y_index], 'ro')
x , y = sp.symbols('x y')
def find_CN(f):
    df = sp.diff(f, x)
    root = sp.solve(df, x)
    CN = []
    for i in root:
        if i.is_real:
            CN.append(i)
    return CN
def find_rex(f):
    CN = find_CN(f)
    df2 = sp.diff(f,x,2)
    for i in CN:
        if df2.subs(x,i) < 0:
            print("The function reaches its maximum value at x = ", i)
        if df2.subs(x,i) > 0:
            print("The function reaches its minimum value at x = ", i)   
def find_MaxMin(f,a,b):
    CN = find_CN(f)
    arr = [a, b]
    for i in CN:
        if(a<=i<=b):
            arr.append(i)
    Value = [f.subs(x, e) for e in arr]
    Max = max(Value)
    Min = min(Value)
    print("Maximum value = ",Max)
    print("Maximum value = ",Min)


def ex1():
    f = 3*x**4 - 16*x**3 + 18*x**2 - 9
    print("critical numbers of fa = ", find_CN(f))
    f = (x+2)/(2*x**2)
    print("critical numbers of fb = ", find_CN(f))
def ex2():
    f = 3*x**4 - 16*x**3 + 18*x**2 - 9
    print("2a : ")
    find_rex(f)
    f = (x+2)/(2*x**2)
    print("2b : ")
    find_rex(f)
def ex3():
    print("3.a")
    f = 3*x**4 - 16*x**3 + 18*x**2 - 9
    find_MaxMin(f,0,5)
    print("3.b")
    f = (x+2)/(2*x**2)
    find_MaxMin(f,0,3)
def ex4():
    print("4.a")
    f = x**2 - 2*x - 5
    find_MaxMin(f,0,2)
    print("4.b")
    f = 3*x + x*3 + 5
    find_MaxMin(f,-4,4)

def ex5():
    f = lambda x: x**2
    min_x = golden_search(f, -2, 1, 0.3)
    print("The minimum value is at x =", min_x)
    plot_function(f, -2, 1, min_x)

def ex6():
    f = lambda x: x**2
    min_x = fibonacci_search(f, -2, 1, 0.3)
    print("The minimum value is at x =", min_x)
    plot_function(f, -2, 1, min_x)

def ex7():
    def find_m():
        x, m = sp.symbols('x m')
        y = x**3 - 3*m*x**2 + 3*(m**2 - 1)*x - (m**2 - 1)
        dy_dm = sp.diff(y, m)
        m_value = sp.solve(dy_dm.subs(x, 1), m)
        return m_value

    m_value = find_m()
    print("The value of m that maximizes the function at x0 = 1 is:", m_value)

def ex8():
    f1 = lambda x: -2*x**2 + x + 4
    f2 = lambda x: -4*x**2 + 2*x + 2
    f3 = lambda x: x**3 + 6*x**2 + 5*x - 12
    f4 = lambda x: 2*x - x**2

    optimize_and_plot(f1, [-5, 5], 1/9, 'f1(x) = -2x^2 + x + 4')
    optimize_and_plot(f2, [-6, 6], 1/10, 'f2(x) = -4x^2 + 2*x + 2')
    optimize_and_plot(f3, [-5, -2], 1/10, 'f3(x) = x^3 + 6x^2 + 5x - 12')
    optimize_and_plot(f4, [0, 3], 1/100, 'f4(x) = 2x - x^2')

    plt.legend()
    plt.show()


ex1()
ex2()
ex3()
ex4()
ex5()
ex6()
ex7()
ex8()