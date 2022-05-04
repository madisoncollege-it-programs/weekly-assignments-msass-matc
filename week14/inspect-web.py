#!/usr/bin/env python3

import requests, bs4

res = requests.get('https://notpurple.com')
res.raise_for_status()

try:
    myHTML = bs4.BeautifulSoup(res.text,features="html.parser")     
    print(myHTML.title)
    links = myHTML.select('a')
    print(links)

except Exception as exc:

    print("Something went wrong! Error {exc}")