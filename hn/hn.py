import requests
from bs4 import BeautifulSoup

def scrape_harvey_norman(query):
    # Define the URL and query parameters for the search page
    url = 'https://www.harveynorman.com.sg/search?q=' + query
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    
    # Send a GET request to the search page with the query parameters and headers
    response = requests.get(url, headers=headers)
    
    # Parse the response content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all the product cards on the search results page
    product_cards = soup.find_all('div', class_='product-card')
    
    # Loop through each product card and extract the relevant information
    products = []
    for card in product_cards:
        # Extract the product name and link
        name = card.find('h5', class_='product-card__name').text.strip()
        link = card.find('a', class_='product-card__link')['href']
        
        # Extract the product price and convert it to a float
        price_str = card.find('span', class_='product-card__price').text.strip().replace(',', '')[1:]
        price = float(price_str)
        
        # Add the product information to the list of products
        products.append({'name': name, 'price': price, 'link': link})
    
    return products

results = scrape_harvey_norman('iPhone 13')
print(results)