from starlette.endpoints import HTTPEndpoint
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from config.database import database
from src.models import support

template = Jinja2Templates(directory='templates')


async def get_support(request):
    query = support.select()
    results = await database.fetch_all(query)
    return template.TemplateResponse('support.html', {"request": request, "results": results})


class Home(HTTPEndpoint):
    async def get(self, request):
        return template.TemplateResponse('index.html', {"request": request})

    async def post(self, request):
        form = await request.form()
        query = support.insert().values(
            username=form['username'],
            email=form['email'],
            message=form['message'],
        )
        await database.execute(query)
        return RedirectResponse(request.url_for('get_support'), status_code=303)
