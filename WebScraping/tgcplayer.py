import requests
import pandas
from bs4 import BeautifulSoup

url = "https://shop.tcgplayer.com/final-fantasy-tcg/product/show?advancedSearch=true&Price_" \
      "Condition=Less+Than&Language=English&newSearch=false&orientation=list&PageNumber="

card_list = []
i = 1

while True:
    print("Parsing Page : " + str(i))
    r = requests.get(url + str(i),
                     headers={
                         'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    soup = BeautifulSoup(r.content, 'html.parser')
    cards = soup.find_all("div", {"class": "product"})

    if len(cards) == 0:
        break

    for card in cards:
        d = {}
        d["Name"] = card.find("a", {"class": "product__name"}).text

        for epf in card.find_all("span", {"class": "product__extended-field"}):
            if epf is not None and "Number" in epf.text:
                d["Number"] = epf.text.replace("Number ", "")
                break

        d["Price"] = card.find("dl", {"class": "product__market-price"}).find("dd").text
        card_list.append(d)
    i += 1

df = pandas.DataFrame(card_list)
df.to_csv("FFTCG.csv")