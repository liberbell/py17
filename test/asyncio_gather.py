import asyncio
import time

async def greetings(message):
    for i in range(6):
        print(message)
        await asyncio.sleep(1)

async def print_numbers(num):
    for i in range(num):
        print(i)
        await asyncio.sleep(1)