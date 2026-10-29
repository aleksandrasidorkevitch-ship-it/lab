# test_main.py
import pytest
from main import add_table, book, cancel, free_tables


def test_add_table_success():
    tables = {}
    add_table(tables, 1, 4)
    assert tables == {1: 4}


def test_add_table_invalid_capacity():
    tables = {}
    with pytest.raises(ValueError):
        add_table(tables, 1, 0)
    with pytest.raises(ValueError):
        add_table(tables, 1, -5)


def test_book_success():
    tables = {1: 2, 2: 4}
    bookings = {}
    # Бронируем на 18:00, 2 гостя. Должен подойти столик №1 (вместимость 2)
    table_num = book(tables, bookings, "Вася", "18:00", 2)
    assert table_num == 1
    assert "Вася" in bookings
    assert bookings["Вася"]["table"] == 1
    assert bookings["Вася"]["time"] == "18:00"
    assert bookings["Вася"]["guests"] == 2


def test_book_picks_first_suitable_table():
    tables = {1: 6, 2: 4, 3: 2}
    bookings = {}
    # На 2 гостя должен выбрать столик №1 (первый подходящий по номеру)
    table_num = book(tables, bookings, "Вася", "18:00", 2)
    assert table_num == 1


def test_book_no_tables_available():
    tables = {1: 2}
    bookings = {}
    # Просим 4 гостя, а столик только на 2
    with pytest.raises(ValueError):
        book(tables, bookings, "Вася", "18:00", 4)


def test_book_all_tables_occupied_at_time():
    tables = {1: 2}
    bookings = {}
    book(tables, bookings, "Вася", "18:00", 2)
    # Пытаемся забронировать на это же время
    with pytest.raises(ValueError):
        book(tables, bookings, "Маша", "18:00", 2)


def test_book_invalid_guests():
    tables = {1: 2}
    bookings = {}
    with pytest.raises(ValueError):
        book(tables, bookings, "Вася", "18:00", 0)


def test_cancel_success():
    bookings = {"Вася": {"table": 1, "time": "18:00", "guests": 2}}
    result = cancel(bookings, "Вася")
    assert result is True
    assert "Вася" not in bookings


def test_cancel_not_found():
    bookings = {}
    result = cancel(bookings, "Вася")
    assert result is False


def test_free_tables():
    tables = {1: 2, 2: 4, 3: 6}
    bookings = {
        "Вася": {"table": 2, "time": "18:00", "guests": 4},
        "Маша": {"table": 1, "time": "19:00", "guests": 2},
    }
    # На 18:00 занят столик 2, значит свободны 1 и 3
    free_at_18 = free_tables(tables, bookings, "18:00")
    assert free_at_18 == [1, 3]

    # На 19:00 занят столик 1, значит свободны 2 и 3
    free_at_19 = free_tables(tables, bookings, "19:00")
    assert free_at_19 == [2, 3]

    # На 20:00 нет броней, значит все свободны
    free_at_20 = free_tables(tables, bookings, "20:00")
    assert free_at_20 == [1, 2, 3]