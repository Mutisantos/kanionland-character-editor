# Coroutine: A function that can be paused and then be resumed
# The library on a request generates an event loop for execution
# After the event loop is generated, it can be used to execute coroutines
import asyncio
import random


async def file_process(file):
    print(f'Processing archivo {file}')
    time = random.randint(1, 10)
    await asyncio.sleep(time)
    print(f'{file} downloaded')
    return file


async def main():
    print('Begin Processing Files:')
    result = await file_process('file1.txt')
    result1 = await file_process('file2.txt')
    result2 = await file_process('file3.txt')
    print(f'{result,result1,result2}')


asyncio.run(main())
