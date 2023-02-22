# PEPScrapy

<details>
  <summary>Содержание</summary>
  <ul>
    <li>
      <a href="#описание">Описание</a>
      <ul>
        <li><a href="#-возможности">Возможности</a></li>
        <li><a href="#технологии">Технологии</a></li>
      </ul>
    </li>
    <li>
      <a href="#-начало-работы">Начало работы</a>
      <ul>
          <li><a href="#-зависимости">Зависимости</a></li>
          <li><a href="#установка">Установка</a></li>
      </ul>
    </li>
    <li><a href="#-использование">Использование</a></li>
    <li><a href="#автор-проекта-ilya-petrukhin">Автор проекта</a></li>
  </ul>
</details>

<a name="описание"></a>

Парсер документов PEP на базе фреймворка Scrapy.

### 🔥 Возможности

- Для каждого документа PEP получить информацию: номер, название, статус.
- Узнать общее количество документов PEP в каждом статусе.

***Формат выходных данных: `.csv`***

### Технологии

[![Scrapy][Scrapy-badge]][Scrapy-url]

## ⚙ Начало Работы

Чтобы запустить локальную копию проекта, следуй инструкциям ниже.

### ⚠ Зависимости

- [Python 3.7+][Python-url]

### Установка

1. **Клонируй репозиторий**

    ```shell
    git clone https://github.com/tvules/PEPScrapy.git
    cd PEPScrapy
    ```

2. **Установи зависимости проекта**

    ```shell
    pip install -r requirements.txt
    ```

## 👀 Использование

1. **Выполни скрипт парсинга**

    ```shell
    scrapy crawl pep
    ```

   Собранная информация будет доступна в директории `results/`.

---

<h4 align="center">
Автор проекта: <a href="https://github.com/tvules">Ilya Petrukhin</a>
</h4>

<!-- MARKDOWN BADGES & URLs -->

[Python-url]: https://www.python.org/

[Scrapy-url]: https://scrapy.org/

[Scrapy-badge]: https://img.shields.io/badge/scrapy-60a839?style=for-the-badge
