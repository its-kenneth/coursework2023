'''Start of Kenneth's Code'''
import requests
import httpx
import random 
from selectolax.parser import HTMLParser
from bs4 import BeautifulSoup

import tkinter as tk
import webbrowser

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
    # Find the first image link that has the class="product-item-link" product-img btn btn-action btn_sm'
    link_list = []
    link_list = (soup.find_all('a', {'class': 'product-img'}))
    #print(link_list)
    if min(len(link_list),len(name_list),len(price_list)) > 5:
        initial_limit = 5
    else: 
        initial_limit = min(len(link_list),len(name_list),len(price_list))
    norman_list = []
    if initial_limit > 0:
        limit = initial_limit
        for x in link_list:
            if limit > 0:
                name = name_list[(initial_limit-limit)].text().strip()
                price = price_list[(initial_limit-limit)].text().strip()
                limit -= 1
                link = (x['href']).replace('//www','www').replace("www.","https://www.")
                norman_list.append( {'name ': name,'price ' : price.replace('S',''),'link ': link,})
            else: 
                break
    elif initial_limit == 0:
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
    #print(min(len(link_list),len(name_list),len(price_list)))
    if min(len(link_list),len(name_list),len(price_list)) > 5:
        initial_limit = 5
    else: 
        initial_limit = min(len(link_list),len(name_list),len(price_list))
    denki_list = []
    if initial_limit > 0:
        limit = initial_limit
        for x in link_list:
            if limit > 0:
                name = name_list[(initial_limit-limit)].text().strip()
                price = price_list[(initial_limit-limit)].text().strip()
                limit -= 1
                link = (x['href']).replace('//www','www')
                denki_list.append( {'name ': name,'price ' : price.replace('S',''),'link ': link,})
            else: 
                break
    elif initial_limit == 0:
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

'''End of Kenneth's Code'''

#print(get_cheapest("b"))
#print(get_cheapest("Air Conditioner"))
#print(get_cheapest("Samsung Galaxy"))
#print(get_cheapest("iPhone 14"))
#print(get_cheapest("TV"))



root = tk.Tk()
root.title("Product Finder")
input_label = tk.Label(text="Enter item to be bought:", fg="black", width=100)            
input_label.pack()

input_entry = tk.Entry(root)
input_entry.pack()
name = input_entry.get()



def button_click():
    name = input_entry.get()
    a = []
    if get_cheapest(name) != "Please enter another item":
        button.config(state="disabled", bg="gray")
        a = (get_cheapest(name))
        name_label = tk.Label(root, text=a[0], fg="black", width=100, height=5)
        name_label.pack()


        price_label = tk.Label(root, text="Price: $"+str(a[1]), fg="black", width=20, height=5)
        price_label.pack()
        
        def search_link():
            link = a[2]
            print("link: ",link)
            webbrowser.open_new_tab(link)

        button_2 = tk.Button(root, text="link", command=search_link, width=20, height = 3)
        button_2.pack()

        def delete_labels():
            for label in label_list:
                label.destroy()
            button.config(state="normal", bg="white")
            
        button_4 = tk.Button(root, text="Clear", command=delete_labels, width= 20, height= 3)
        button_4.pack()

        label_list = [name_label, price_label, button_2, button_4]


    else:
        window = tk.Tk()

        def delete_labels_2():
            window.destroy()

        button_3 = tk.Button(window, text="Try another input", command=delete_labels_2, width= 20, height= 3)
        button_3.pack()

        window.mainloop()

button = tk.Button(root, text="Search Item", command=button_click, width= 20, height= 3)
button.pack()    


root.mainloop()


