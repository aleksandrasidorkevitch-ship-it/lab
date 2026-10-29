# main.py
from typing import Dict, List, Optional


def add_table(tables: Dict[int, int], number: int, capacity: int) -> None:
    if capacity <= 0:
        raise ValueError("capacity must be > 0")
    tables[number] = capacity


def book(
    tables: Dict[int, int],
    bookings: Dict[str, dict],
    guest: str,
    time_slot: str,
    guests: int,
) -> int:
    if guests <= 0:
        raise ValueError("guests must be > 0")
    occupied = {
        b["table"]
        for b in bookings.values()
        if b["time"] == time_slot
    }
    candidates = sorted(
        (num, cap) for num, cap in tables.items() if num not in occupied and cap >= guests
    )
    if not candidates:
        raise ValueError("no table available")
    table_num = candidates[0][0]
    bookings[guest] = {"table": table_num, "time": time_slot, "guests": guests}
    return table_num


def cancel(bookings: Dict[str, dict], guest: str) -> bool:
    if guest in bookings:
        del bookings[guest]
        return True
    return False


def free_tables(tables: Dict[int, int], bookings: Dict[str, dict], time_slot: str) -> List[int]:
    occupied = {b["table"] for b in bookings.values() if b["time"] == time_slot}
    return sorted(num for num in tables if num not in occupied)