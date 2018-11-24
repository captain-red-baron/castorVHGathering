from scraper.abstract_scraper import Scraper


class HtmlScraper(Scraper):

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def scrape_keyword(self, keyword: str, target: str) -> [str]:
        return []
