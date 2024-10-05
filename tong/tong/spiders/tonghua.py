import json

import scrapy
from tong.settings import cookies,data
from tong.items import TongItem


class TonghuaSpider(scrapy.Spider):
    name = "tonghua"
    allowed_domains = ["iwencai.com"]
    start_urls = ["https://www.iwencai.com/gateway/urp/v7/landing/getDataList"]

    def start_requests(self):
        for num in range(1,4):
            data['page'] = str(num)
            yield scrapy.FormRequest(
                url=self.start_urls[0],
                cookies=cookies,
                formdata=data,
                callback=self.parse
            )

    def parse(self, response):
        response = response.text
        json_data = json.loads(response)
        datas = json_data['answer']['components'][0]['data']['datas']
        for data in datas:
            item = TongItem()
            title = data.get('股票简称')
            Aprice = data.get('a股市值(不含限售股)[20240930]')
            code = data.get('code')
            gainum = data.get('所属概念数量')
            newprice = data.get('最新价')
            zhangfu = data.get('最新涨跌幅')
            concept = data.get('概念解析')
            item['name'] = title
            item['Aprice'] = Aprice
            item['code'] = code
            item['gainum'] = gainum
            item['newprice'] = newprice
            item['zhangfu'] = zhangfu
            item['concept'] = concept

            yield item
            # print(f'标题:{title}\na股市值:{Aprice}\n股票代码:{code}股票概念数量:{gainum}\n股票最新价:{newprice}股票最新涨跌幅:{zhangfu}\n股票概念{concept}\n')

