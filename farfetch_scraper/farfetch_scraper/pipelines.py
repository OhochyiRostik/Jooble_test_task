# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

import xml.etree.ElementTree as ET


class XMLPipeline:
    def open_spider(self, spider):
        self.items = []

    def close_spider(self, spider):
        channel = ET.Element("channel")
        description = ET.SubElement(channel, "description")
        description.text = "Farfetch UK"

        for parse_item in self.items:
            item = ET.SubElement(channel, "item")

            id = ET.SubElement(item, "id")
            id.text = parse_item['id']

            item_group_id = ET.SubElement(item, "item_group_id")
            item_group_id.text = parse_item['item_group_id']


            mpn = ET.SubElement(item, "mpn")
            mpn.text = parse_item['mpn']

            gtin = ET.SubElement(item, "gtin")
            gtin.text = parse_item['gtin']

            title = ET.SubElement(item, "title")
            title.text = parse_item['title']

            description = ET.SubElement(item, "description")
            description.text = parse_item['description']

            image_link = ET.SubElement(item, "image_link")
            image_link.text = parse_item['image_link']

            additional_image_link = ET.SubElement(item, "additional_image_link")
            additional_image_link.text = parse_item['additional_image_link']

            link = ET.SubElement(item, "link")
            link.text = parse_item['link']

            gender = ET.SubElement(item, "gender")
            gender.text = parse_item['gender']

            age_group = ET.SubElement(item, "age_group")
            age_group.text = parse_item['age_group']

            brand = ET.SubElement(item, "brand")
            brand.text = parse_item['brand']

            color = ET.SubElement(item, "color")
            color.text = parse_item['color']

            size = ET.SubElement(item, "size")
            size.text = parse_item['size']

            availability = ET.SubElement(item, "availability")
            availability.text = parse_item['availability']

            price = ET.SubElement(item, "price")
            price.text = parse_item['price']

            condition = ET.SubElement(item, "condition")
            condition.text = parse_item['condition']

            product_type = ET.SubElement(item, "product_type")
            product_type.text = parse_item['product_type']

            google_product_category = ET.SubElement(item, "google_product_category")
            google_product_category.text = parse_item['google_product_category']

        channel_link = ET.SubElement(channel, "link")
        channel_link.text = "https://www.farfetch.com/"
        channel_title = ET.SubElement(channel, "title")
        channel_title.text = "Farfetch"
        tree = ET.ElementTree(channel)

        tree.write("products.xml")

    def process_item(self, item, spider):
        self.items.append(item)
        return item

# class FarfetchScraperPipeline:
#     def process_item(self, item, spider):
#         return item
