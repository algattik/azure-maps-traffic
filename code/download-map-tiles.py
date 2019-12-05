import aiohttp
import asyncio
from settings import settings

zoom = settings.zoom


async def download():
    async with aiohttp.ClientSession() as session:
        for tileX in range(settings.leftTile, settings.rightTile+1):
            for tileY in range(settings.topTile, settings.bottomTile+1):
                url = ("https://atlas.microsoft.com/map/tile/png"
                       "?api-version=1.0"
                       f"&subscription-key={settings.subscriptionkey}"
                       "&layer=hybrid"
                       "&style=main"
                       f"&zoom={settings.zoom}"
                       f"&x={tileX}"
                       f"&y={tileY}"
                       )
                print(url)
                async with session.get(url) as resp:
                    print(resp.status)
                    resp.raise_for_status()
                    fileName = f"data/map.{tileX}.{tileY}.{zoom}.tile.png"
                    with open(fileName, "wb") as f:
                        f.write(await resp.read())

asyncio.run(download())
