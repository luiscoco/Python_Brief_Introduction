import asyncio

async def greet(name):
    await asyncio.sleep(1)
    print(f"Hello, {name}")

asyncio.run(greet("Alice"))