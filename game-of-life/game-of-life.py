import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 255
OFF = 0
vals = [ON, OFF]


def wrapping(frame_num, img, grid, n):
    """board wrapping"""
    new_grid = grid.copy()
    for i in range(n):
        for j in range(n):
            total = int((grid[i, (j-1)%n] + grid[i, (j+1)%n] +
                         grid[(i-1)%n, j] + grid[(i+1)%n, j] +
                         grid[(i-1)%n, (j-1)%n] + grid[(i-1)%n, (j+1)%n] +
                         grid[(i+1)%n, (j-1)%n] + grid[(i+1)%n, (j+1)%n])/255)
            # Conway's rules
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    new_grid[i, j] = OFF
            else:
                if total == 3:
                    new_grid[i, j] = ON
    # data actualization
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,


def random_grid(n):
    """Returns board N x N of random values"""
    return np.random.choice(vals, n*n, p=[0.2, 0.8]).reshape(n, n)


def glider(i, j, grid):
    glider = np.array([[0, 0, 255],
                      [255, 0, 255],
                      [0, 255, 255]])
    grid[i:i+3, j:j+3] = glider


def die_hard(i, j, grid):
    die_hard = np.array([[0, 0, 0, 0, 0, 0, 255, 0],
                         [255, 255, 0, 0, 0, 0, 0, 0],
                         [0, 255, 0, 0, 0, 255, 255, 255]])
    grid[i:i+3, j:j+8] = die_hard


def gosper_glider_gun(i, j, grid):
    gosper_glider_gun = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0,
                                   0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 255, 0, 0,
                                   0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 0, 0, 0, 0, 0, 0, 255, 255, 0, 0, 0, 0,
                                   0, 0, 0, 0, 0, 0, 0, 0, 255, 255],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 255, 0, 0, 0, 0, 255, 255, 0, 0, 0, 0,
                                   0, 0, 0, 0, 0, 0, 0, 0, 255, 255],
                                  [255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 255, 0, 0, 0, 255, 255, 0, 0,
                                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 255, 0, 255, 255, 0, 0, 0, 0, 255, 0,
                                   255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 255, 0,
                                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                   0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                   0, 0, 0, 0, 0, 0, 0, 0, 0]])
    grid[i:i+9, j:j+36] = gosper_glider_gun


def infinite_5(i, j, grid):
    infinite_5 = np.array([[255, 255, 255, 0, 255],
                           [255, 0, 0, 0, 0],
                           [0, 0, 0, 255, 255],
                           [0, 255, 255, 0, 255],
                           [255, 0, 255, 0, 255]])
    grid[i:i+5, j:j+5] = infinite_5


def pulsar(i, j, grid):
    pulsar = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 255, 255, 255, 0, 0, 0, 255, 255, 255, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 255, 0, 0, 0, 0, 255, 0, 255, 0, 0, 0, 0, 255, 0],
                       [0, 255, 0, 0, 0, 0, 255, 0, 255, 0, 0, 0, 0, 255, 0],
                       [0, 255, 0, 0, 0, 0, 255, 0, 255, 0, 0, 0, 0, 255, 0],
                       [0, 0, 0, 255, 255, 255, 0, 0, 0, 255, 255, 255, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 255, 255, 255, 0, 0, 0, 255, 255, 255, 0, 0, 0],
                       [0, 255, 0, 0, 0, 0, 255, 0, 255, 0, 0, 0, 0, 255, 0],
                       [0, 255, 0, 0, 0, 0, 255, 0, 255, 0, 0, 0, 0, 255, 0],
                       [0, 255, 0, 0, 0, 0, 255, 0, 255, 0, 0, 0, 0, 255, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 255, 255, 255, 0, 0, 0, 255, 255, 255, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    grid[i:i+15, j:j+15] = pulsar


def main():
    parser = argparse.ArgumentParser(description="Initializing Conway's Game of Life simulation.")
    parser.add_argument('--grid-size', dest='n', required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--glider', action='store_true', required=False)
    parser.add_argument('--gosper', action='store_true', required=False)
    parser.add_argument('--diehard', action='store_true', required=False)
    parser.add_argument('--infinite5', action='store_true', required=False)
    parser.add_argument('--pulsar', action='store_true', required=False)
    args = parser.parse_args()

    # setting board size
    n = 100
    if args.n and int(args.n) > 8:
        n = int(args.n)

    # setting animation's update interval
    update_interval = 1
    if args.interval:
        update_interval = int(args.interval)

    # board declaration
    grid = np.array([])
    # checks, if any demo flag is set
    if args.glider:
        grid = np.zeros(n*n).reshape(n, n)
        glider(1, 1, grid)
    elif args.gosper:
        grid = np.zeros(n*n).reshape(n, n)
        gosper_glider_gun(0, 0, grid)
    elif args.diehard:
        grid = np.zeros(n*n).reshape(n, n)
        die_hard(10, 15, grid)
    elif args.infinite5:
        grid = np.zeros(n*n).reshape(n, n)
        infinite_5(20, 20, grid)
    elif args.pulsar:
        grid = np.zeros(n*n).reshape(n, n)
        pulsar(1,1,grid)
    else:
        # filling board with random grids
        grid = random_grid(n)

    # configures animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, wrapping, fargs=(img, grid, n, ),
                                  frames=10,
                                  interval=update_interval,
                                  save_count=50)
    if args.movfile:
        ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])

    plt.show()


if __name__ == '__main__':
    main()
