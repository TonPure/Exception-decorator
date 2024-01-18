import time

special_list = ['f1', 'f2', 'f3', 'f4', 'f5'] # список названий особенных функций

def decorator(func):
    def wrapper(*args, **kwargs):
        attempts = 0                          # счетчик попыток для особенных функций
        try:
            #raise ZeroDivisionError          # раскоментировать для симуляции ошибки
            return func(*args, **kwargs)
        except Exception as e:
            fname = func.__name__             # имя функции для проверки на особенность
            print(f"Attempt failed: {e}")
            time.sleep(1)
            if fname in special_list:         # если фун-я особенная
                while attempts < 3:           # пытаемся 3 раза
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        attempts += 1         # подсчет попыток
                        print(f"Attempt {attempts} failed: {e}")
                        time.sleep(1)
            else:                             # фун-я не особенная
                while True:
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        print(f"Attempt failed: {e}")
                        time.sleep(1)
    return wrapper

@decorator
def f1(das):                                 # фун-я для проверки
    print(das*2)
f1('k')

