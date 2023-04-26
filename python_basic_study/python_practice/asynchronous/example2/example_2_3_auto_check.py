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


for input_run_code in (1, 2, 3):
    run_code = input_run_code

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

"""
Explanation:
    * sync_main() -> 순차적 진행
    * asyncio.run(async_main()) -> 비동기적 진행
    
    * sync_main()
        One with sleep_time 2 -> wait for 2 seconds
        Two with sleep time 2 -> It has been over for 2 seconds
        One with sleep_time 1 -> wait for 1 seconds
        Two with sleep time 1 -> It has been over for 1 seconds
        One with sleep_time 3 -> wait for 3 seconds
        Two with sleep time 3 -> It has been over for 3 seconds
        sync_main() Elapsed time: 6.000000953674316 -> The time to pass every time.sleep()
        --> 2 + 1 + 3 = 6 seconds + 0.000000953674316 seconds (time.sleep() overhead)
        
    
    * asyncio.run(async_main())
        One with sleep_time 2 -> wait for 2 seconds
        One with sleep_time 1 -> wait for 1 seconds
        One with sleep_time 3 -> wait for 3 seconds
        Two with sleep_time 1 -> It has been over for 1 seconds
        Two with sleep_time 2 -> It has been over for 2 seconds
        Two with sleep_time 3 -> It has been over for 3 seconds
        async_main() Elapsed time: 3.0000009536743164 -> The time to pass every time.sleep()
        --> 3 seconds + 0.000000953674316 seconds (time.sleep() overhead)
                
        Sleep 2 seconds 동시에 Sleep 1 seconds 동시에 Sleep 3 seconds
        --> 가장 짧은 1초가 먼저 끝나고, 그 다음 2초가 끝나고, 마지막으로 3초가 끝남
        --> sleep 의 대기가 시작하면 대기 시간을 기다리지 않고 다음 코드를 실행함
        ==> 결과적으로 대기 시간이 가장 긴 3초 안에 1초, 2초의 대기가 끝남
        
    * Function elastic time: 0.011042 ms (annotation time)
        함수의 실행 시간이 1초 보다 크게 짧음
        --> 대기와 상관없이 모든 코드를 실행 이후 함수 자체를 끝내버림
        --> 함수 자체가 비동기적으로 실행되는지?        
        
        
        
Explanation_2:

sync_main(): runs sequentially
asyncio.run(async_main()): runs asynchronously

- sync_main() will wait for 2 seconds, then 1 second, then 3 seconds 
and the total time will be 6 seconds + a small overhead

- asyncio.run(async_main()) will wait for 2 seconds, 1 second and 3 seconds simultaneously,
so the total time will be 3 seconds + a small overhead

- Function elapsed time: 0.011042 ms (measured using an annotation) 
is significantly shorter than the actual wait time, 
this is because the function itself finishes quickly regardless of any waiting time
"""
