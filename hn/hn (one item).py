import httpx
from selectolax.parser import HTMLParser
from bs4 import BeautifulSoup


response = "https://www.harveynorman.com.sg/index.php?subcats=Y&status=A&pshort=N&pfull=N&pname=Y&pkeywords=Y&search_performed=Y&q=iphone+14&dispatch=products.search"
name_selector = "div.product-info"
price_selector = "span.price"


def get_data(url,name_selector,price_selector,):
    resp = httpx.get(
        url,
        headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
        }
    )
    html = HTMLParser(resp.text)
    #GET NAME & PRICE
    name = html.css_first(name_selector).text().strip()
    price = html.css_first(price_selector).text().strip()
    #GET LINK
    soup = BeautifulSoup(resp, 'html.parser')
    # Find the first anchor tag with class="product-item-link"
    product_link = soup.find('a', {'class': 'btn btn-action btn_sm'})
    # Extract the href attribute value
    link = product_link['href']
    return {'name ': name,'price ' : price, 'link ': link}

print(get_data(response,name_selector,price_selector))