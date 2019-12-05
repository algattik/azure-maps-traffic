from PIL import Image
from settings import settings


def stitch_image(type):
    new_im = Image.new('RGBA', (
        (settings.rightTile - settings.leftTile + 1) * settings.tileSize,
        (settings.bottomTile - settings.topTile + 1) * settings.tileSize,
    ), (255, 255, 255, 0))

    for tileX in range(settings.leftTile, settings.rightTile+1):
        for tileY in range(settings.topTile, settings.bottomTile+1):
            trafficImg = Image.open(
                f"data/map.{tileX}.{tileY}.{settings.zoom}.{type}.png")
            new_im.paste(trafficImg, (
                (tileX-settings.leftTile)*settings.tileSize,
                (tileY-settings.topTile)*settings.tileSize,
            ), trafficImg)

    new_im.save(f"data/stitched-{type}.png", "PNG")


stitch_image("tile")
stitch_image("traffic")
