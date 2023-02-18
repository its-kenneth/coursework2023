import httpx
from selectolax.parser import HTMLParser

response = "https://www.bestdenki.com.sg/it-mobile/apple/iphone.html"
selector = "span.price"

def get_data(url,selector):
    resp = httpx.get(
        url,
        headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
        }
    )
    html = HTMLParser(resp.text)
    price = html.css_first(selector).text().strip()
    return price

    print(results)

print(get_data(response,selector))