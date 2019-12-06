import aiohttp
import asyncio
import random
import itertools
from settings import settings

total = itertools.count()
failures = itertools.count()


async def dlroutes():
    global total, failures
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
            next(total)
            try:
                async with session.get(url) as resp:
                    resp.raise_for_status()
                    fileName = f"data/route.{routenum}.json"
                    with open(fileName, "wb") as f:
                        f.write(await resp.read())
            except Exception as e:
                print(e)
                next(failures)


asyncio.run(dlroutes())

totalCount = next(total)
failureCount = next(failures)
print(f"Total: {totalCount} Failed: {failureCount}")
assert 1. * failureCount / totalCount < 0.1
