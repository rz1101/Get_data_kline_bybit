Этот проект предоставляет простой способ получения исторических свечей (криптовалютных ценовых данных) с биржи Bybit через их API. Он позволяет легко извлекать данные о ценах на различных временных интервалах.

Установка
Убедитесь, что у вас установлен Python 3.x
Установите необходимые зависимости:
pip install requests pandas
Скопируйте или клонируйте репозиторий:
git clone https://github.com/razumpost/get_data_kline_bybit.git
Перейдите в директорию проекта:
cd get_data_kline_bybit
Использование
Пример использования:

from kline import kline

df = kline("BTCUSDT", 60, "2023-09-09 00:00")
df.to_csv('btc_klines_60m.csv', index=False)
print(df.head())
Документация
Код содержит подробные комментарии, объясняющие каждую шаг функции kline.

Лицензия
Этот проект распространяется под лицензией MIT. Смотрите файл LICENSE для деталей.

Контакты
Если у вас есть вопросы или предложения по улучшению, пожалуйста, обратитесь к @razumpost.

Вопросы и ответы
Q: Какие параметры принимает функция kline? A: Функция принимает три аргумента: символ криптовалюты, временной интервал и начальную дату.
