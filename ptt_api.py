from zeep import Client
from lxml import etree
import json
import requests
from time import gmtime, strftime


def ptt_result_API():
    client_api = Client('http://www.pttplc.com/webservice/pttinfo.asmx?WSDL')
    result = client_api.service.CurrentOilPrice("en")
    Data = etree.fromstring(result)
    mystring = strftime("%Y-%m-%d %H:%M:%S", gmtime()) + '\n'
    mylist = list()
    for Oil in Data.xpath('DataAccess'):
        product_name = Oil.xpath('PRODUCT/text()')[0]
        product_price = Oil.xpath('PRICE/text()') or [0]
        if(product_price[0] != 0):
            mylist.append(product_name + '\n' + str(product_price.pop(0)) + ' baht \n')
            mystring += mylist[-1]
    return mystring

mystring = ptt_result_API()
print(mystring)
