# test_main.py
import pytest
from main import mean, median, passed_count


def test_mean_normal():
    assert mean([4.0, 5.0, 3.0]) == 4.0

def test_mean_empty():
    with pytest.raises(ValueError):
        mean([])


def test_median_odd():
    # Нечетное количество: [3, 4, 5] -> медиана 4
    assert median([3.0, 4.0, 5.0]) == 4.0

def test_median_even():
    # Четное количество: [3, 4, 5, 6] -> медиана (4+5)/2 = 4.5
    assert median([3.0, 4.0, 5.0, 6.0]) == 4.5

def test_median_empty():
    with pytest.raises(ValueError):
        median([])


def test_passed_count():
    scores = [2.0, 3.9, 4.0, 5.0]
    # По умолчанию порог 4.0 (должно пройти 4.0 и 5.0)
    assert passed_count(scores) == 2
    # С кастомным порогом 3.0 (проходит 3.9, 4.0, 5.0)
    assert passed_count(scores, threshold=3.0) == 3
    # Пустой список
    assert passed_count([]) == 0