from django.urls import path
from pages.views import home_view, methods_view, about_view
from Equation_Systems.views import doolittle

urlpatterns = [
    path("", home_view, name = "index.index"),
    path("methods/", methods_view, name="methods.index"),
    path("about/", about_view, name="about.index"),
    path("doolittle/", doolittle, name='dolittle.index')
]