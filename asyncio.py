# import asyncio

# # def main():
# #     print("Hello")

# # main()

# async def main():
#     print("Hello")

# # func = main()
# # print(type(func))

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

# loop.close()

import asyncio

async def main():
    print("Hello")
    
# loop = asyncio.get_event_loop()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()