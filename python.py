import asyncio 
import discord
from discord import Webhook
import aiohttp

async def anything(url):
   async with aiohttp.ClientSession() as session:
     webhook = Webhook.from_url(url, session=session)
     embed = discord.Embed(titLe="This is from a webhook!")
     await webhook.send (embed=embed, username="Richard Web")

if _name.== "_main_":
  url = 'https://discord.com/api/webhooks/1283614885661511712/hJ8nqs84PwRE4r5MSupsWcGy9nhSH8S73aif-Ks4sD3-jVZWT9uN0NqW0zIQ_AxSburc/github'

  loop = asyncio.new_event_loop()
  loop.run_until_complete(anything(url))
  loop.close
