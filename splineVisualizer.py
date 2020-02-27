import matplotlib.pyplot as plt
import sys
import time
from networktables import NetworkTables
import inspect
import math
# To see messages from networktables, you must setup logging
import logging

logging.basicConfig(level=logging.DEBUG)
if len(sys.argv) != 2:
    print("Error: specify an IP to connect to!")
    exit(0)

ip = sys.argv[1]

NetworkTables.initialize(server=ip)

sd = NetworkTables.getTable("splines")

xs = sd.getValue("splineY"),

field_img = plt.imread("Field.png")

robotWidth = 0.3  # in meters


def getSides(xs, ys):
    # for i in range(len(xs)):
    angles = [math.atan2((ys[i+1] - ys[i]), (xs[i+1] - xs[i]))
              for i in range(len(xs) - 1)]
    print(angles)
    angles.append(0)
    bxs = [xs[i] + robotWidth * math.sin(angles[i]) for i in range(len(xs))]
    bys = [ys[i] + robotWidth * math.cos(angles[i]) for i in range(len(ys))]
    txs = [xs[i] - robotWidth * math.sin(angles[i]) for i in range(len(xs))]
    tys = [ys[i] - robotWidth * math.cos(angles[i]) for i in range(len(ys))]
    # for i in range(len(xs)):
    #     txs[i] = xs[i]

    return txs, tys, bxs, bys


print(xs)
while True:
    xs = sd.getNumberArray("splineX", [])
    ys = sd.getNumberArray("splineY", [])

    sxs = sd.getNumberArray("startX", [])
    sys = sd.getNumberArray("startY", [])

    if not len(xs) == 0:
        fig, ax = plt.subplots()
        ax.imshow(field_img, extent=(0, 16.48, 0, 8.1))

        plt.plot(xs, ys, '-')

        topX, topY, bottomX, bottomY = getSides(xs, ys)

        plt.plot(xs, ys, '-', c='#f39639')
        plt.plot(topX, topY, '--', c='#f39639')
        plt.plot(bottomX, bottomY, '--', c='#f39639')

        ax.scatter(sxs, sys, s=20, c='r')

        plt.show()
        break
