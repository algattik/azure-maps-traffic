from PIL import Image, ImageDraw
from settings import settings
from maputils import PositionToGlobalPixel
import json
import glob


def PointToTile(p):
    globalPix = PositionToGlobalPixel(
        (p["longitude"], p["latitude"]),
        settings.zoom, settings.tileSize)
    tileXpix = int(globalPix[0] - (settings.leftTile * settings.tileSize))
    tileYpix = int(globalPix[1] - (settings.topTile * settings.tileSize))
    return (tileXpix, tileYpix)


def drawRoutes():
    im = Image.open("data/stitched-tile.png")
    routeFiles = glob.glob("data/route.*.json")
    for routeFile in routeFiles:
        im = drawRoute(im, routeFile)
    im.save("data/routes.png", "PNG")


def drawRoute(im, routeFile):

    # make a blank image for the route, initialized to transparent text color
    canvas = Image.new('RGBA', im.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(canvas)

    with open(routeFile) as inJson:
        routeDict = json.load(inJson)

    for route in routeDict["routes"]:

        for leg in route["legs"]:
            points = leg["points"]

            for p1, p2 in zip(points, points[1:]):
                tilepos1 = PointToTile(p1)
                tilepos2 = PointToTile(p2)
                draw.line([tilepos1, tilepos2], fill=(0, 255, 0, 20), width=10)

    # merge route image with background
    return Image.alpha_composite(im, canvas)


drawRoutes()
