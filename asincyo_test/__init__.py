import asyncio

async def main():
    return await func2()

async def func2():
    for i in range(10):
        await asyncio.sleep(1.5)
        print("WORKING! x2")
    return "HELLO"

async  def wait_me():
    for i in range(10):
        await asyncio.sleep(1)
        print("WORKING!")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    exec =asyncio.wait([wait_me(), main()])
    print(loop.run_until_complete(exec))
