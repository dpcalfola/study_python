"""
Goals of the code
    1. How to run async function
    2. How to check up elapsed time
"""

import asyncio
import sys
import time

from python_snippets.annotations.estimate_executation_time.estimate_time_1 import (
    estimate_time,
)  # Annotation for elapsed time


def sync_counter(sleep_time):
    """
    One with... -> Start to wait for {sleep_time} from now
    Two with... -> It has been over for {sleep_time}
    :param sleep_time:
    :return:
    """

    print(f"One with sleep_time {sleep_time}")
    time.sleep(sleep_time)
    print(f"Two with sleep time {sleep_time}")


def sync_main():
    """
    Call sync_counter Order by 2, 1, 3
    :return:
    """
    for num in (2, 1, 3):
        sync_counter(num)


async def async_counter(sleep_time):
    print(f"One with sleep_time {sleep_time}")
    await asyncio.sleep(sleep_time)
    print(f"Two with sleep_time {sleep_time}")


async def async_main():
    await asyncio.gather(*(async_counter(i) for i in (2, 1, 3)))

    # 🌟 Important point "await asyncio.gather(*(async_counter(i) for i in (2, 1, 3)))
    # Asterisk * -> Unpacking
    # -> async_counter(2), async_counter(1), async_counter(3)
    # await asyncio.gather(*[async_counter(2), async_counter(1), async_counter(3)])
    #
    # If there's no asterisk, generator expression would be passed as a single argument
    # -> Treated as a single argument


start_time: float = time.time()
asyncio.run(async_main())
end_time: float = time.time()
elapsed_time: float = end_time - start_time
print(f"async_main() Elapsed time: {elapsed_time}")

start_time: float = time.time()
sync_main()
end_time: float = time.time()
elapsed_time: float = end_time - start_time
print(f"sync_main() Elapsed time: {elapsed_time}")

#
# How to run async function

# 1. asyncio.run

# 2. asyncio.create_task
# example of asyncio.create_task
# async def main():
#     task = asyncio.create_task(async_main()())
#     await task
# asyncio.run(main())

# 3. asyncio.ensure_future
# example of asyncio.ensure_future
# async def main():
#     task = asyncio.ensure_future(async_main()())
#     await task
# asyncio.run(main())

# 4. asyncio.wait
# example of asyncio.wait
# async def main():
#     task = asyncio.wait(async_main()())
#     await task
# asyncio.run(main())

# 5. asyncio.gather
# example of asyncio.gather
# async def main():
#     task = asyncio.gather(async_main()())
#     await task
# asyncio.run(main())

# 6. asyncio.as_completed
# example of asyncio.as_completed
# async def main():
#     task = asyncio.as_completed(async_main()())
#     await task
# asyncio.run(main())

# 7. asyncio.to_thread
# example of asyncio.to_thread
# async def main():
#     task = asyncio.to_thread(async_main()())
#     await task
# asyncio.run(main())

# 8. asyncio.start_server
# example of asyncio.start_server
# async def main():
#     task = asyncio.start_server(async_main()())
#     await task
# asyncio.run(main())
