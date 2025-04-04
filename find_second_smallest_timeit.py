import timeit

def find_second_smallest(numbers):
    """
    Находит второе наименьшее число в списке.
    Если список слишком короткий или не имеет второго наименьшего, возвращает None.
    """
    if not numbers or len(numbers) < 2:
        return None

    smallest = numbers[0]
    second_smallest = None

    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num > smallest:
            if second_smallest is None or num < second_smallest:
                second_smallest = num
    return second_smallest

# Пример использования
data = [3, 1, 4, 3, 5, 9, 3, 6, 5]

# Замер времени
num_iterations = 10000  # Увеличено количество итераций для большей точности
time_taken = timeit.timeit(lambda: find_second_smallest(data), number=num_iterations)

print(f"Среднее время выполнения функции (после {num_iterations} итераций): {time_taken / num_iterations:.7f} секунд")

second_min = find_second_smallest(data)

if second_min is not None:
    print("Второе наименьшее число:", second_min)
else:
    print("В списке нет второго наименьшего числа.")

