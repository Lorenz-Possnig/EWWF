class Equation():

    function = None
    error = 0.0001
    integrate_N_times = 100

    def __init__(self, function, error=0.0001, integrate_N_times=100):
        """Init the class with a function and an error to be used by functions"""
        self.function = function
        self.error = error
        self.integrate_N_times = integrate_N_times

    def falsePosition(self, x0, x1):
        """
        Uses falsePositionMethod / Regula Falsi to find zero values
        :param x0: lower bound of interval that contains a zero value
        :param x1: upper bound of interval that contains a zero value
        :type x0: any number
        :type x1: any number
        :rtype: float
        :return: zero value of self.function between x0 and x1
        """
        f = self.function
        condition = True
        while condition:
            x2 = x0 - (x1 - x0) * f(x0) / ( f(x1) - f(x0) )

            if f(x0) * f(x2) < 0:
                x1 = x2
            else:
                x0 = x2
            
            condition = abs(f(x2)) > self.error
        return x2

    def zero(self, lower, upper):
        """
        Error check for self.falsePosition
        :param lower: x0 of self.falsePosition
        :param upper: x1 of self.falsePosition
        :type lower: any number
        :type upper: any number
        :rtype: float
        :returns: result of self.falsePosition
        :raises: ValueError
        """
        if self.function(lower) * self.function(upper) > 0.0:
            raise ValueError('Given values do not bracket the root')
        else:
            return self.falsePosition(lower, upper)

    def derivative(self, a):
        """
        Uses central difference formula to numerically approximate derivatives
        :param a: compute derivative at x = a
        :type a: any number
        :rtype: float
        :returns: the value of f'(x)
        """
        h = self.error
        f = self.function
        forward = ( f(a + h) - f(a) ) / h
        backward = ( f(a) - f(a - h) ) / h
        central = (forward + backward) / 2
        return central

    def derive(self):
        """
        Returns a new Equation with f'(x) as the function
        """
        func = lambda x: self.derivative(x)
        return Equation(func)

    def extreme(self, left, right):
        """
        Returns an extreme (minimum or maximum) value between left and right
        :param left: lower bound of interval
        :param right: upper bound of interval
        :type left: any number
        :type right: any number
        :rtype: float
        :returns: min or max value of a function in given interval
        :raises: ValueError
        """
        d = self.derive()
        z = d.zero(left, right)
        return self.function(z)

    def integrate(self, a, b):
        """
        Approximate Integration between f(a) and f(b) using Midpoint Rule
        :param a: lower bound of integration
        :param b: upper bound of integration
        :type a: any number
        :type b: any number
        :rtype: float
        """
        f = self.function
        value = 0
        value2 = 0
        for n in range(1, self.integrate_N_times + 1):
            value += f(a + ( (n-(1/2)) * ((b-a)/self.integrate_N_times) ))
        value2 = ((b-a)/self.integrate_N_times) * value
        return value2


def linearEquation(k, d):
    """
    Returns a first order function of type kx + d
    :param k: k
    :param d: d
    :type k: any number
    :type d: any number
    :rtype: function
    :returns: a first order function of type kx + d
    """
    return (lambda x: k * x + d)

def quadraticEquation(a, b, c):
    """
    Returns a second order function of tyoe ax² + bx + c
    :param a: a
    :param b: b
    :param c: c
    :type a: any number
    :type b: any number
    :type c: any number
    :rtype: function
    :returns: a second order function of tyoe ax² + bx + c
    """
    return (lambda x: a * (x * x) + b * x + c)
