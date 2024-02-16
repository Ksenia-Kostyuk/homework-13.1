import pytest

from utils import Category, Product


@pytest.fixture
def category_test():
    return Category('Фрукты', 'Сладкие, спелые и свежие', ['Яблоки', 'Апельсины', 'Персики'])


@pytest.fixture
def product_test():
    return Product('Яблоки', 'Белый налив, сбор 2023 года', 70.0, 50)


def test_init_category(category_test):
    assert category_test.name == 'Фрукты'
    assert category_test.description == 'Сладкие, спелые и свежие'
    assert category_test.products == ['Яблоки', 'Апельсины', 'Персики']
    assert category_test.products_return() == 'Яблоки, Апельсины, Персики'


def test_init_product(product_test):
    assert product_test.name == 'Яблоки'
    assert product_test.description == 'Белый налив, сбор 2023 года'
    assert product_test.pay == 70.0
    assert product_test.in_stock == 50