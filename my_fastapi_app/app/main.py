from fastapi import FastAPI
from app.routes import basic_routes, spell_corection_route, multiword_search_route, autocomplete_search_route

app = FastAPI()

app.include_router(basic_routes.router)
app.include_router(spell_corection_route.router)
app.include_router(multiword_search_route.router)
app.include_router(autocomplete_search_route.router)