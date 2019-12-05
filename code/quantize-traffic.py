from scipy.spatial import distance
import numpy as np
from settings import settings
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


def closest_node_pal(node):
    nodes = np.array([i[0] for i in node_palette])
    closest_index = distance.cdist([node], nodes).argmin()
    return node_palette[closest_index][2]*40


trafficImg = Image.open("data/stitched-traffic.png")
na = np.apply_along_axis(closest_node_pal, 2, np.array(trafficImg))
Image.fromarray(na.astype('uint8')).save("data/stitched-traffic-quantized.png", "PNG")
