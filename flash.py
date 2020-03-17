from requests import get
url = "https://www.flipkart.com/poco-x2-atlantis-blue-64-gb/p/itmbe7b58e0378b8?pid=MOBFZGJ6ZGMD7GEZ&lid=LSTMOBFZGJ6ZGMD7GEZAOQLPQ&marketplace=FLIPKART&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_0_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_0_6_na_na_na&fm=SEARCH&iid=7c67262f-1cc3-4b01-97ea-bf01225e1c8a.MOBFZGJ6ZGMD7GEZ.SEARCH&ppt=sp&ppn=sp&ssid=8fnjep2t740000001584457474420&qH=9b046b567ecc0251"
response = get(url)
print(response.text[:500])