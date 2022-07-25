import numpy as np

def random_predict(number) -> int:
    """Система угадывает случайное число от 1 до 100
    Args:
        number: Загаданное число
    Returns:
        int: Число попыток до успешного попадания
    """
    predict_number = np.random.randint(1, 101) # Задаем начальное случайное значение
    min_span = 1 # Минимальная граница динамического интервала
    max_span = 100 # Максимальная граница динамического интервала
    count = 0 # Счетчик попыток
    while True:
        count += 1
        if predict_number > number:
            max_span = predict_number - 1
            predict_number = (min_span + max_span) // 2
        elif predict_number < number:
            min_span = predict_number + 1
            predict_number = (min_span + max_span) // 2
        else: # условие выхода: predict_number == number
            break
    return count

def score(random_predict) -> int:
    """ За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    tryouts_list = []
    np.random.seed(5) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        tryouts_list.append(random_predict(number))
    score = int(np.mean(tryouts_list))
    return score

print(f"Ваш алгоритм угадывает число в среднем за: {score(random_predict)} попытки")