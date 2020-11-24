from django.urls import path
from pages.views import home_view, methods_view, about_view, help_view
from Equation_Systems.views import doolittle_view, jacobi_view, gaussSeidel_view, gaussSimple_view, pivot_view
from Function_Roots.views import fixedPoint_view, newton_view, secant_view, incrementalsearch_view,falseposition_view,bisection_view
from Interpolation.views import splains_view, vandermonde_view, newtondivdif_view, lagrange_view, neville_view

urlpatterns = [
    path("", home_view, name = "index.index"),
    path("methods/", methods_view, name="methods.index"),
    path("about/", about_view, name="about.index"),
    path("help/", help_view, name="help.index"),
    path("fixedPoint/", fixedPoint_view, name="fixedPoint.index"),
    path("secant/", secant_view, name="secant.index"),
    path("newton/", newton_view, name="newton.index"),
    path("incrementasearch/", incrementalsearch_view, name="incrementalsearch.index"),
    path("falseposition/", falseposition_view, name="falseposition.index"),
    path("bisection/", bisection_view, name="bisection.index"),
    path("doolittle/", doolittle_view, name='doolittle.index'),
    path("gaussSeidel/", gaussSeidel_view, name="gaussSeidel.index"),
    path("jacobi/", jacobi_view, name="jacobi.index"),
    path("gaussSimple/", gaussSimple_view, name="gaussSimple.index"),
    path("splains/", splains_view, name="splains.index"),
    path("vandermonde/", vandermonde_view, name="vandermonde.index"),
    path("newtondivdif/", newtondivdif_view, name="newtondivdif.index"),
    path("lagrange/", lagrange_view, name="lagrange.index"),
    path("neville/", neville_view, name="neville.index")
    path("pivot/", pivot_view, name="pivot.index")
]