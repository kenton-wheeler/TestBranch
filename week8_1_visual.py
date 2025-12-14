import matplotlib.pyplot as plt

def draw_triangle():
    # plot a triangle that is green, has a solid line and triangle markers
    x = [3, 4, 5, 3]
    y = [4, 6, 4, 4]
    plt.plot(x, y, 'g-o')

def draw_rectangle():
    # plot a rectangle that is red, has a dotted line and square markers
    x = [3, 3, 5, 5, 3]
    y = [2, 3, 3, 2, 2]
    plt.plot(x, y, 'r:s')