import asyncio


async def gay(text):
    print(f"{text} gay started")
    await asyncio.sleep(1)
    print(f"{text} gay stopped")

async def main():
    await asyncio.gather(gay("1"), gay("2"))

asyncio.run(main())
