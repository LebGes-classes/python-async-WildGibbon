import data_analytics.analizes_instruments as inst
import pandas as pd
import asyncio
import os


async def async_read_excel(path) -> pd.DataFrame:
    return await asyncio.to_thread(pd.read_excel, path)

async def async_write_excel(sheets: list[pd.DataFrame], path) -> None:
    with pd.ExcelWriter(path) as writer:
        for i, sheet in enumerate(sheets):
            await asyncio.to_thread(sheet.to_excel, writer, sheet_name=str(i))

async def main():
    read_coroutines = []
    write_coroutines = []

    for file_name in os.listdir("data"):
        if file_name.endswith(".xlsx"):
            read_coroutines.append(async_read_excel("data/" + file_name))

    data_frames : list[pd.DataFrame] = await asyncio.gather(*read_coroutines)

    for i, df in enumerate(data_frames):
        sheets = [inst.sort_by_calibration_dates(df),
                  inst.filter_warranty(df),
                  inst.sort_by_issues(df)]

        write_coroutines.append(async_write_excel(sheets, f"output/output_{i}.xlsx"))

    await asyncio.gather(*write_coroutines)


asyncio.run(main())
