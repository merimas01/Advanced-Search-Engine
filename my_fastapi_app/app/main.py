from fastapi import FastAPI
from app.routes import basic_routes, spell_corection_route, multiword_search_route, autocomplete_search_route, speech_recognition_route

app = FastAPI()


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(basic_routes.router)
app.include_router(spell_corection_route.router)
app.include_router(multiword_search_route.router)
app.include_router(autocomplete_search_route.router)
app.include_router(speech_recognition_route.router)


