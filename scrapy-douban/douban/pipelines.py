# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import openpyxl


class DoubanPipeline(object):
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.sheet = self.wb.active
        self.sheet.title = '豆瓣图书TOP250短评第一页'
        self.sheet.append(['书名', '用户id', '短评'])

    def process_item(self, item, spider):
        line = [item['name'], item['user_id'], item['content']]
        self.sheet.append(line)
        return item

    def close_spider(self, spider):
        self.wb.save('./douban.xlsx')
        self.wb.close()

