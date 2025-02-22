# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Установка

- Скачайте код
- Перейдите в каталог wine
- Создайте виртуальную среду и активируйте:

```py
python -m venv .venv
.venv\Scripts\activate
```

- Установите зависимости:

```py
pip install -r requerements.txt
```

## Входные данные

- Данные берутся из excel, в таблице указан образец:

| **Категория** | **Название**        | **Сорт**        | **Цена** | **Картинка**             | **Акция**            |
|---------------|---------------------|-----------------|----------|--------------------------|----------------------|
| Белые вина    | Белая леди          | Дамский пальчик | 399      | belaya_ledi.png          | Выгодное предложение |
| Напитки       | Коньяк классический |                 | 350      | konyak_klassicheskyi.png |                      |
| Белые вина    | Ркацители           | Ркацители       | 499      | rkaciteli.png            |                      |

- Также есть пример файла [wine.xlsx](./wine.xlsx) который можно заполнить своими данными.

## Запуск

- Запуск сайта с данными из образца командой:

```py
python main.py
```

- С данными из заполненного файла:

```py
python main.py --file "путь к файлу" --sheet "наименование листа таблицы"
```

- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
