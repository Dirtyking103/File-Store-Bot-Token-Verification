from aiohttp import web
from .route import routes


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
async def example_handler(request):
    return web.Response(text="Hello, world!", content_type='text/plain')
    
