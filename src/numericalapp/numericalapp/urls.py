from django.urls import path
from pages.views import home_view, methods_view, about_view
from Equation_Systems.views import doolittle_view, jacobi_view, gaussSeidel_view, gaussSimple_view
from Function_Roots.views import fixedPoint_view, newton_view, secant_view

urlpatterns = [
    path("", home_view, name = "index.index"),
    path("methods/", methods_view, name="methods.index"),
    path("about/", about_view, name="about.index"),
    path("fixedPoint/", fixedPoint_view, name="fixedPoint.index"),
    path("secant/", secant_view, name="secant.index"),
    path("newton/", newton_view, name="newton.index"),
    path("doolittle/", doolittle_view, name='doolittle.index'),
    path("gaussSeidel/", gaussSeidel_view, name="gaussSeidel.index"),
    path("jacobi/", jacobi_view, name="jacobi.index"),
    path("gaussSimple/", gaussSimple_view, name="gaussSimple.index")
]