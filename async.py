import asyncio

async def fruit():
    print("I am a fruit")
    await asyncio.sleep(5)
    print("I am still a fruit")
    
async def main():
    print("I am a person")
    await asyncio.sleep(5)
    print("I am still a person")
    


    
asyncio.gather(main(), fruit())