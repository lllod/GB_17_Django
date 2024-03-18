# Фреймворк Django (семинары)

## Семинар 1

1. Создайте пару представлений в вашем первом приложении:
    * главная
    * о себе.
2. Внутри каждого представления должна быть переменная html — многострочный текст с HTML-вёрсткой и данными о вашем
   первом
   Django-сайте и о вас (было сделано на семинаре).
3. Сохраняйте в логи данные о посещении страниц.
4. Вместо хранения html в переменной, подумать как можно реаллизовать через работу с файлом html.

**Выполнено**
> Приложение seminar1app

## Семинар 2

1. Создайте три модели Django: клиент, товар и заказ.
   Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько
   заказов.
    1. Поля модели «Клиент»:
       * имя клиента
       * электронная почта клиента
       * номер телефона клиента
       * адрес клиента
       * дата регистрации клиента
    2. Поля модели «Товар»:
       * название товара
       * описание товара
       * цена товара
       * количество товара
       * дата добавления товара
    3. Поля модели «Заказ»:
       * связь с моделью «Клиент», указывает на клиента, сделавшего заказ
       * связь с моделью «Товар», указывает на товары, входящие в заказ
       * общая сумма заказа
       * дата оформления заказа
2. Допишите несколько функций CRUD для работы с моделями по желанию. Что по вашему мнению актуально в такой базе.

**Выполнено**
> Приложение seminarsapp

## Семинар 3

Продолжаем работать с товарами и заказами.

1. Создайте шаблон, который выводит список заказанных клиентом товаров из всех его заказов с сортировкой по времени:
   * за последние 7 дней (неделю)
   * за последние 30 дней (месяц)
   * за последние 365 дней (год)

Товары в списке не должны повторятся.

**Выполнено**
> Приложение seminarsapp