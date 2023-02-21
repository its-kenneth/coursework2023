import requests
import httpx
import random 
from selectolax.parser import HTMLParser
from bs4 import BeautifulSoup
#search_item = input("Search an item: ")

def get_norman(search_item):    
    response = ""
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
    link_list = (soup.find_all('a', {'class': 'btn btn-action btn_sm'}))
    if min(len(link_list),len(name_list),len(price_list)) > 5:
        limit = 5
    else: 
        limit = min(len(link_list),len(name_list),len(price_list))
    norman_list = []
    if limit > 0:
        for x in link_list:
            if limit > 0:
                name = name_list[(5-limit)].text().strip()
                price = price_list[(5-limit)].text().strip()
                limit -= 1
                link = (x['href']).replace('//www','www').replace("www.","https://www.")
                norman_list.append( {'name ': name,'price ' : price.replace('S',''),'link ': link,})
            else: 
                break
    elif limit == 0:
        norman_list = []    
    return norman_list

#search_item = input("Search an item: ")
def get_denki(search_item):
    response = ""
    best_instant = "https://www.bestdenki.com.sg/instantsearch/result/?q={}".format(search_item) #generate generic link
    response = requests.get(best_instant) #get redirected link
    response = response.url #url
    name_selector = "div.webmodeldescription" 
    price_selector = "span.price"
    resp = httpx.get(
        response,
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
    link_list = (soup.find_all('a', {'class': 'product-item-link'}))
    if min(len(link_list),len(name_list),len(price_list)) > 5:
        limit = 5
    else: 
        limit = min(len(link_list),len(name_list),len(price_list))
    denki_list = []
    if limit > 0:
        for x in link_list:
            if limit > 0:
                name = name_list[(5-limit)].text().strip()
                price = price_list[(5-limit)].text().strip()
                limit -= 1
                link = (x['href']).replace('//www','www')
                denki_list.append( {'name ': name,'price ' : price.replace('S',''),'link ': link,})
            else: 
                break
    elif limit == 0:
        denki_list = []  
    return denki_list

cheapest_info = []
def get_cheapest(search_item):
    all = get_norman(search_item) + get_denki(search_item)
    cheapest_info = []
    #print(all)
    if len(all)>0:
        cheapest_item = all[random.randint(0,len(all)-1)]
        for z in all:
            price = float(z['price '].replace('$', '').replace(',',''))
            cheapest_price = float(cheapest_item['price '].replace('$', '').replace(',',''))
            if price < cheapest_price:
                cheapest_item = z
        cheapest_info.append(cheapest_item['name '])
        cheapest_info.append(float(cheapest_price))
        cheapest_info.append(cheapest_item['link '])
        return cheapest_info
    return "Please enter another item"

#print(get_cheapest("b"))
#print(get_cheapest("Air Conditioner"))
#print(get_cheapest("Samsung Galaxy"))
#print(get_cheapest("iPhone 14"))
#print(get_cheapest("TV"))