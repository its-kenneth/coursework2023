import requests
import httpx
from selectolax.parser import HTMLParser
from bs4 import BeautifulSoup

response = ""
#search_item = input("Search an item: ")
norman_list = []

def get_data(search_item):
    norman_link = "https://www.harveynorman.com.sg/index.php?subcats=Y&status=A&pshort=N&pfull=N&pname=Y&pkeywords=Y&search_performed=Y&q={}+14&dispatch=products.search".format(search_item) #generate generic link
    #response = requests.get(best_instant) #get redirected link
    #response = response.url #url
    name_selector = "div.product-info"
    price_selector = "span.price"
    resp = httpx.get(
        norman_link,
        headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
        }
    )
    html = HTMLParser(resp.text)
    #GET NAME & PRICE
    name_list = html.css(name_selector)
    price_list = html.css(price_selector)
    #GET LINK
    #HTML PARSER
    soup = BeautifulSoup(resp, 'html.parser')
    # Find the first image link that has the class="product-item-link"
    link_list = soup.find_all(('a'), {'class': "product-img"})
    #print(link_list)
    limit = 5
    for x in link_list:
        if limit > 0:
            name = name_list[(5-limit)].text().strip()
            price = price_list[(5-limit)].text().strip()
            limit -= 1
            link = (x['href'])
            norman_list.append( {'name ': name,'price ' : price.replace('S',''),'link ': link,})
        else: 
            break
    return norman_list
cheapest_info = []
def get_cheapest(search_item):
    all = get_data(search_item)
    cheapest_item = all[0]
    for z in all:
        price = float(z['price '].replace('$', '').replace(',',''))
        cheapest_price = float(cheapest_item['price '].replace('$', '').replace(',',''))
        if price < cheapest_price:
            cheapest_item = z
    cheapest_info.append(cheapest_item['name '])
    cheapest_info.append(float(cheapest_price))
    cheapest_info.append(cheapest_item['link '])
    return cheapest_info

print(get_cheapest("TV"))

