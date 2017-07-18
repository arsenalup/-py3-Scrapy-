# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WeatherPipeline(object):
    def __init__(self):
        self.file = open('wea.txt', 'w+')
    def process_item(self, item, spider):
        city = item['city'][0]
        self.file.write('city:' + str(city) +'\n\n')

        date = item['data']
        desc = item['dayDesc']
        #夜间白天
        dayDesc = desc[1::2]
        nightDesc = desc[0::2]
        dayTemp = item['dayTemp']

        weaitem = list(zip(date, dayDesc, nightDesc, dayTemp))
        weaitem_len = sum(1 for _ in weaitem)

        for i in range(weaitem_len):
            item = weaitem[i]
            d = item[0]
            dd = item[1]
            nd = item[2]
            ta = item[3].split('/')
            dt = ta[0]
            try:
                nt = ta[1]
            except:
                nt = '0'
            txt = 'data:{0}\t\t day:{1}({2})\t\tnight:{3}({4})\n\n'.format(
                d,
                dd,
                dt,
                nd,
                nt,
            )
            self.file.write(txt)

        return item
