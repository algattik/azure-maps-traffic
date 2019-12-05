import os
from maputils import PositionToTileXY
from typing import NamedTuple

box = "51.5458709,-0.2258784/51.439161,-0.0196732"  # London
#box = "48.9225438,2.2172182/48.7919087,2.446609"  # Paris
#box = "40.8552213,-74.092324/40.6380784,-73.8943915"  # NYC

p1 = [i.split(",") for i in box.split("/")]
bottom = min([float(i[0]) for i in p1])
top = max([float(i[0]) for i in p1])
left = min([float(i[1]) for i in p1])
right = max([float(i[1]) for i in p1])

zoom = 13
tileSize = 256

topLeftTile = PositionToTileXY((left, top), zoom, tileSize)
bottomRightTile = PositionToTileXY((right, bottom), zoom, tileSize)

assert bottomRightTile[0] - topLeftTile[0] >= 0
assert bottomRightTile[1] - topLeftTile[1] >= 0
assert bottomRightTile[0] - topLeftTile[0] < 10
assert bottomRightTile[1] - topLeftTile[1] < 10


class Settings(NamedTuple):
    bottom: float
    top: float
    right: float
    left: float
    zoom: int
    tileSize: int
    bottomTile: int
    topTile: int
    rightTile: int
    leftTile: int
    subscriptionkey: str


settings = Settings(
    bottom=bottom,
    top=top,
    right=right,
    left=left,
    zoom=zoom,
    tileSize=tileSize,
    bottomTile=bottomRightTile[1],
    topTile=topLeftTile[1],
    leftTile=topLeftTile[0],
    rightTile=bottomRightTile[0],
    subscriptionkey=os.environ["MAPS_KEY"],
)
