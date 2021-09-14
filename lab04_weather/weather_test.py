import pytest
from weather import weather

def test_basic():
    assert weather('07-12-2008', 'Albury') == (-4.8, 2.4)
    assert weather('28-01-2014', 'Albury') == (-6.9, 14.0)
    assert weather('11-03-2009', 'SalmonGums') == (-6.7, 11.6)
    assert weather('24-06-2017', 'Uluru') == (6.6, -3.4)

def test_invalid_date():
    assert weather('1234123', 'Albury') == (None, None)

def test_invalid_location():
    assert weather('10-08-2009', 'Novigrad') == (None, None)

def test_out_of_range_date():
    assert weather('9-05-1990', 'Albury') == (None, None)

def test_date_with_missing_data():
    assert weather('11-09-2009', 'Albury') == (None, None)

def test_non_string_date():
    assert weather(26, 'Albury') == (None, None)

def test_non_string_location():
    assert weather('07-12-2008', -123) == (None, None)