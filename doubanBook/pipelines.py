# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class DoubanbookPipeline(object):
    column = ['bookName','author']
    def open_spider(self,spider):
        self.f = open('book.csv','w',newline='')
        self.writer = csv.DictWriter(self.f,self.column)
        self.writer.writeheader()

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item

    def close_spider(self,spider):
        self.file.close()
