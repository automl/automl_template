import pytest
from pytest import mark

from automl_template.myclass import MyClass


@mark.parametrize("a", [-10, -1, 0])
def test_construction_with_negative_a(a: int) -> None:
    """
    Parameters
    ----------
    a : int
        The bad `a` parameter to construct `MyClass` with

    Expects
    -------
    * Should raise a ValueError with a zero or negative int
    """
    with pytest.raises(ValueError):
        MyClass(a=a, b={})


@mark.parametrize("a", [1, 10])
@mark.parametrize("x", [-10, -1, 0, 1, 10])
def test_oreos(a: int, x: int) -> None:
    """
    Parameters
    ----------
    a : int
        Parameter to construct MyClass with

    x : int
        Parameter to `oreos`

    Expects
    -------
    * Should return `a + x`
    """
    myclass = MyClass(a=a, b={})
    assert myclass.oreos(x) == a + x


@mark.parametrize("x", [1337])
def test_oreoes_detects_haxor(x: int) -> None:
    """
    Parameters
    ----------
    x : int
        A hacking number

    Expects
    -------
    * Should detect haxor numbers
    """
    myclass = MyClass(a=1, b={})
    with pytest.raises(ValueError):
        myclass.oreos(x)


@mark.parametrize("a", [1, 10, 30])
@mark.parametrize("c, value", [(True, "foo"), (False, "bar")])
def test_spaghetti_hoops(a: int, c: bool, value: str) -> None:
    """
    Parameters
    ----------
    a : int
        Parameter controlling how many hoops to make

    c : bool
        Switch to control whether "foo" or "bar" is given

    value: str
        Whether to expect "foo" or "bar" as the values

    Expects
    -------
    * Should have a length of `a`
    * Should have the mapping "hoop_{i}": `value`
    """
    myclass = MyClass(a=a, b={}, c=c)
    result = myclass.spaghetti_hoops

    assert len(result) == a
    assert all(result[f"hoop_{i}"] == value for i in range(a))
