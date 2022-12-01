import tkinter as tk
from math import cos, sin, degrees
import numpy as np


def rotate_matrix(fi, a, b):
    fi = degrees(fi)
    ma = [
        [cos(fi), sin(fi), 0],
        [-sin(fi), cos(fi), 0],
        [a*cos(fi)+b*sin(fi)+a, -a*cos(fi)-b*sin(fi)+b, 1]
    ]
    return ma


def scale_matrix(a, b):
    ma = [
        [a, 0, 0],
        [0, b, 0],
        [(1-a)*a, (1-b)*b, 1]
    ]
    return ma


def rotate(x1, x2, x3, x4, x0, y1, y2, y0, y, canvas):
    matr = rotate_matrix(10, x0, y0)
    x1new = np.matmul([x1, y1, 1], matr)
    x2new = np.matmul([x2, y1, 1], matr)
    x3new = np.matmul([x3, y2, 1], matr)
    x4new = np.matmul([x4, y2, 1], matr)
    x5new = np.matmul([x0, y, 1], matr)
    canvas.create_line(x1new[0], x1new[1], x2new[0], x2new[1], fill="Red")
    canvas.create_line(x1new[0], x1new[1], x3new[0], x3new[1], fill="Red")
    canvas.create_line(x3new[0], x3new[1], x4new[0], x4new[1], fill="Red")
    canvas.create_line(x4new[0], x4new[1], x2new[0], x2new[1], fill="Red")
    canvas.create_line(x1new[0], x1new[1], x5new[0], x5new[1], fill="Red")
    canvas.create_line(x2new[0], x2new[1], x5new[0], x5new[1], fill="Red")
    canvas.create_line(x3new[0], x3new[1], x5new[0], x5new[1], fill="Red")
    canvas.create_line(x4new[0], x4new[1], x5new[0], x5new[1], fill="Red")


def scale(x1, x2, x3, x4, x0, y1, y2, y0, y, canvas):
    matr = scale_matrix(0.25, 0.25)
    x1new = np.matmul([x1, y1, 1], matr)
    x2new = np.matmul([x2, y1, 1], matr)
    x3new = np.matmul([x3, y2, 1], matr)
    x4new = np.matmul([x4, y2, 1], matr)
    x5new = np.matmul([x0, y, 1], matr)
    canvas.create_line(x1new[0], x1new[1], x2new[0], x2new[1], fill="Red")
    canvas.create_line(x1new[0], x1new[1], x3new[0], x3new[1], fill="Red")
    canvas.create_line(x3new[0], x3new[1], x4new[0], x4new[1], fill="Red")
    canvas.create_line(x4new[0], x4new[1], x2new[0], x2new[1], fill="Red")
    canvas.create_line(x1new[0], x1new[1], x5new[0], x5new[1], fill="Red")
    canvas.create_line(x2new[0], x2new[1], x5new[0], x5new[1], fill="Red")
    canvas.create_line(x3new[0], x3new[1], x5new[0], x5new[1], fill="Red")
    canvas.create_line(x4new[0], x4new[1], x5new[0], x5new[1], fill="Red")


def main():
    x1 = 180
    y1 = 600
    x2 = 580
    x3 = 250
    y2 = 400
    x4 = 650
    x0 = (x1 + x4) / 2  # 415
    y0 = (y1+y2) / 2    # 500
    y = 100
    root = tk.Tk()
    root.title('LR1')
    root.geometry('1920x1080')
    canvas = tk.Canvas(root, bg='Green', width=1920, height=1080)
    canvas.create_line(x1, y1, x2, y1)
    canvas.create_line(x3, y2, x4, y2)
    canvas.create_line(x1, y1, x3, y2)
    canvas.create_line(x2, y1, x4, y2)
    canvas.create_line(x1, y1, x4, y2)
    canvas.create_line(x2, y1, x3, y2)
    canvas.create_line(x0, y0, x0, y)
    canvas.create_line(x1, y1, x0, y)
    canvas.create_line(x2, y1, x0, y)
    canvas.create_line(x4, y2, x0, y)
    canvas.create_line(x3, y2, x0, y)
    answer = input("1 - rotate, 2 - scale : ")
    if answer == '1':
        rotate(x1, x2, x3, x4, x0, y1, y2, y0, y, canvas)
    else:
        scale(x1, x2, x3, x4, x0, y1, y2, y0, y, canvas)

    canvas.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
