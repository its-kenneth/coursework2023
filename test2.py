import httpx
from selectolax.parser import HTMLParser
from bs4 import BeautifulSoup
def get_link(url,selection):
    resp = httpx.get(
        "https://www.bestdenki.com.sg/it-mobile/apple/iphone.html",
    headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
        }
    )
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(resp, 'html.parser')

    # Find the first anchor tag with class="product-item-link"
    product_link = soup.find('a', {'class': 'product-item-link'})

    # Extract the href attribute value
    href_value = product_link['href']

    # Print the result
    return href_value

getlink("https://www.bestdenki.com.sg/it-mobile/apple/iphone.html",'a' {'class': 'product-item-link'})