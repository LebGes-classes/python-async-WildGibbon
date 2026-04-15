import asyncio
import os
import time

import pandas as pd



async def async_read_excel(path):
    print(f"{path} gay started")
    return await asyncio.to_thread(pd.read_excel, path)

async def main():
    coroutines = []

    for file_name in os.listdir("data"):
        if file_name.endswith(".xlsx"):
            coroutines.append(async_read_excel("data/" + file_name))

    results = await asyncio.gather(*coroutines)
    print(results)



asyncio.run(main())
