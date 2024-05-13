# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FarfetchScraperItem(scrapy.Item):
    id = scrapy.Field()
    item_group_id = scrapy.Field()
    mpn = scrapy.Field()
    gtin = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    image_link = scrapy.Field()
    additional_image_link = scrapy.Field()
    link = scrapy.Field()
    gender = scrapy.Field()
    age_group = scrapy.Field()
    brand = scrapy.Field()
    color = scrapy.Field()
    size = scrapy.Field()
    availability = scrapy.Field()
    price = scrapy.Field()
    condition = scrapy.Field()
    product_type = scrapy.Field()
    google_product_category = scrapy.Field()
