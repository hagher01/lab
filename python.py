from discord import Webhook
import aiohttp

async def foo():
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url('https://discord.com/api/webhooks/1283614885661511712/hJ8nqs84PwRE4r5MSupsWcGy9nhSH8S73aif-Ks4sD3-jVZWT9uN0NqW0zIQ_AxSburc/github', session=session)
        await webhook.send('Hello World', username='Foo')

import requests
from discord import Webhook, RequestsWebhookAdapter
webhook = Webhook partial(1283614885661511712, 'hJ8nqs84PwRE4r5MSupsWcGy9nhSH8S73aif', adapter=RequestsWebhookAdapter () )
webhook send ( 'Hello World',
