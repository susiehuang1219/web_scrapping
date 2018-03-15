# -*- coding: utf-8 -*-

# Reference: http://doc.scrapy.org/en/latest/topics/settings.html

BOT_NAME = 'rental_pricing_project'

SPIDER_MODULES = ['rental_pricing_project.spiders']
NEWSPIDER_MODULE = 'rental_pricing_project.spiders'

ITEM_PIPELINES = ['rental_pricing_project.pipelines.MongoDBPipeline', ]

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017  # open port
MONGODB_DB = "rental_pricing"
MONGODB_COLLECTION = "partial_links"

DOWNLOAD_DELAY = 20
