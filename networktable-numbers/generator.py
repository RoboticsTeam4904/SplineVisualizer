import numpy as np
import json

x_offset = 4
y_offset = 4

def generate_straight(x: float) -> float:
    return 0;

def generate_right_turn(x: float) -> float:
    return np.log(x/5.0)/5.0 +1

paths = {"straight": generate_straight, "right_turn": generate_right_turn}

for path in paths:
    output = {"x": [], "y": []}
    for i in np.arange(0.01, 2, 0.001):
        output["x"].append(i + x_offset)
        output["y"].append(paths[path](i) + y_offset)

    with open(path + ".json", "w+") as wf:
        wf.write(json.dumps(output))
