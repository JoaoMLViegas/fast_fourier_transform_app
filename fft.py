import numpy as np
import math

F_one = np.array([[1, 1],
                  [1, -1]])

F_two = np.array([[1, 1, 1, 1],
                  [1, -1, 1j, -1j],
                  [1, 1, -1, -1],
                  [1, -1, -1j, 1j]])

D_one = np.array([[1, 0],
                  [0, 1j]])

D_two = np.array([[1, 0, 0, 0],
                  [0, complex(math.sqrt(2)/2, math.sqrt(2)/2), 0, 0],
                  [0, 0, 1j, 0],
                  [0, 0, 0, complex(-math.sqrt(2)/2, math.sqrt(2)/2)]])


def switch(poly, i, j):
    temp = poly[i]
    poly[i] = poly[j]
    poly[j] = temp
    return poly


def rev2(poly):
    switch(poly, 1, 2)
    return poly


def rev3(poly):
    switch(poly, 1, 4)
    switch(poly, 3, 6)
    return poly


def degree_of_poly(poly):
    j = 0
    for i in range(len(poly)):
        if poly[i] != 0:
            j = i
    return j


def dft_4(poly):
    poly = rev2(poly)
    part1 = poly[0:2]
    part2 = poly[2:4]
    part1 = F_one @ part1
    part2 = F_one @ part2
    part2 = D_one @ part2
    upper = part1 + part2
    lower = part1 - part2
    return np.concatenate((upper, lower))


def main_fft_4(poly1, poly2):
    poly1 = dft_4(poly1)
    poly2 = dft_4(poly2)

    poly1 = poly1 * poly2
    poly1 = np.conjugate(poly1)
    poly1 = dft_4(poly1)
    poly1 = np.conjugate(poly1)
    return poly1 / 4


def main_fft_8(poly1, poly2):
    return 0, 0, 0, 0, 0


def polinomial_multiplication(poly1, poly2):
    degree1 = degree_of_poly(poly1)
    degree2 = degree_of_poly(poly2)

    if degree1 + degree2 + 1 <= 4:
        answer = main_fft_4(poly1, poly2)
    else:
        answer = main_fft_8(poly1, poly2)

    return [float(x.real) for x in answer]
