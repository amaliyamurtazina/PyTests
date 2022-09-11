# Для запуска ввести в терминал pytest -s -v tests/all_tests.py
import pytest

# тесты на структуры данных int
# позитивное
def test_is_positive():
    assert 1 > 0

# негативное
def test_type_is_not_int():
    a = 1
    if (type(a) != int) or (type(a) == int):
        assert True

# позитивное с параметром
@pytest.mark.parametrize('a, b, expected', [(10, 0, 10), (-10, 0, -10), (-10, 10, 0)])
def test_sum_with_param(a, b, expected):
    assert a + b == expected, 'Сумма считается не верно'


# тесты на структуры данных dict
# позитивное
def test_existence():
    users_age = {'Amaliya': 26, 'Roma': 28}
    assert 'Amaliya' in users_age

# позитивное с параметром
@pytest.mark.parametrize('users, expected_len', [({'Amaliya' : 26}, 1), ({'Amaliya': 26, 'Roma':28}, 2), ({}, 0)])
def test_len(users, expected_len):
    assert len(users) == expected_len

# негативное
def test_pop():
    users_age = {'Amaliya': 26, 'Roma': 28}
    try:
        assert users_age.pop('Dima')
    except KeyError:
        pass
