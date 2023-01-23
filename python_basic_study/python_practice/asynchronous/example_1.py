"""
Asynchronism: (n) 비동시성, 비동기성
Asynchronous: (a) 동시에 존재하는

"""

import asyncio


async def my_async_function():
    print("Starting my_async_function")
    await asyncio.sleep(3)
    print("my_async_function completed")


async def main():
    print("Starting main function")
    await my_async_function()
    print("main function completed")


asyncio.run(main())
