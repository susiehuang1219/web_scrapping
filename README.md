# Bay Area Rental Pricing Search Project

A python crawler and pipeline to scrape Craigslist's rental apt listings in the Bay Area, store items in MongoDB and export structured data as csv

## items.py: 
Use the Item class in Scrapy to return the web page extracted data as Python dicts

## MongoPipeline.py
After an item has been scraped by a spider, it is sent to the Item Pipeline and stored in MongoDB

## settings.py
Customize the behaviour of all Scrapy components


## listing_page_spider.py 
Scrape page contents for urls on listing pages

##rental_pricing_spider.py
Parse link, price, size and location from page contents

## export_as_csv.py
Export data as csv from MongoDB