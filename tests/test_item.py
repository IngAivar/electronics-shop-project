"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def test_data():
    return Item("Смартфон", 10000, 20)


def test_item_init(test_data):
    assert type(test_data.name) == str
    assert type(test_data.price) == int
    assert type(test_data.quantity) == int
    assert type(test_data.all) == list

    assert test_data.name == "Смартфон"
    assert test_data.price == 10000
    assert test_data.quantity == 20


def test_calculate_total_price(test_data):
    assert test_data.calculate_total_price() == test_data.price * test_data.quantity


def test_apply_discount(test_data):
    test_data.apply_discount()
    assert test_data.price == 10000
