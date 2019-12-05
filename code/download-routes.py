import aiohttp
import asyncio
import random
from settings import settings


async def dlroutes():
    async with aiohttp.ClientSession() as session:
        for routenum in range(100):

            x1 = random.uniform(settings.bottom, settings.top)
            x2 = random.uniform(settings.bottom, settings.top)
            y1 = random.uniform(settings.left, settings.right)
            y2 = random.uniform(settings.left, settings.right)
            url = ("https://atlas.microsoft.com/route/directions/json"
                   "?api-version=1.0"
                   f"&subscription-key={settings.subscriptionkey}"
                   f"&query={x1},{y1}:{x2},{y2}"
                   "&traffic=true"
                   "&computeTravelTimeFor=all"
                   )
            print(url)
            async with session.get(url) as resp:
                print(resp.status)
                resp.raise_for_status()
                fileName = f"data/route.{routenum}.json"
                with open(fileName, "wb") as f:
                    f.write(await resp.read())


asyncio.run(dlroutes())
