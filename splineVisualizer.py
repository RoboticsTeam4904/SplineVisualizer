import matplotlib.pyplot as plt
import sys
import time
# from networktables import NetworkTables
import inspect
import json

import math
# To see messages from networktables, you must setup logging
import logging

# logging.basicConfig(level=logging.DEBUG)
# if len(sys.argv) != 2:
#     print("Error: specify an IP to connect to!")
#     exit(0)

# ip = sys.argv[1]
data = None
file_name = "networktable-numbers/left_turn.json"
with open(file_name, "r") as rf:

    data = json.loads(rf.read())

# NetworkTables.initialize(server=ip)


# sd = NetworkTables.getTable("splines")

# print(inspect.getmembers(sd, predicate=inspect.ismethod))

# xs = sd.getValue("splineY"),

field_img = plt.imread("Field.png")

# print(xs)
# xs = sd.getValue("splineY"),

field_img = plt.imread("Field.png")

robotWidth = 0.3  # in meters


# def getSides(xs, ys):
#     # for i in range(len(xs)):
#     angles = [math.atan2((ys[i+1] - ys[i]), (xs[i+1] - xs[i]))
#               for i in range(len(xs) - 1)]
#     print(angles)
#     angles.append(0)
#     bxs = [xs[i] - robotWidth * math.sin(angles[i] + 90)
#            for i in range(len(xs))]
#     bys = [ys[i] - robotWidth * math.cos(angles[i] + 90)
#            for i in range(len(ys))]
#     txs = [xs[i] - robotWidth * math.sin(angles[i] - 90)
#            for i in range(len(xs))]
#     tys = [ys[i] - robotWidth * math.cos(angles[i] - 90)
#            for i in range(len(ys))]
#     # for i in range(len(xs)):
#     #     txs[i] = xs[i]

def offset(xs, ys, distance):
    xsi = iter(xs)
    ysi = iter(ys)
    x1 = xs[0]
    y1 = ys[0]
    z = distance
    points = []
    rxs = []
    rys = []
    for i in range(len(xs)):
        x2 = xs[i]
        y2 = ys[i]
        # tangential slope approximation
        try:
            slope = (y2 - y1) / (x2 - x1)
            # perpendicular slope
            # (might be 1/slope depending on direction of travel)
            pslope = -1/slope
        except ZeroDivisionError:
            continue
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2

        sign = ((pslope > 0) == (x1 > x2)) * 2 - 1

        # if z is the distance to your parallel curve,
        # then your delta-x and delta-y calculations are:
        #   z**2 = x**2 + y**2
        #   y = pslope * x
        #   z**2 = x**2 + (pslope * x)**2
        #   z**2 = x**2 + pslope**2 * x**2
        #   z**2 = (1 + pslope**2) * x**2
        #   z**2 / (1 + pslope**2) = x**2
        #   z / (1 + pslope**2)**0.5 = x

        delta_x = sign * z / ((1 + pslope**2)**0.5)
        delta_y = pslope * delta_x

        points.append((mid_x + delta_x, mid_y + delta_y))
        rxs.append(mid_x + delta_x)
        rys.append(mid_y + delta_y)
        x1, y1 = x2, y2
    return rxs, rys


# print(xs)
while True:
    # xs = sd.getNumberArray("splineX", [])
    xs = data["x"]
    # ys = sd.getNumberArray("splineY", [])
    ys = data["y"]

    # sxs = sd.getNumberArray("startX", [])
    # sys = sd.getNumberArray("startY", [])

    if not len(xs) == 0:
        fig, ax = plt.subplots()
        ax.imshow(field_img, extent=(0, 16.48, 0, 8.1))

        plt.plot(xs, ys, '-')

        # ax.scatter(sxs, sys, s=20, c='r')
        topX, topY = offset(xs, ys, robotWidth)
        bottomX, bottomY = offset(xs, ys, -robotWidth)

        plt.plot(xs, ys, '-', c='#f39639')
        plt.plot(topX, topY, '--', c='#f39639')
        plt.plot(bottomX, bottomY, '--', c='#f39639')

        # ax.scatter(sxs, sys, s=20, c='r')

        plt.show()
        break
