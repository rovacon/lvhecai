# -*- coding: utf-8 -*-

# Scrapy settings for lvhecai project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'lvhecai'

SPIDER_MODULES = ['lvhecai.spiders']
NEWSPIDER_MODULE = 'lvhecai.spiders'

DEPTH_LIMIT = 3
DOWNLOAD_TIMEOUT = 60
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lvhecai (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19'
