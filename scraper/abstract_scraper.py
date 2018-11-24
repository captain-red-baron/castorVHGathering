from abc import ABC, abstractmethod


class Scraper(ABC):
    """
    This is an abstract scraper class, being inherited by the respective implementations.
    """

    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def scrape_keyword(self, keyword: str, target: str) -> [str]:
        """
        Scrapes a keyword in a target.
        :param keyword: The keyword to scrape.
        :param target: The target, where to search the keyword in (PDF, HTML)
        :return: A List of paragraphs where the keyword is included.
        """
        pass
