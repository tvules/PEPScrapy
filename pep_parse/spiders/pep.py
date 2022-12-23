import re
from typing import Generator

from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Spider

from pep_parse.items import PepParseItem


class PepSpider(Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    link_extractor = LinkExtractor(
        allow=r"pep-\d+$", restrict_css="#numerical-index"
    )

    def parse(self, response: Response, **kwargs) -> Generator:
        return response.follow_all(
            urls=self.link_extractor.extract_links(response),
            callback=self.parse_pep,
        )

    def parse_pep(self, response: Response, **kwargs) -> PepParseItem:
        matched = re.match(
            r"\w*\W*(?P<number>\d+)\W+(?P<name>.+)",
            "".join(response.css("#pep-content h1 ::text").getall()),
        )
        number, name = (
            matched.groups() if matched is not None else (None, None)
        )
        return PepParseItem(
            number=number,
            name=name,
            status=response.css('dt:contains("Status") + dd abbr::text').get(),
        )
