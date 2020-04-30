import time
import asyncio

async def greetings(message):
    for i in range(6):
        print(message)
        await asyncio.sleep(1)

start_time = time.time()

asyncio.run(greetings("Hello"))
asyncio.run(greetings("World"))