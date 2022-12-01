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


def draw_figure(points, color):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
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
    pc = Poly3DCollection(v, facecolors='green', edgecolors='r')
    ax.add_collection3d(pc)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()


def rotate_x(points_list, fi):
    new_points_list = []
    ma = rotate_matrix_x(fi=fi)
    for i in points_list:
        new_points_list.append(matrix_mul(ma, [i[0], i[1], i[2]]))
    print(new_points_list)
    return new_points_list


def rotate_y(points_list ,fi):
    new_points_list = []
    ma = rotate_matrix_y(fi=fi)
    for i in points_list:
        new_points_list.append(matrix_mul(ma, [i[0], i[1], i[2]]))
    print(new_points_list)
    return new_points_list


def rotate_z(points_list, fi):
    new_points_list = []
    ma = rotate_matrix_z(fi=fi)
    for i in points_list:
        new_points_list.append(matrix_mul(ma, [i[0], i[1], i[2]]))
    print(new_points_list)
    return new_points_list


def reflection_x0y(points_list):
    new_points_list = []
    ma = reflection_x0y_matrix()
    for i in points_list:
        new_points_list.append(matrix_mul(ma, [i[0], i[1], i[2]]))
    print(new_points_list)
    return new_points_list


def reflection_y0z(points_list):
    new_points_list = []
    ma = reflection_y0z_matrix()
    for i in points_list:
        new_points_list.append(matrix_mul(ma, [i[0], i[1], i[2]]))
    return new_points_list


def reflection_z0x(points_list):
    new_points_list = []
    ma = reflection_z0x_matrix()
    for i in points_list:
        new_points_list.append(matrix_mul(ma, [i[0], i[1], i[2]]))
    return new_points_list


def stretching_compression(points_list, a, b, c):
    new_points_list = []
    ma = stretching_compression_matrix(a, b, c)
    for i in points_list:
        new_points_list.append(matrix_mul(ma, [i[0], i[1], i[2]]))
    print(new_points_list)
    return new_points_list


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
    a = 2
    b = 2
    c = 2
    fi = 45
    xnew = 1
    ynew = 1
    znew = 1
    points_list = [
        [x1, y1, z1], [x1, y2, z1], [x2, y2, z1], [x2, y1, z1], [x, y, z]
    ]
    draw_figure(points_list, 'cyan')
    draw_figure(rotate_x(points_list, fi), 'green')
    draw_figure(rotate_y(points_list, fi), 'green')
    draw_figure(rotate_z(points_list, fi), 'green')
    draw_figure(stretching_compression(points_list, a, b, c), 'green')
    draw_figure(reflection_x0y(points_list), 'green')
    draw_figure(reflection_y0z(points_list), 'green')
    draw_figure(reflection_z0x(points_list), 'green')
    draw_figure(transfer_x(points_list, xnew), 'green')
    draw_figure(transfer_y(points_list, ynew), 'green')
    draw_figure(transfer_z(points_list, znew), 'green')


if __name__ == '__main__':
    main()
