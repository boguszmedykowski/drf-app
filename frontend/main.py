import flet as ft
from flet import *
from pages.api_call import *
from views import views_handler
from appbar import *


def main(page: ft.Page):

    def route_change(route):
        print(page.route)
        page.views.clear()
        page.views.append(
            views_handler(page)[page.route]
        )
        pass

    page.on_route_change = route_change
    page.go('/')


ft.app(target=main, view=ft.WEB_BROWSER)
