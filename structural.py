# structural.py
# Задача 25: Система бронирования столиков (структурный стиль)


def book_table(tables, bookings, guest, time, guests):
    """Забронировать столик под число гостей на указанное время."""
    for table in tables:
        # проверка вместимости
        if table["capacity"] < guests:
            continue

        # проверка занятости
        busy = False
        for b in bookings:
            if b["table_number"] == table["number"] and b["time"] == time:
                busy = True
                break
        if busy:
            continue

        # создаём бронь
        bookings.append({
            "guest": guest,
            "time": time,
            "guests": guests,
            "table_number": table["number"],
        })
        return table["number"]

    return None


def cancel_booking(bookings, guest, time):
    """Отменить бронь по гостю и времени."""
    for b in bookings:
        if b["guest"] == guest and b["time"] == time:
            # удаляем
            bookings.remove(b)
            return True
    return False


def free_tables(tables, bookings, time):
    """Столики, свободные на указанное время."""
    result = []
    for table in tables:
        # проверка занятости
        busy = False
        for b in bookings:
            if b["table_number"] == table["number"] and b["time"] == time:
                busy = True
                break
        if not busy:
            result.append(table)
    return result


if __name__ == "__main__":
    # зал: три столика
    tables = [
        {"number": 1, "capacity": 2},
        {"number": 2, "capacity": 4},
        {"number": 3, "capacity": 6},
    ]
    bookings = []

    print("Столики в зале:")
    for t in tables:
        print(f"  №{t['number']} — до {t['capacity']} чел.")

    print()
    print("Бронь: гость Вася, 18:00, 4 чел.")
    n = book_table(tables, bookings, "Вася", "18:00", 4)
    print(f"Занят столик №{n}" if n is not None else "Свободных столиков нет")

    print()
    print("Бронь: гость Маша, 19:00, 2 чел.")
    n = book_table(tables, bookings, "Маша", "19:00", 2)
    print(f"Занят столик №{n}" if n is not None else "Свободных столиков нет")

    print()
    print("Бронь: гость Петя, 18:00, 2 чел.")
    n = book_table(tables, bookings, "Петя", "18:00", 2)
    print(f"Занят столик №{n}" if n is not None else "Свободных столиков нет")

    print()
    print("Свободные столики на 18:00:")
    for t in free_tables(tables, bookings, "18:00"):
        print(f"  №{t['number']} (до {t['capacity']} чел.)")

    print()
    print("Свободные столики на 19:00:")
    for t in free_tables(tables, bookings, "19:00"):
        print(f"  №{t['number']} (до {t['capacity']} чел.)")

    print()
    print("Отмена брони: гость Вася, 18:00")
    ok = cancel_booking(bookings, "Вася", "18:00")
    print("Бронь удалена" if ok else "Бронь не найдена")

    print()
    print("Свободные столики на 18:00:")
    for t in free_tables(tables, bookings, "18:00"):
        print(f"  №{t['number']} (до {t['capacity']} чел.)")