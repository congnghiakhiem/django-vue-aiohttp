import asyncio

from aiohttp import web
from aiohttp_wsgi import WSGIHandler

from mysite.wsgi import application


async def init_app():
    from myapp.events_handler import event_routes
    from myapp.websocket import ws_routes
    
    wsgi_handler = WSGIHandler(application)
    app = web.Application()

    # routes
    app.router.add_routes(ws_routes)
    app.router.add_routes(event_routes)
    app.router.add_route("*", "/{path_info:.*}", wsgi_handler)

    # # pg
    # db_url = config('DATABASE_URL', default='', cast=parse)
    # app['pgpool'] = await asyncpg.create_pool(
    #     database=db_url['NAME'],
    #     user=db_url['USER'],
    #     password=db_url['PASSWORD'],
    #     host=db_url['HOST'],
    #     port=db_url['PORT']
    # )

    # # redis
    # app['redispool'] = await aioredis.create_redis_pool(settings.REDIS_URL, minsize=5, maxsize=10, loop=loop)

    return app


loop = asyncio.get_event_loop()
web.run_app(loop.run_until_complete(init_app()), port=8000)
