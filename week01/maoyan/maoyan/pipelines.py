# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
import csv
class MaoyanPipeline(object):

    def __init__(self):
        store_file = os.path.dirname(__file__) + 'movies.csv'
        self.file = open(store_file, 'a+', encoding='utf8', newline='')
        self.writer = csv.writer(self.file,dialect='excel')

    def process_item(self, item, spider):
        #return item
        name = item['name']
        tag1 = item['tag1']
        tag2 = item['tag2']
        tag3 = item['tag3']
        time = item['time']
        #output = f'|{name}\t|{tag1}/{tag2}/{tag3}\t|{time}|\n\n'
        self.writer.writerow([name, tag1, tag2, tag3, time])
        # with open('./maoyanmovies.txt','a+', encoding='utf8', ) as article:
        #     article.write(output)
        return item

    def close_spider(self, spider):
        self.file.close()