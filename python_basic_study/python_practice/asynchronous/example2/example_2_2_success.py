"""
* Synchronous:
Basically means that
you can execute one thing at a time.

* Asynchronous:
Means that you can execute multiple things at a time
And you don't have to finish executing the current thing
in order to move on to next one.

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


@estimate_time
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


@estimate_time
async def async_main():
    await asyncio.gather(*(async_counter(i) for i in (2, 1, 3)))

    # 🌟 Important point
    # Asterisk * -> Unpacking
    # -> async_counter(2), async_counter(1), async_counter(3)
    # await asyncio.gather(*[async_counter(2), async_counter(1), async_counter(3)])
    #
    # If there's no asterisk, generator expression would be passed as a single argument
    # -> Treated as a single argument


# Get the command number to execute sync_main(), async_main() or exit the code
def get_run_code() -> int:
    guide_message: str = (
        "1 - Execute sync_main()\n2 - Execute async_main()\n3 - Exit the code"
    )
    error_message: str = "\nError: Input value should be integer 1 to 4"
    print(guide_message)

    while True:
        print("Enter the command number:", end="")
        try:
            input_run_code: int = int(sys.stdin.readline().rstrip())
            if input_run_code in (1, 2, 3):
                return input_run_code
            else:
                print(error_message)

        except ValueError:
            print(error_message)
            pass


# Execute sync or async main or exit the code
while True:
    run_code = get_run_code()
    print()
    if run_code == 1:
        print("Execute sync_main()")
        sync_main()
    elif run_code == 2:
        print("Execute asyncio.run(async_main())")
        start_time: float = time.time()
        asyncio.run(async_main())
        end_time: float = time.time()
        elapsed_time: float = end_time - start_time
        print(
            f"async_main() Elapsed time: {elapsed_time} -> The time to pass every time.sleep()"
        )
    elif run_code == 3:
        print("Code execution is finished")
        break
    print()
