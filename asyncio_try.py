import asyncio

@asyncio.coroutine
def slow():
    yield from asyncio.sleep(2)
    print ('slow-1')
    yield from asyncio.sleep(1)
    print ('slow-2')
    return "done slow"


@asyncio.coroutine
def fast():
    yield from asyncio.sleep(1)
    print ('fast-1')
    yield from asyncio.sleep(3)
    print ('fast-2')
    return 'done fast'


def return_future_result(future):
    print (future.result())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    for i in range(2):
        if i == 0:
            task = loop.create_task(slow())
        else:
            task = loop.create_task(fast())
        task.add_done_callback(return_future_result)

    loop.run_until_complete(task)


'''
Output 

fast-1
slow-1
slow-2
done slow
fast-2
done fast

'''