from math import cos, sin, radians
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def rotate_matrix_x(fi):
    fi = radians(fi)
    ma = [
        [1, 0, 0],
        [0, cos(fi), sin(fi)],
        [0, -sin(fi), cos(fi)]
    ]
    return ma


def rotate_matrix_y(fi):
    fi = radians(fi)
    ma = [
        [cos(fi), 0, -sin(fi)],
        [0, 1, 0],
        [sin(fi), 0, cos(fi)]
    ]
    return ma


def rotate_matrix_z(fi):
    fi = radians(fi)
    ma = [
        [cos(fi), sin(fi), 0],
        [-sin(fi), cos(fi), 0],
        [0, 0, 1]
    ]
    return ma


def stretching_compression_matrix(a, b, c):
    # a > 0 коэффициент сжатия (растяжения) вдоль оси абсцисс
    # b > 0 коэффициент сжатия (растяжения) вдоль оси ординат
    # c > 0 коэффициент сжатия (растяжения) вдоль оси аппликат

    ma = [
        [a, 0, 0],
        [0, b, 0],
        [0, 0, c]
    ]
    return ma


def reflection_x0y_matrix():
    ma = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, -1]
    ]
    return ma


def reflection_y0z_matrix():
    ma = [
        [-1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    return ma


def reflection_z0x_matrix():
    ma = [
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, 1]
    ]
    return ma


def matrix_mul(ma1, ma2):
    ma = []
    for i in range(3):
        sum = 0
        for j in range(3):
            sum += ma1[i][j] * ma2[j]
        ma.append(sum)
    return ma


def draw_all_plots(points_list):
    a = 2
    b = 2
    c = 2
    fi = 45
    xnew = 1
    ynew = 1
    znew = 1

    fig = plt.figure(figsize=plt.figaspect(0.5))
    fig = draw_figure(fig, points_list, 'cyan', 1, 'Figure')
    fig = draw_figure(fig, rotate_x(points_list, fi), 'green', 2, 'Rotate X')
    fig = draw_figure(fig, rotate_y(points_list, fi), 'green', 3, 'Rotate Y')
    fig = draw_figure(fig, rotate_z(points_list, fi), 'green', 4, 'Rotate Z')
    fig = draw_figure(fig, stretching_compression(points_list, a, b, c), 'yellow', 5, '\nStretching compression')
    fig = draw_figure(fig, reflection_x0y(points_list), 'brown', 6, 'Reflection XoY')
    fig = draw_figure(fig, reflection_y0z(points_list), 'brown', 7, 'Reflection YoZ')
    fig = draw_figure(fig, reflection_z0x(points_list), 'brown', 8, 'Reflection ZoX')
    fig = draw_figure(fig, transfer_x(points_list, xnew), 'hotpink', 9, 'Transfer X')
    fig = draw_figure(fig, transfer_y(points_list, ynew), 'hotpink', 10, 'Transfer Y')
    fig = draw_figure(fig, transfer_z(points_list, znew), 'hotpink', 11, 'Transfer Z')
    plt.show()


def draw_figure(fig, points, color, index, title):
    ax = fig.add_subplot(2, 6, index, projection='3d')
    ax.title.set_text(title)
    ax.set_xlim((-20, 20))
    ax.set_ylim((-20, 20))
    ax.set_zlim((-20, 20))
    v = [
        [points[0], points[1], points[2], points[3]],
        [points[0], points[4], points[1]],
        [points[0], points[4], points[3]],
        [points[3], points[4], points[2]],
        [points[2], points[4], points[1]]
    ]
    pc = Poly3DCollection(v, facecolors=color, edgecolors='black')
    ax.add_collection3d(pc)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    return fig

def calculate_new_points(points_list, ma):
    new_points_list = []
    for i in points_list:
        new_points_list.append(matrix_mul(ma, [i[0], i[1], i[2]]))
    print(new_points_list)
    return new_points_list


def rotate_x(points_list, fi):
    ma = rotate_matrix_x(fi)
    return calculate_new_points(points_list, ma)
    


def rotate_y(points_list ,fi):
    ma = rotate_matrix_y(fi)
    return calculate_new_points(points_list, ma)


def rotate_z(points_list, fi):
    ma = rotate_matrix_z(fi)
    return calculate_new_points(points_list, ma)


def reflection_x0y(points_list):
    ma = reflection_x0y_matrix()
    return calculate_new_points(points_list, ma)


def reflection_y0z(points_list):
    ma = reflection_y0z_matrix()
    return calculate_new_points(points_list, ma)


def reflection_z0x(points_list):
    ma = reflection_z0x_matrix()
    return calculate_new_points(points_list, ma)


def stretching_compression(points_list, a, b, c):
    ma = stretching_compression_matrix(a, b, c)
    return calculate_new_points(points_list, ma)


def transfer_x(points_list, xnew):
    for i in points_list:
        i[0] += xnew
    return points_list


def transfer_y(points_list, ynew):
    for i in points_list:
        i[1] += ynew
    return points_list


def transfer_z(points_list, znew):
    for i in points_list:
        i[2] += znew
    return points_list


def main():
    x1 = 1
    x2 = 7
    y1 = 1
    y2 = 7
    z1 = 1
    x = 3
    y = 3
    z = 9
    points_list = [
        [x1, y1, z1], [x1, y2, z1], [x2, y2, z1], [x2, y1, z1], [x, y, z]
    ]
    draw_all_plots(points_list)


if __name__ == '__main__':
    main()
