import asyncio
import aiohttp

async def fruit(session, url):
    async with session.get(url) as response:
        print(f"Received response for {url}: {response.status}")
        
async def main():
    urls = ["https://httpbin.org/delay/2"] * 5
    
    async with aiohttp.ClientSession() as session:
        tasks = [fruit(session, url) for url in urls]
        await asyncio.gather(*tasks)
        
asyncio.run(main())

