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
    await asyncio.gather(async_counter(i) for i in (2, 1, 3))


# Start check up performance


def get_run_code() -> int:
    guide_message: str = "1 - Execute sync_main()\n2 - Execute async_main()"
    error_message: str = "\nError: Input value should be integer 1 or 2"

    print(guide_message)

    while True:
        print("Enter the number 1 or 2:", end="")
        try:
            input_run_code: int = int(sys.stdin.readline().rstrip())
            if input_run_code in (1, 2):
                return input_run_code
            else:
                print(error_message)

        except ValueError:
            print(error_message)
            pass


run_code = get_run_code()
print(run_code)

# Execute sync or async main

# Debate wit chatGPT
# Q: Which case is better?. Previous code checked that {run_code} supposed to 1 or 2

# Case 1:
sync_main() if run_code == 1 else async_main()

# Case 2:
if run_code == 1:
    sync_main()
elif run_code == 2:
    async_main()
