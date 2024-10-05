# Scrapy settings for tong project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import execjs
import os

file_path = os.path.join(os.path.dirname(__file__), 'JS', 'huaCode.js')
BOT_NAME = "tong"

SPIDER_MODULES = ["tong.spiders"]
NEWSPIDER_MODULE = "tong.spiders"

with open(file_path,mode='r',encoding='utf-8') as file:
    jsFile = file.read()

ctx = execjs.compile(jsFile)
v = ctx.call('res')

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "tong (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
LOG_LEVEL = 'WARNING'

cookies = {
    'cid': '7eee3fc023932ceca9ea2aac30ddce9a1724331523',
    'other_uid': 'Ths_iwencai_Xuangu_ynt61dfcpswcq8wq2xahbi8qdvo8erp0',
    'ta_random_userid': 'd399ggu21i',
    'v': v,
}

data = {
    'query': '5g',
    'urp_sort_way': 'desc',
    'urp_sort_index': '最新涨跌幅',
    'page': '3',
    'perpage': '50',
    'condition': '[{"dateText":"","indexName":"所属概念","indexProperties":["包含5g","概念id 300843"],"ci":true,"source":"text2sql","type":"index","indexPropertiesMap":{"概念id":"300843","包含":"5g"},"reportType":"null","ciChunk":"5g","score":0.0,"createBy":"preCache","chunkedResult":"5g","uiText":"所属概念包含5g","valueType":"_所属概念","domain":"abs_股票领域","sonSize":0,"logid":"186d641f7d6a5b2bfcba99997aa845a5","dateList":[],"order":0}]',
    'logid': '186d641f7d6a5b2bfcba99997aa845a5',
    'ret': 'json_all',
    'sessionid': '186d641f7d6a5b2bfcba99997aa845a5',
    'source': 'Ths_iwencai_Xuangu',
    'date_range[0]': '20240921',
    'iwc_token': '0ac9511817269046698198222',
    'urp_use_sort': '1',
    'user_id': 'Ths_iwencai_Xuangu_ynt61dfcpswcq8wq2xahbi8qdvo8erp0',
    'uuids[0]': '24087',
    'query_type': 'stock',
    'comp_id': '6836372',
    'business_cat': 'soniu',
    'uuid': '24087',
}

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.iwencai.com',
    'Referer': 'https://www.iwencai.com/unifiedwap/result?w=5g&querytype=stock',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
    'hexin-v': 'A18Ms0AFRfjQWkHknSi1wsmm7rjsxKPszRy3JvGt-3ZVNHGm-ZRDtt3oR7IC',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "tong.middlewares.TongSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "tong.middlewares.TongDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "tong.pipelines.TongPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
