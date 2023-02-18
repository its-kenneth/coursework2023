import httpx
from selectolax.parser import HTMLParser
from bs4 import BeautifulSoup


response = "https://www.bestdenki.com.sg/it-mobile/apple/iphone.html"
name_selector = "div.webmodeldescription"
price_selector = "span.price"
link_selector = "a.product-item-link"


def get_data(url,name_selector,price_selector,link_selector):
    resp = httpx.get(
        url,
        headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
        }
    )
    html = HTMLParser(resp.text)
    name = html.css_first(name_selector).text().strip()
    price = html.css_first(price_selector).text().strip()
    code_link = html.css_first(link_selector).text().strip()
    soup = BeautifulSoup(f"<a {code_link}>link text</a>", 'html.parser')
    link = soup.a['href']
    return link
    #return {'name ': name,'price ' : price,'link ': link}

print(get_data(response,name_selector,price_selector,link_selector))