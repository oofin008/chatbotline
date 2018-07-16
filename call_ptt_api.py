﻿from ptt_api import cleanhtml
from zeep import Client
from lxml import etree
import json
import requests
client_api = Client('http://www.pttplc.com/webservice/pttinfo.asmx?WSDL')
result = client_api.service.CurrentOilPrice("en")

#print(result)
#print(type(result))
replyQueue = list()
replyQueue.append(result)
#print(replyQueue[:])

Data = etree.fromstring(result)
mylist = cleanhtml(result)
mylist = mylist.split()
print(type(result))
print(type(mylist))
print(type(Data))
print(mylist)
mylist2 = list()
for Oil in Data.xpath('DataAccess'):
    product_name = Oil.xpath('PRODUCT/text()')[0]
    product_price = Oil.xpath('PRICE/text()') or [0]
    print(product_name, float(product_price[0]),'Baht')

#เหลือjoin ptt_list , replyQueue