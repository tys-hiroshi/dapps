import asyncio


Seconds = [
    ("first", 5),
    ("second", 0),
    ("third", 3)
]


async def sleeping(order, seconds, hook=None):
    print(seconds)
    await asyncio.sleep(seconds)
    if hook:
        hook(order)
    return order


async def basic_async():
    # the order of result is nonsequential (not depends on order, even sleeping time)
    for s in Seconds:
        print(s)
        print(*s)
        r = await sleeping(*s)
        print("{0} is finished.".format(r))
    return True

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(basic_async())