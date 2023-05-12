import pytest
import arithmetics

def test_tambah():
    result = arithmetics.tambah(10, 10)
    assert result == 20

def test_kurang():
    result = arithmetics.kurang(10, 10)
    assert result == 0

def test_kali():
    result = arithmetics.kali(10, 10)
    assert result == 100

def test_bagi():
    result = arithmetics.bagi(10, 10)
    assert result == 1
