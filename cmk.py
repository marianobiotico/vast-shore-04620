from lxml import html
import requests
import jinja2
import os

#Sitio:
page = requests.get('https://coinmarketcap.com/currencies/bitcoin/')
text = html.fromstring(page.content)
#MarketCap:
marketcap = text.xpath('/html/body/div/div[1]/div[2]/div[1]/div[2]/div[4]/div[2]/div/table/tbody/tr[4]/td/text()')
#Variacion:
variacion = text.xpath('/html/body/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/div[2]/span[2]/text()')
#Precio:
precio = text.xpath('/html/body/div/div[1]/div[2]/div[1]/div[2]/div[4]/div[2]/div/table/tbody/tr[1]/td/text()')


print(precio)