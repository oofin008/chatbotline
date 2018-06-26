from zeep import Client
from lxml import etree
import json
import re

#get rid of html tag from data
def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

client_api = Client('http://www.pttplc.com/webservice/pttinfo.asmx?WSDL')
result = client_api.service.CurrentOilPrice("en")
#print(result)
#print(type(result))
Data = etree.fromstring(result)
mylist = cleanhtml(result)
mylist = mylist.split()
print(type(mylist))
print(type(Data))
print(mylist)
for Oil in Data.xpath('DataAccess'):
    product_name = Oil.xpath('PRODUCT/text()')[0]
    product_price = Oil.xpath('PRICE/text()') or [0]
    print(product_name, float(product_price[0]),'Baht')

