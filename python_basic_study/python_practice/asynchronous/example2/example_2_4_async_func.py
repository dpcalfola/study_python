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

from python_snippets.annotations.estimate_executation_time.estimate_time_1 import \
    estimate_time  # Annotation for elapsed time


def sync_counter(sleep_time):
    """
    One with... -> Start to wait for {sleep_time} from now
    Two with... -> It has been over for {sleep_time}
    :param sleep_time:
    :return:
    """

    print(f'One with sleep_time {sleep_time}')
    time.sleep(sleep_time)
    print(f'Two with sleep time {sleep_time}')


@estimate_time
def sync_main():
    """
    Call sync_counter Order by 2, 1, 3
    :return:
    """
    for num in (2, 1, 3):
        sync_counter(num)


async def async_counter(sleep_time):
    print(f'One with sleep_time {sleep_time}')
    await asyncio.sleep(sleep_time)
    print(f'Two with sleep_time {sleep_time}')


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


async def double_main():
    await asyncio.gather(async_main(), async_main())


print('Execute Method : run twice asyncio.run(async_main())')
start_time: float = time.time()
double_main()
end_time: float = time.time()
elapsed_time: float = end_time - start_time
print(f'Twice async_main() elapsed time: {elapsed_time:.6f} -> The time to pass every time.sleep()')

"""
* Function elastic time: 0.011042 ms (annotation time)
    함수의 실행 시간이 1초 보다 크게 짧음
        --> 대기와 상관없이 모든 코드를 실행 이후 함수 자체를 끝내버림
        --> 함수 자체가 비동기적으로 실행되는지?        
"""
