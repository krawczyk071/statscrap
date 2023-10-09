import asyncio
import json
import pandas as pd
import aiohttp

from understat import Understat


# async def main():
#     async with aiohttp.ClientSession() as session:
#         understat = Understat(session)
#         data = await understat.get_league_players(
#             "epl", 2018, {"team_title": "Manchester United"}
#         )
#         print(json.dumps(data))


async def main():
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        table = await understat.get_league_table("EPL", "2018")
        # print(table)
        file_path = "out18.csv"
        out_dict = table
        df = pd.DataFrame.from_dict(out_dict)
        df.to_csv(file_path, index=False, header=True)


# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
