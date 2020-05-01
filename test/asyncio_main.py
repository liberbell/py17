import asyncio
import time

async def greetings(message):
    for i in range(6):
        print(message)
        await asyncio.sleep(1)

async def main():
    start_time = time.time()