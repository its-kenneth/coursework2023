import requests
import httpx
from selectolax.parser import HTMLParser
from bs4 import BeautifulSoup

def get_courts(search_item):
    courts_url = ("https://www.courts.com.sg/catalogsearch/result/?q={}".format(search_item))
    resp = requests.get(
        courts_url,
        headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
        }
    )
    name_selector = "a.product-item-link" 
    #price_selector = "span.price"
    html = HTMLParser(resp.text)
    name = html.css_first(name_selector)
    #price = html.css_first(price_selector)
    return name
    #print(html)



print(get_courts("iPhone 13"))