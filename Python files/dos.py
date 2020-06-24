import requests
site=str(input(">"))
req=requests.get(site)

while True:
    print("Dos attack going on...")
    req