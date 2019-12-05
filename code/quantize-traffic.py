from scipy.spatial import distance
import numpy as np
from PIL import Image

node_palette = [
    ([0, 0, 0], "black", 0),
    ([255, 255, 255], "white", 0),
    ([119, 119, 119], "gray", 0),
    ([43, 200, 43], "green", 1),
    ([255, 242, 54], "yellow", 2),
    ([255, 222, 52], "orange", 3),
    ([255, 203, 50], "darkorange", 4),
    ([255, 153, 46], "amber", 5),
    ([255, 112, 42], "red", 6),
]
nodes = np.array([i[0] for i in node_palette])


def closest_node_pal(node):
    if [node] == [255, 255, 255, 0]:
        intensity_level = 0  # white
    else:
        closest_index = distance.cdist([node[0:3]], nodes).argmin()
        intensity_level = node_palette[closest_index][2]
    return intensity_level * 40


trafficImg = Image.open("data/stitched-traffic.png")
na = np.apply_along_axis(closest_node_pal, 2, np.array(trafficImg))
Image.fromarray(na.astype('uint8')).save(
  "data/stitched-traffic-quantized.png", "PNG")
