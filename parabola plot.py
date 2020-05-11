import parabola as prb
from matplotlib import pyplot as plt

# help(parabola)


def main():

    # Define parabola with real roots
    p_real = prb.Parabola(1, -7, 10)
    print(p_real)
    print(f'Roots are {p_real.root_type}')
    print(f'\troot1 = {p_real.root1}')
    print(f'\troot2 = {p_real.root2}')
    print()

    # Define number of points to be plotted
    N = 200
    # Set the x-distance between the two roots
    dist_root1_root2 = abs(p_real.root2 - p_real.root1)
    # Define the x-lower and x-upper limits to be a multiple of the
    # distance between the roots
    x_lower = p_real.root1 - 2 * dist_root1_root2
    x_upper = p_real.root2 + 2 * dist_root1_root2

    step = (x_upper - x_lower) / N

    x = []
    y = []

    for i in range(0, N):
        x.append(x_lower + i * step)
        y.append(p_real.y(x_lower + i * step))

    # print(x)
    # print(y)

    # Set the plot style
    plt.style.use('fivethirtyeight')

    # Set plot title, x and y labels
    plt.title(p_real)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, y, label='y(x)', linewidth=1)
    plt.tight_layout()

    plt.show()


if __name__ == '__main__':
    main()
