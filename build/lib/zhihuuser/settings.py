# -*- coding: utf-8 -*-

# Scrapy settings for zhihuuser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihuuser'

SPIDER_MODULES = ['zhihuuser.spiders']
NEWSPIDER_MODULE = 'zhihuuser.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'zhihu (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',
    'cookie': '_xsrf=lCpUiCUa0EEfTXd5iMe8y5luDY8PZfdD; _zap=b51bddef-cdf1-4059-a8da-d3b678477d74; d_c0="ACAnlgNiRQ6PTlGYT9pNyZRnYqQjeK-FB6g=|1537954373"; __utma=155987696.844627157.1537954474.1537954474.1537954474.1; __utmz=155987696.1537954474.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); l_cap_id="M2ZhN2JkMTgwMjU2NGMzZDljNDFjNzA2YTJiODk2ZjU=|1537955243|579afe0c643ec08d47f87b60f038b9bf699847c3"; r_cap_id="ZTVhMTk1ZmE4ZWQzNGFlYThlMmUxM2NmZDY1M2E4N2Y=|1537955243|044127f6a4f73eab30590dea56dc746e8236f6f6"; cap_id="YmJjZWFmNjY2YWU2NDc1ZTg5ZWU0NTYxMThlM2RlYTE=|1537955243|4a42adeced98c1893044db6f3a19d0a8b4f99f23"; q_c1=0ec71376d0cb4740ad0d864eccfe973d|1537955265000|1537955265000; tgw_l7_route=56f3b730f2eb8b75242a8095a22206f8; anc_cap_id=0523563056494919b3e725ec98c02413; capsion_ticket="2|1:0|10:1539169001|14:capsion_ticket|44:OTg4MjBmMWJmYTE1NDlkMGE4M2JlN2RjYmRkZTBjZGM=|df7122d15a3f57ec4f2ca2d5147f9af4e3db09ad0652636067cfbc86e6b78364',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'zhihuuser.middlewares.ZhihuSpiderMiddleware': 543,
# }

# SPIDER_MIDDLEWARES = {
#     'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'zhihuuser.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# DOWNLOADER_MIDDLEWARES = {
#     'scrapy_splash.SplashCookiesMiddleware': 723,
#     'scrapy_splash.SplashMiddleware': 725,
#     'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'zhihuuser.pipelines.MongoPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline':301,

}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
# HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

# SPLASH_URL = 'http://192.168.99.100:8050'

MONGO_URI = 'localhost'
MONGO_DATABASE = 'zhihu'

SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_QUEUE_CLASS='scrapy_redis.queue.SpiderPriorityQueue'
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

REDIS_URL =None
REDIS_HOST='127.0.0.1'
REDIS_PORT=6379
HTTPERROR_ALLOWED_CODES = [403]
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# SCHEDULER_FLUSH_ON_START = True
