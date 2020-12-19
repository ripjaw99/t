import asyncio
import aiohttp



async def plop(r):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.roblox.com/users/get-by-username?username=KaanAgent') as r:
            res = await r.json()
            print(res['Id'])
asyncio.run(plop('r'))



