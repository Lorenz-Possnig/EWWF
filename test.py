from equation import Equation
from equation import quadraticEquation

if __name__ == '__main__':
    f = Equation(quadraticEquation(-2, 18, 44))
    z0 = f.zero(-100, 0)
    z1 = f.zero(0, 100)
    print([z0, z1])
    h = f.extreme(-10, 10)
    print(h)
    print(f.integrate(z0, z1))
    f = Equation(lambda x: 2 * (x ** 3) + 5 * (x * x) + 3 * x + 4)
    z = f.zero(-5, 5)
    print(z)