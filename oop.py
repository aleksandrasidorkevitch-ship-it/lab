# oop.py
# Задача 25: Система бронирования столиков (ООП-стиль)


class Table:
    """Столик в ресторане."""

    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity


class Booking:
    """Бронь столика."""

    def __init__(self, guest, time, guests, table_number):
        self.guest = guest
        self.time = time
        self.guests = guests
        self.table_number = table_number


class Restaurant:
    """Ресторан: хранит столики и брони."""

    def __init__(self):
        self._tables = []
        self._bookings = []

    def add_table(self, number, capacity):
        """Добавить столик в зал."""
        self._tables.append(Table(number, capacity))

    def tables(self):
        """Список всех столиков."""
        return list(self._tables)

    def book(self, guest, time, guests):
        """Забронировать столик под число гостей на указанное время."""
        for table in self._tables:
            # проверка вместимости
            if table.capacity < guests:
                continue

            # проверка занятости
            if self._is_busy(table.number, time):
                continue

            # создаём бронь
            self._bookings.append(Booking(guest, time, guests, table.number))
            return table.number

        return None

    def cancel(self, guest, time):
        """Отменить бронь по гостю и времени."""
        for b in self._bookings:
            if b.guest == guest and b.time == time:
                # удаляем
                self._bookings.remove(b)
                return True
        return False

    def free_tables(self, time):
        """Столики, свободные на указанное время."""
        result = []
        for table in self._tables:
            # проверка занятости
            if not self._is_busy(table.number, time):
                result.append(table)
        return result

    def _is_busy(self, table_number, time):
        """Занят ли столик с таким номером на это время."""
        for b in self._bookings:
            if b.table_number == table_number and b.time == time:
                return True
        return False


if __name__ == "__main__":
    # создаём ресторан и столики
    rest = Restaurant()
    rest.add_table(1, 2)
    rest.add_table(2, 4)
    rest.add_table(3, 6)

    print("Столики в зале:")
    for t in rest.tables():
        print(f"  №{t.number} — до {t.capacity} чел.")

    print()
    print("Бронь: гость Вася, 18:00, 4 чел.")
    n = rest.book("Вася", "18:00", 4)
    print(f"Занят столик №{n}" if n is not None else "Свободных столиков нет")

    print()
    print("Бронь: гость Маша, 19:00, 2 чел.")
    n = rest.book("Маша", "19:00", 2)
    print(f"Занят столик №{n}" if n is not None else "Свободных столиков нет")

    print()
    print("Бронь: гость Петя, 18:00, 2 чел.")
    n = rest.book("Петя", "18:00", 2)
    print(f"Занят столик №{n}" if n is not None else "Свободных столиков нет")

    print()
    print("Свободные столики на 18:00:")
    for t in rest.free_tables("18:00"):
        print(f"  №{t.number} (до {t.capacity} чел.)")

    print()
    print("Свободные столики на 19:00:")
    for t in rest.free_tables("19:00"):
        print(f"  №{t.number} (до {t.capacity} чел.)")

    print()
    print("Отмена брони: гость Вася, 18:00")
    ok = rest.cancel("Вася", "18:00")
    print("Бронь удалена" if ok else "Бронь не найдена")

    print()
    print("Свободные столики на 18:00:")
    for t in rest.free_tables("18:00"):
        print(f"  №{t.number} (до {t.capacity} чел.)")