import os
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(
    tags=["base"],
    responses={404: {"description": "Not found"}},
)

templates = Jinja2Templates(os.path.join(os.getcwd(), "app/public/templates"))

@router.get("/", response_class=HTMLResponse)
def get_home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/login", response_class=HTMLResponse)
def get_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/menu", response_class=HTMLResponse)
def get_menu_page(request: Request):
    return templates.TemplateResponse("menu.html", {"request": request})

@router.get("/admin", response_class=HTMLResponse)
def get_admin_page(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

@router.get("/password_reset", response_class=HTMLResponse)
def get_password_reset_page(request: Request):
    return templates.TemplateResponse("password_reset.html", {"request": request})
