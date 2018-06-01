import asyncio
from datetime import datetime

from aiohttp import web
from aiohttp_sse import sse_response

event_routes = web.RouteTableDef()


@event_routes.get('/events')
async def event_handler(request):
    loop = request.app.loop
    async with sse_response(request) as resp:
        while True:
            data = 'Server Time : {}'.format(datetime.now())
            print(data)
            await resp.send(data)
            await asyncio.sleep(1, loop=loop)
