import time
import asyncio

async def greeting(message):
    for i in range(6):
        print(message)
        await asyncio.sleep(1)

start_time = time.time()

