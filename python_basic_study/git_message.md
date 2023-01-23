# git message

### 2023-01-15

1. 
```text

Study > EOF, Annotation Snippets
         
    1. EOF = End of File
        The way to check up where reads stop
        Make 2 example
     
    2. Calculate Elapsed time snippet
        Use as annotation

```

### 2023-01-22
1.
```text
Study > Asynchronous concept


    < Goals >
        - To understand about asynchronous concept
        
        - Specifically:
            - To make sync and async code
            - Find out what these two are different
            - Calculate the time difference of executive 
    
    
    < Result > 
        
        * sync_main(): runs sequentially
        * asyncio.run(async_main()): runs asynchronously
        
        - sync_main():
            will wait for 2 seconds, then 1 second, then 3 seconds 
            and the total time will be 6 seconds + a small overhead
        
        - asyncio.run(async_main()):
            will wait for 2 seconds, 1 second and 3 seconds simultaneously,
            so the total time will be 3 seconds + a small overhead
        
        - Function elapsed time: 0.011042 ms (measured using an annotation): 
            is significantly shorter than the actual wait time,
            this is because the function itself finishes quickly
            regardless of any waiting time
    
    
    
    < Code >
        1. python_practice/asynchronous/example_1.py
            How to use async, await, asyncio keyword 
        
        2. python_practice/asynchronous/example2/ 
            The test how much time it takes to run the code
            between asynchronous and synchronous
            
            The main concept code is
            "example_2_3_auto_check.py"
            The bottom of this code,
            I wrote detailed about that I understand  
       
```