import asyncio
from aiohttp import web

@asyncio.coroutine
def hello(request):
    return web.Response(body=b'Hello Baby Etchecopar')

app = web.Application()
app.router.add_route('GET', '/', hello)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    handler = app.make_handler()
    f = loop.create_server(handler, '0.0.0.0', 9998)
    srv = loop.run_until_complete(f)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.run_until_complete(handler.finish_connections(1.0))
        srv.close()
        loop.run_until_complete(srv.wait_closed())
        loop.run_until_complete(app.finish())
    loop.close()