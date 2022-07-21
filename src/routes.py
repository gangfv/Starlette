from starlette.routing import Route

from src.endpoints import get_support, Home

routes = [
    Route('/', Home),
    Route('/support', get_support, name='get_support'),
]

