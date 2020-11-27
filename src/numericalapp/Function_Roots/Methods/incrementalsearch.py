from sympy.parsing.sympy_parser import parse_expr as pe
import sympy as sp
from math import *


def Incrementalsearches(function,initialvalue,d,i):
	f= pe(function)
	xo=initialvalue
	ansTable = []
	x = sp.symbols('x')
	found=False

	if f.subs(x,xo) == 0:
		iterFound =  f'Root of f found at x = {xo}'
		ansTable.append(iterFound)
		xo += d
		found = True

	cont = 0 
	while (cont < i):
		res1 = f.subs(x,xo)
		xa = xo + d
		res2 = f.subs(x,xa)
		if res2 == 0:
			iterFound = f'Root of f found at x = {xa}'
			ansTable.append(iterFound)
			xa += d
			found=True
		elif (res1*res2 < 0):
			m = f'There is a root of f in ( {"{:14.5f}".format(xo)},{"{:14.5f}".format(xa)} )'
			ansTable.append(m)
			found=True
		cont += 1
		xo=xa
	if (cont==i and not found):
		message = "With the number of requested iterations, no interval was found that could contain a root"
		return ansTable, message
	message = "Roots information"
	return ansTable, message

