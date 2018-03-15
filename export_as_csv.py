import csv
from pymongo import MongoClient

client = MongoClient()
db = client.rental_pricing
myquery = db.partial_links.find() 
output = csv.writer(open('bay_area_rental_pricing_output.csv', 'wt')) 

for items in myquery[0:]: 
    try:
        zip = items['zip_code'] # collections are importent as dictionary and I am making them as list
        price = items['price']
        size = items['size']
        result = list()
        if zip != 'United States':
            if zip[0]=='9':
                print zip
                result.append(zip.encode('utf-8', 'ignore')) #encoding
                result.append(price.encode('utf-8', 'ignore'))
                result.append(size.encode('utf-8', 'ignore'))
        # else:
        #     result.append("none")
    except KeyError:
        print 'no zip code'
        # result = list()
        # result.append('no_zip_code_yet'.encode('utf-8','ignore'))
    if len(result) > 2:
        output.writerow(result)