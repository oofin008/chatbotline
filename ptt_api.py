from zeep import Client
from lxml import etree

client_api = Client('http://www.pttplc.com/webservice/pttinfo.asmx?WSDL')
result = client_api.service.CurrentOilPrice("en")

Data = etree.fromstring(result)

for Oil in Data.xpath('DataAccess'):
    product_name = Oil.xpath('PRODUCT/text()')[0]
    product_price = Oil.xpath('PRICE/text()') or [0]
    print(product_name, float(product_price[0]),'Baht')
    print(type(product_name))
