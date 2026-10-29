# main.py

def mean(scores: list[float]) -> float:
    """Среднее арифметическое оценок."""
    if not scores:
        raise ValueError("empty list")
    return sum(scores) / len(scores)


def median(scores: list[float]) -> float:
    """Медиана оценок (число посередине)."""
    if not scores:
        raise ValueError("empty list")
    
    sorted_scores = sorted(scores)
    n = len(sorted_scores)
    mid = n // 2
    
    if n % 2 == 1:
        return sorted_scores[mid]
    else:
        return (sorted_scores[mid - 1] + sorted_scores[mid]) / 2.0


def passed_count(scores: list[float], threshold: float = 4.0) -> int:
    """Количество оценок выше или равных порогу."""
    return sum(1 for score in scores if score >= threshold)