import httpx
from selectolax.parser import HTMLParser

#print(products)

#name ie3A+n bM+7UW Cve6sh
#special price: FD2XVZ
#OG price ZEgDH9
#image  _7DTxhh vc8g9F

def get_data(store,url,selector):
    resp = httpx.get(
        url,
        headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
        }
    )
    html = HTMLParser(resp.text)
    print(html)
    price = html.css_first(selector).text().strip()
    return {"store": store, "price": price }


def main():
    results = [
        get_data(
            "Amazon",
            "https://www.amazon.com/dp/B0BGQSV8JL/",
            "span.a-offscreen",
        ),
        get_data(
            "Lazada",
            "https://www.lazada.sg/products/apple-iphone-13-mini-i1987645595-s10763214559.html",
            "span.pdp-price.pdp-price_type_bold.pdp-price_color_orange.pdp-price_size_l",
        ),
    ]
    print(results)

main()

