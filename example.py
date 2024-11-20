# дон! это пример файла как работает модуль дон
from don import Консоль_Дон

def main():
    # иниализируем консоль для вывода 
    консоль = Консоль_Дон()
    print('Пример использования:')


    # напесат_дон
    консоль.напесат_дон('Привет, это демонстрация дон')

    # спросить_дон
    имя = консоль.спросить_дон('Как тебя звать')
    консоль.напесат_дон(f'Дон рад тебя видеть, {имя}')

    # повтор_дон
    консоль.повтор_дон('Повторяем дон', 3)

    # перевернуты_дон
    консоль.перевернуты_дон('Сила Дона велика')

    # список_обход_дон
    консоль.список_обход_дон(['Первый дон', 'Второй дон', 'Третий дон'])

    # болшой_буквы_дон
    консоль.болшой_буквы_дон('я важный текст дон')

if __name__ == '__main__':
    main()