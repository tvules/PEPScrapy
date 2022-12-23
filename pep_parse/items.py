from scrapy.item import Item, Field


class PepParseItem(Item):
    number = Field()
    name = Field()
    status = Field()
