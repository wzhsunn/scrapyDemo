from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
import time
from sciencedirect.items import JournalItem, VolumeItem
from scrapy.item import Item
from selenium import webdriver

class JournalSpider(Spider):
    name = "journal"
    allowed_domains = ["sciencedirect.com"]

    start_urls = ["http://www.sciencedirect.com/science/journal/01559982/38"]
        
    def parse(self, response):
        sel = Selector(response)
        volumes = sel.xpath("//div[@class='contentBorders']/div/table/tr")
        print volumes
        mainUrl = "http://www.sciencedirect.com/"
        cn = 0
        items = []
        for volume in volumes:
            name = volume.xpath('td/div/a/text()').extract()
            href = volume.xpath('td/div/a/@href').extract()
            if len(href) > 0:
                fullHref = mainUrl + href[0]
                print name, fullHref
                item = JournalItem()
                item['name'] = name
##                item['href'] = href

##                items.append(item)
                yield item
                yield Request(fullHref, callback=self.parse_articles)
               
                cn = cn + 1
                if cn > 2:
                    break
##        yield items
                
    def parse_articles(self, response):
        sel = Selector(response)
        articles = sel.xpath("//div[@id='bodyMainResults']")
        print articles
        cn = 0
        items = []
        for article in articles:
            hrefs = article.xpath('table/tr/td/h3/a/@href').extract()
            print hrefs
            for href in hrefs:
                item = ArticleItem()
##                yield Request(href, callback=self.parse_article)
                item["href"] = href
                yield item
                print href
                cn = cn + 1
                if cn > 2:
                    break

    def parse_article(self, response):
        driver = webdriver.Firefox()
        driver.get(response.url)
        title = driver.find_element_by_xpath("//h1").text
##        item = TitleItem()
##        item['title'] = title
        print title 
        driver.close()    
