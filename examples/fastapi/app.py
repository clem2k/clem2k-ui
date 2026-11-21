"""Exemple FastAPI + Jinja2 avec clem2k-ui.

    pip install "clem2k-ui[fastapi] @ git+https://github.com/clem2k/clem2k-ui" fastapi uvicorn
    uvicorn app:app --reload
"""
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

import clem2k_ui

app = FastAPI()
templates = Jinja2Templates(directory="templates")
clem2k_ui.mount(app, "/clem2k", templates=templates)  # sert dist/ + logo, ajoute clem2k_head() et clem2k_icon()

SERVICES = [("traefik", "up", "ok"), ("nextcloud", "up", "ok"), ("backup", "restart", "warn")]


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(request, "index.html", {"services": SERVICES})
