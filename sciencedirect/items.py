# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class SciencedirectItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass
    
class JournalItem(Item):
    name = Field()
    volume = []

class VolumeItem(Item):
    name = Field()
    issues = []

class IssueItem(Item):
    name = Field()
    articles = []

class ArticleItem(Item):
    title = Field()
    authors = Field()
    abstract = Field()
    keywords = Field()
    
