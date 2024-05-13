import json

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from farfetch_scraper.items import FarfetchScraperItem


class FarfetchSpider(CrawlSpider):
    name = 'farfetch'
    allowed_domains = ['www.farfetch.com']
    start_urls = ['https://www.farfetch.com/ca/shopping/women/dresses-1/items.aspx']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//li[@data-testid="productCard"]/div/a[@data-component="ProductCardLink"]'),
             callback='parse', follow=True, process_links='process_links'),
        Rule(LinkExtractor(restrict_xpaths='//div[@data-testid="pagination-section"]/div/a[@data-testid="page-next"]')),
    )

    def process_links(self, links):
        return links[:1]

    def parse(self, response):
        item = FarfetchScraperItem()

        data_json = json.loads(response.xpath('//main/script/text()').get())

        item["id"] = data_json.get("productID")

        item["item_group_id"] = response.xpath('//p[contains(text(), "Brand style ID:")]/span[@data-component="Body"]/text()').get()

        item["mpn"] = item["item_group_id"]

        item["gtin"] = None

        item["brand"] = response.xpath('//h1/a[@data-component="LinkGhostDark"]/text()').get()

        item["description"] = response.xpath('//div/a[@data-component="HeadingBold"]/following-sibling::p[1]/text()').get()

        item["title"] = item["brand"] + " " + item["description"]

        # item["image_link"] = response.xpath('//div[1]/button[@data-component="Container"]/img/@src').get()
        # item["additional_image_link"] = response.xpath('//div[2]/button[@data-component="Container"]/img/@src').get()

        item["image_link"] = data_json.get("image")[0].get("contentUrl")
        item["additional_image_link"] = data_json.get("image")[1].get("contentUrl")

        item["link"] = response.url

        item["color"] = data_json.get("color")

        item["size"] = response.xpath('//div/h4[@data-component="BodyBold" and text()="Wearing"]/following-sibling::p[1]/text()').get()

        availability = data_json.get("offers", {}).get("availability")
        if availability == "https://schema.org/InStock":
            item["availability"] = True
        else:
            item["availability"] = False

        item["price"] = response.xpath('//div[@data-component="PriceCallout"]/p[@data-component="PriceLarge"]/text()').get()

        condition = data_json.get("offers", {}).get("itemCondition")
        if condition == "https://schema.org/NewCondition":
            item["condition"] = "New"
        else:
            item["condition"] = "Not New"

        product_type = response.xpath('//ol[@data-component="Breadcrumbs"]/li[@data-component="BreadcrumbWrapper"]/a/text()').getall()
        item["product_type"] = ">".join(product_type)
        item["gender"] = product_type[0]

        if item["gender"] == "Kids Home":
            item["age_group"] = "Kids"
        else:
            item["age_group"] = "Adults"

        item["google_product_category"] = "2271"
        yield item
