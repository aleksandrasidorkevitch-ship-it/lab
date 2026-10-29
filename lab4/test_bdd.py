# test_bdd.py
import pytest
from pytest_bdd import given, when, then, parsers, scenario
from main import mean, median, passed_count

# --- ШАГИ (Step Definitions) ---

@given(parsers.parse('список оценок "{scores_str}"'), target_fixture="scores")
def given_scores(scores_str):
    # Превращаем строку "4, 5, 3" в список чисел [4.0, 5.0, 3.0]
    return [float(x.strip()) for x in scores_str.split(",")]

@when('я считаю средний балл', target_fixture="result")
def when_mean(scores):
    return mean(scores)

@then(parsers.parse('результат должен быть {expected:g}'))
def then_result_is(result, expected):
    assert result == expected

@when('я считаю медиану', target_fixture="result")
def when_median(scores):
    return median(scores)

@when(parsers.parse('я считаю сдавших с порогом {threshold:g}'), target_fixture="result")
def when_passed_count(scores, threshold):
    return passed_count(scores, threshold)

@then(parsers.parse('количество сдавших должно быть {expected:d}'))
def then_count_is(result, expected):
    assert result == expected

# --- ПРИВЯЗКА СЦЕНАРИЕВ ---
# Привязываем каждый сценарий из файла features/stats.feature к тесту

@scenario('features/stats.feature', 'Подсчет среднего балла')
def test_mean_scenario():
    pass

@scenario('features/stats.feature', 'Подсчет медианы для четного количества')
def test_median_scenario():
    pass

@scenario('features/stats.feature', 'Подсчет сдавших с кастомным порогом')
def test_passed_scenario():
    pass