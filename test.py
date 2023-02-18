import requests
response = ""
search_item = input("Search an item: ")
best_instant = "https://www.bestdenki.com.sg/instantsearch/result/?q={}".format(search_item) 
response = requests.get(best_instant)
print(response.url)
