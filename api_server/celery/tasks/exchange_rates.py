
import json
import xmljson
import requests
from celery.decorators import task
from lxml.html import fromstring
import xml.etree.ElementTree as ET
from api_server.models.exchange import ExchangeRates

@task()
def get_exchange_rates():
    
    data_xml = requests.get('http://88.208.6.228/cgi/mcrate.cgi')
    print(data_xml)
    json_data = json.dumps(xmljson.badgerfish.data(fromstring(data_xml.content)))
    
    json_data = json.loads(json_data)
   
    rates = ExchangeRates.objects.all()
    existing_rate = {c['@symbol'] for c in json_data['result']['currency']}
    
    for r in json_data['result']['currency']:
        ExchangeRates.objects.update_or_create(symbol=r['@symbol'], rate=r["@rate"], )
                                                
                                                
    for i in rates:
        if i.rate not in existing_rate:
            i.is_deleted = True
            i.save()
            