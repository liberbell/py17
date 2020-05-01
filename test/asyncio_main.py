import asyncio
import time

async def greetings(message):
    for i in range(6):
        print(message)
        await asyncio.sleep(1)

async def main():
    start_time = time.time()

    # await greetings("Hello")
    # await greetings("World")

    task1 = asyncio.create_task(greetings("Hello"))
    task2 = asyncio.create_task(greetings("World"))

    await task1
    await task2

    end_time = time.time()

    print("Control returned to main")
    print("Total time: ", end_time - start_time)

asyncio.run(main())