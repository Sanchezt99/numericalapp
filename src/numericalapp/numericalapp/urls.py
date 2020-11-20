from django.urls import path
from pages.views import home_view, methods_view

urlpatterns = [
    path("", home_view, name = "index.index"),
    path("methods", methods_view, name="methods.index"),
]