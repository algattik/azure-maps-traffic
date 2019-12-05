# Adapted from TypeScript code at
# https://docs.microsoft.com/en-gb/azure/azure-maps/zoom-levels-and-tile-grid
import math

EarthRadius = 6378137

MinLatitude = -85.05112878
MaxLatitude = 85.05112878
MinLongitude = -180
MaxLongitude = 180


def PositionToTileXY(position, zoom, tileSize):
    latitude = Clip(position[1], MinLatitude, MaxLatitude)
    longitude = Clip(position[0], MinLongitude, MaxLongitude)

    x = (longitude + 180) / 360
    sinLatitude = math.sin(latitude * math.pi / 180)
    y = 0.5 - math.log((1 + sinLatitude) / (1 - sinLatitude)) / (4 * math.pi)

    mapSize = MapSize(zoom, tileSize)

    return (
        math.floor(Clip(x * mapSize + 0.5, 0, mapSize - 1) / tileSize),
        math.floor(Clip(y * mapSize + 0.5, 0, mapSize - 1) / tileSize)
    )


def Clip(n, minValue, maxValue):
    return min(max(n, minValue), maxValue)


def MapSize(zoom, tileSize):
    return math.ceil(tileSize * math.pow(2, zoom))


def PositionToGlobalPixel(position, zoom, tileSize):
    latitude = Clip(position[1], MinLatitude, MaxLatitude)
    longitude = Clip(position[0], MinLongitude, MaxLongitude)

    x = (longitude + 180) / 360
    sinLatitude = math.sin(latitude * math.pi / 180)
    y = 0.5 - math.log((1 + sinLatitude) / (1 - sinLatitude)) / (4 * math.pi)

    mapSize = MapSize(zoom, tileSize)

    return (
        Clip(x * mapSize + 0.5, 0, mapSize - 1),
        Clip(y * mapSize + 0.5, 0, mapSize - 1)
    )
