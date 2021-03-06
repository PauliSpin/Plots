"""
Solves the parabolic equation
      2
    ax + bx + c = 0

    Roots are classified as Linear (a = 0), equal, real or complex.

"""
import math


def sgn(n):
    ''' Return a '+' or a '-' based on the sign of n '''
    if n >= 0:
        return '+'
    else:
        return '-'


class Parabola(object):

    ''' Class to define a parabola based on its coefficients and calculate its roots '''

    def __init__(self, a, b, c):
        ''' Set a, b, c and d (discriminant) for the class '''
        self.a = a              # Coefficient of x2
        self.b = b              # Coefficient of x
        self.c = c              # Constant
        self.d = b*b - 4*a*c    # Discriminant

    def y(self, x):
        ''' returns the y value of the Parabola at x '''
        return self.a*x*x + self.b*x + self.c

    @property
    def root1(self):
        ''' Calculate the first root '''
        if self.a == 0:
            return -self.c/self.b
        else:
            if self.d == 0:
                return (-self.b/(2*self.a))
            elif self.d > 0:
                return (-self.b - math.sqrt(self.d)) / (2*self.a)
            else:
                return complex(-self.b/(2*self.a), (math.sqrt(-self.d))/(2*self.a))

    @property
    def root2(self):
        ''' Calculate the second root '''
        if self.a == 0:
            return -self.c/self.b
        else:
            if self.d == 0:
                return (-self.b/(2*self.a))
            elif self.d > 0:
                return (-self.b + math.sqrt(self.d)) / (2*self.a)
            else:
                return complex(-self.b/(2*self.a), -(math.sqrt(-self.d))/(2*self.a))

    @property
    def root_type(self):
        ''' Return string to describe the type of roots for this class '''
        if self.a == 0:
            return "Linear"

        if self.d == 0:
            return "Equal"
        elif self.d > 0:
            return "Real"
        else:
            return "Complex"

    @property
    def turning_point(self):
        ''' calculate the turning point (maximum or minimum) position as (x, y) '''
        if self.d > 0:
            x = -self.b/(2*self.a)
            y = self.a*x*x + self.b*x + self.c
            return (x, y)

    def __str__(self):
        ''' Create a string to describe this class '''
        if self.a == 0:
            if self.b == 1:
                return f'x {sgn(self.c)} {abs(self.c)} = 0'
            else:
                return f'{self.b}x {sgn(self.c)} {abs(self.c)} = 0'
        else:
            if self.a == 1:
                return f'x2 + {self.b}x + {self.c} = 0'
            else:
                return f'{self.a}x2 + {self.b}x + {self.c} = 0'


def main():
    p_linear = Parabola(0, 1, -1)
    p_equal = Parabola(1, -6, 9)
    p_real = Parabola(1, -7, 10)
    p_complex = Parabola(3, -6, 4)

    print(p_linear)
    print(f'Root is {p_linear.root_type}')
    print(f'\troot = {p_linear.root1}')
    print()

    print(p_equal)
    print(f'Roots are {p_equal.root_type}')
    print(f'\troot  = {p_equal.root1}')
    print()

    print(p_real)
    print(f'Roots are {p_real.root_type}')
    print(f'\troot1 = {p_real.root1}')
    print(f'\troot2 = {p_real.root2}')
    print()

    print(p_complex)
    print(f'Roots are {p_complex.root_type}')
    print(f'\troot1 = {p_complex.root1}')
    print(f'\troot2 = {p_complex.root2}')
    print()


if __name__ == '__main__':
    main()
