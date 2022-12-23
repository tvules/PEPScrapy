import csv
from datetime import datetime

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.item import Item
from scrapy.spiders import Spider

from pep_parse.settings import BASE_DIR


class PepParsePipeline:
    expected_keys = ("number", "name", "status")
    fieldnames = ("статус", "количество")
    filename = "status_summary"

    def open_spider(self, spider: Spider) -> None:
        self.stats = spider.crawler.stats
        self.statuses = {}

    def process_item(self, item: Item, spider: Spider) -> Item:
        adapter = ItemAdapter(item)
        for key in self.expected_keys:
            if adapter.get(key) is None:
                raise DropItem(
                    f"Отсутствует значение ключа `{key}`: item={item}"
                )
        status = adapter.get("status")
        self.statuses[status] = self.statuses.get(status, 0) + 1
        return item

    def close_spider(self, spider: Spider) -> None:
        self._set_total()
        time = self._get_start_time().strftime("%Y-%m-%dT%H-%M-%S")
        path = BASE_DIR / f"results/{self.filename}_{time}.csv"
        with open(path, mode="w", encoding="utf-8", newline="") as file:
            w = csv.DictWriter(file, fieldnames=self.fieldnames)
            w.writeheader()
            w.writerows(
                dict(zip(w.fieldnames, data)) for data in self.statuses.items()
            )

    def _set_total(self) -> None:
        self.statuses["Total"] = sum(self.statuses.values())

    def _get_start_time(self) -> datetime:
        return self.stats.get_value("start_time", datetime.utcnow())
