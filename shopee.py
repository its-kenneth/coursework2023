item_name = input("")
import requests

url = "https://partner.shopeemobile.com/api/v2/product/search_item?access_token=access_token&attribute_status=2&item_name=apple&offset=0&page_size=10&partner_id=partner_id&shop_id=shop_id&sign=sign&timestamp=timestamp"

payload={}
headers = {

}
response = requests.request("GET",url,headers=headers, data=payload, allow_redirects=False)

print(response.text)