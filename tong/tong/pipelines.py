# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TongPipeline:
    def open_spider(self,spider):
        print('文件写入开始')
        self.file=open('gupiao.csv',mode='a',encoding='utf-8')
        pass
    def close_spider(self,spider):
        if self.file:
            self.file.close()
        print('文件写入结束')
        pass
    def process_item(self, item, spider):
        self.file.write(f'标题:{item['name']}\na股市值:{item['Aprice']}\n股票代码:{item['code']}股票概念数量:{item['gainum']}\n股票最新价:{item['newprice']}股票最新涨跌幅:{item['zhangfu']}\n股票概念{item['concept']}\n')
        return item
