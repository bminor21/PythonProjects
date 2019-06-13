import requests
import pandas
from bs4 import BeautifulSoup

url = "https://shop.tcgplayer.com/final-fantasy-tcg/product/show?advancedSearch=true&Price_" \
      "Condition=Less+Than&Language=English&newSearch=false&orientation=list&PageNumber="

card_list = []
i = 1

while True:
    print("Page : " + str(i))
    r = requests.get(url + str(i),
                     headers={
                         'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    soup = BeautifulSoup(r.content, 'html.parser')
    cards = soup.find_all("div", {"class": "product__card"})

    if len(cards) == 0:
        break

    dict = {}
    for card in cards:
        dict["Name"] = card.find("a", {"class": "product__name"}).text

        for epf in card.find_all("span", {"class": "product__extended-field"}):
            if epf is None:
                continue
            if "Number" in epf.text:
                dict["Number"] = epf.text.replace("Number ", "")
                break

        dict["Price"] = card.find("dl", {"class": "product__market-price"}).find("dd").text

    card_list.append(dict)
    i += 1

df = pandas.DataFrame(card_list)
df.to_csv("FFTCG.csv")