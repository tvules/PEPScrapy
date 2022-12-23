# Scrapy PEP

## Особенности

- Собрать данные о всех документах `PEP`
- Получить информацию о количестве документов `PEP` в каждом статусе
- Узнать общее количество всех документов `PEP`

**Формат выходных данных: `.csv`**

## Технологии

- [Python 3.7+](https://www.python.org/)
- [Scrapy](https://scrapy.org/)

## Инструкция

**1. Клонируйте репозиторий**

```shell
git clone https://github.com/tvules/scrapy_parser_pep.git
cd scrapy_parser_pep
```

**2. Установите зависимости проекта**

```shell
pip install -r requirements.txt
```

**3. Запустите процесс парсинга**

```shell
scrapy crawl pep
```

**4. По окончанию процесса файлы будут доступны в директории `results`**

<h5 align="center">Автор проекта: <a href="https://github.com/tvules">Ilya Petrukhin</a></h5>
