from cgitb import text
from bs4 import BeautifulSoup
import requests
import re


search_item = input("What item do you want to search for? ")
search_item = re.sub("\s","+",search_item)

urlNewegg = f"https://www.newegg.com/p/pl?d={search_item}&N=4131"
pageNewegg = requests.get(urlNewegg).text
docNewegg = BeautifulSoup(pageNewegg,"html.parser")

pageNewegg_text = docNewegg.find(class_="list-tool-pagination-text").strong
pageNewegg_text= int(str(pageNewegg_text).split('/')[1].split('>')[1][:-1])

items_found = {}

for page in range(1,pageNewegg_text+1):
    url = f"https://www.newegg.com/p/pl?d={search_item}&N=4131&page={page}"
    page = requests.get(url).text
    doc  = BeautifulSoup(page,"html.parser")

    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    items = div.find_all(text=re.compile(search_item))
    for item in items:
        parent = item.parent
        if parent.name !="a":
            continue
        link = parent['href']
        parent2 = parent.parent.parent
        try:
            price = parent2.find(class_="price-current").strong.string
        except:
            pass
        items_found[item]={"price":int(price.replace(",","")),"link":link}


sorted_items = sorted(items_found.items(),key=lambda x: x[1]['price'])
for item in sorted_items:
    print(item[0])
    print(f"${item[1]['price']}")
    print(item[1]['link'])
    print("----------------------------------")