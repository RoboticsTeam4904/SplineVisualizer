import numpy as np
import json

outfile = "straight.json"

output = {"x": [], "y": []}
for i in np.arange(0, 2, 0.001):
    output["y"].append(0)
    output["x"].append(i)

with open(outfile, "w+") as wf:
    wf.write(json.dumps(output))
