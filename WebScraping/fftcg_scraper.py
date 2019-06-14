"""
Author : @bminor21

Disclaimer: By using this web scraper you assume all legal responsibility.
"""
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import requests


class PriceScraper:
    """
        Singleton class.
        Scrapes TCGPlayer.com for cards and saves the market price
    """

    init_date = None

    _instance = None

    url = "https://shop.tcgplayer.com/final-fantasy-tcg/product/show?advancedSearch=true&Price_" \
          "Condition=Less+Than&Language=English&newSearch=false&orientation=list&PageNumber="

    header = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}

    card_dict = dict()

    # Only one instance
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(PriceScraper)
        return cls._instance

    def __init__(self):
        self.__scrapeprices()

    def __scrapeprices(self):
        print("Scraping...")
        pageNumber = 1
        _dict = dict()

        while True:
            r = requests.get(self.url + str(pageNumber), headers=self.header)
            soup = BeautifulSoup(r.content, 'html.parser')
            cards = soup.find_all("div", {"class": "product"})

            if len(cards) == 0:
                break

            for card in cards:
                number = ""

                for epf in card.find_all("span", {"class": "product__extended-field"}):
                    if epf is not None and "Number" in epf.text:
                        number = epf.text.replace("Number ", "")
                        break

                try:
                    price = card.find("dl", {"class": "product__market-price"}).find("dd").text
                except:
                    price = ""

                _dict[number] = price

            pageNumber += 1

        if len(self.card_dict) > 0:
            del self.card_dict

        self.card_dict = _dict
        self.init_date = datetime.now()
        print("Done scraping.")

    def update_prices(self) -> None:
        """
        check to see if we haven't updated the price today
        :return: None
        """
        if self.__validate():
            self.__scrapeprices()

    def __validate(self) -> bool:
        """
        If we haven't updated today or don't have any fresh data, do the update
        :return: bool
        """
        if self.init_date is None:
            return True
        return datetime.now() >= (self.init_date + timedelta(days=1))

    def get_price(self, number: str) -> str:
        """
            Gets a price of the card from the dictionary.
            @param, Card number (ex: 4-066R)
        """
        if number not in self.card_dict:
            return "Unknown Card"
        return self.card_dict[number]