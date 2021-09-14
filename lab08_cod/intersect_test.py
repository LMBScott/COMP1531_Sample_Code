import pytest
from cod import Line_Segment

def test_vertical_intersect_oblique():
    a = Line_Segment((1,1),(1,5))
    b = Line_Segment((3,3),(-2,1))
    assert a.intersects(b)

def test_vertical_intersect_vertical():
    a = Line_Segment((1,1),(1,5))
    b = Line_Segment((1,2),(1,3))
    assert a.intersects(b)

def test_vertical_not_intersect_vertical():
    a = Line_Segment((1,1),(1,5))
    b = Line_Segment((2,2),(2,3))
    assert not a.intersects(b)

def test_horizontal_not_intersect_horizontal():
    a = Line_Segment((1,1),(5,1))
    b = Line_Segment((1,2),(5,2))
    assert not a.intersects(b)

def test_horizontal_not_intersect_horizontal():
    a = Line_Segment((1,1),(5,1))
    b = Line_Segment((1,2),(5,2))
    assert not a.intersects(b)

def test_horizontal_intersect_vertical():
    a = Line_Segment((1,1),(1,5))
    b = Line_Segment((0,2),(2,2))
    assert a.intersects(b)

def test_oblique_intersects_oblique():
    a = Line_Segment((1,1),(3,3))
    b = Line_Segment((1,3),(3,1))
    assert a.intersects(b)

def test_oblique_intersects_oblique():
    a = Line_Segment((1,2),(5,6))
    b = Line_Segment((1,1),(5,8))
    assert a.intersects(b)

def test_oblique_not_intersect_oblique():
    a = Line_Segment((1,2),(5,6))
    b = Line_Segment((1,1),(2,2))
    assert not a.intersects(b)

def test_vertical_intersects_oblique_end():
    a = Line_Segment((3,1),(3,3))
    b = Line_Segment((1,1),(3,3))
    assert a.intersects(b)