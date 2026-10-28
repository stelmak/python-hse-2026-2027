"""
ДЗ презентации 5, повышенный уровень, задача 2.
Время: 25–35 минут.

Тема: минимальное число платформ.

Условие:
    Даны arrivals и departures поездов.
    Верните минимальное число платформ.

Пример:
    arrivals   = [900, 940, 950, 1100, 1500, 1800]
    departures = [910, 1200, 1120, 1130, 1900, 2000]
    Ответ: 3
"""

arrivals   = [900, 940, 950, 1100, 1500, 1800]
departures = [910, 1200, 1120, 1130, 1900, 2000]

def min_platforms(arrivals: list, departures: list) -> int:

    arrivals = sorted(arrivals, reverse=False)
    departures = sorted(departures, reverse=False)
    max_platforms = 0
    now_platforms = 0

    i = 0
    j = 0

    while i < len(arrivals) and j < len(departures):
        if arrivals[i] < departures[j]:
            now_platforms += 1
            if now_platforms > max_platforms:
                max_platforms += 1
            i += 1
        else:
            now_platforms -= 1
            j += 1

    return max_platforms

if __name__ == "__main__":
    assert min_platforms([], []) == 0
    assert min_platforms([900], [910]) == 1
    assert min_platforms(
        [900, 940, 950, 1100, 1500, 1800],
        [910, 1200, 1120, 1130, 1900, 2000]
    ) == 3
    assert min_platforms([100, 200, 300], [150, 250, 350]) == 1
    print("task_02 (p5 advanced): тесты пройдены")