import matplotlib.pyplot as plt
import sys
import time
# from networktables import NetworkTables
import inspect

# To see messages from networktables, you must setup logging
import logging

logging.basicConfig(level=logging.DEBUG)
if len(sys.argv) != 2:
    print("Error: specify an IP to connect to!")
    exit(0)

ip = sys.argv[1]

# NetworkTables.initialize(server=ip)

# sd = NetworkTables.getTable("splines")

print(inspect.getmembers(sd, predicate=inspect.ismethod))

xs = sd.getValue("splineY"),

field_img = plt.imread("Field.png")

print(xs)
while True:
    xs = sd.getNumberArray("splineX", [])
    ys = sd.getNumberArray("splineY", [])

    sxs = sd.getNumberArray("startX", [])
    sys = sd.getNumberArray("startY", [])

    print("————————————————————————————————————————————————————————————————————————————")

    print(xs)
    print(ys)

    print("————————————————————————————————————————————————————————————————————————————")

    if not len(xs) == 0:
        fig, ax = plt.subplots()
        ax.imshow(field_img, extent=(0, 16.48, 0, 8.1))

        plt.plot(xs, ys, '-')

        ax.scatter(sxs, sys, s=20, c='r')

        plt.show()
        break
