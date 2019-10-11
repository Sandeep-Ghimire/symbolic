
import main
from main import *
import pytest
Poly = main.Polynomial


class TestPolyNoArg:

    @staticmethod
    @pytest.fixture
    def zero_poly():
        return Poly()

    def test_init(self,zero_poly):
        zero_poly

    def test_repr(self,zero_poly):
        assert str(zero_poly) == ""

    def test_simplify(self,zero_poly):
        zero_poly.simplify()
        assert zero_poly._poly == []

    def test_addition(self,zero_poly):
        p = Poly() + Poly()
        assert p._poly == []


class TestSimplify:
    def test_all_nonzero_coeffs(self):
        "simplify does not modify nonzero args"
        p = Poly([(1,2),(3,4),(5,6)])
        p.simplify()
        assert p._poly == [(1,2),(3,4),(5,6)]

    def test_with_some_zero_coeffs(self):
        p = Poly([(0,1),(0,1),(3,1),(4,6)])
        p.simplify()
        assert p._poly == [(3,1),(4,6)]


class TestRepr:
    def test_when_power_is_1(self):
        p = Poly([(2,1),(3,2),(4,1)])
        assert str(p) == "6x+3x^2"

    def test_when_power_is_zero(self):
        p = Poly([(2,0),(3,2),(4,0)])
        assert str(p) == "6+3x^2"

    def test_when_power_is_neither_zero_nor_one(self):
        p = Poly([(2,3),(4,5),(-6,7)])
        assert str(p) == "2x^3+4x^5-6x^7"


class TestAddition:
    def test_add(self):
        a = Poly([(1,2),(3,4)])
        b = Poly([(2,2),(-6,4)])
        assert (a+b)._poly == [(3,2),(-3,4)]

    def test_diff_power(self):
        a = Poly([(0,2),(-3,-4)])
        b = Poly([(1,3),(-5,16)])
        assert (a+b)._poly == [(-3,-4),(1,3),(-5,16)]

class TestSubtraction:
    def test_same_object_yields_empty_poly(self):
        p = Poly([(1,2),(3,4),(5,6)])
        assert (p - p) == Poly()

    def test_sub(self):
        p1 = Poly([(1,2),(3,4),(5,6)])
        p2 = Poly([(-1,2),(-3,4),(-5,6)])
        assert p1 - p2 == Poly([(2,2),(6,4),(10,6)])

    def test_sub2(self):
        p1 = Poly([(4,5),(-3,2),(6,-8)])
        p2 = Poly([(1,2),(3,5),(6,-8)])
        assert p1 - p2 == Poly([(-4,2),(1,5)])



class TestMultiplication:
    def test_mult_on_zero(self):
        p = Poly()
        assert (p * p) == p

    def test_mult(self):
        p1 = Poly([(1,1),(2,2),(3,3)])
        p2 = Poly([(1,2),(1,1)])
        assert p1*p2 == Poly([(1,3),(1,2),(2,4),(2,3),(3,5),(3,4)])




split_by = main.split_by

def test_split_by():
    assert split_by("",lambda x : x) == ['']
    assert split_by("x^2-3x^7+90x^43",lambda x:x =='+' or x=='-') == ['x^2',"-3x^7","+90x^43"]




        



 