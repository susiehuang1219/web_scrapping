# -*- coding: utf-8 -*-

import scrapy
from scrapy.item import Item,Field


class RentalPricingProjectItem(Item):
    link = Field()
    price = Field()
    google_map_link = Field()
    size = Field()
    pass