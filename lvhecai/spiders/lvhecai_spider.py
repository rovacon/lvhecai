# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import Selector 
from lvhecai.items import LvhecaiItem
from scrapy.utils.response import get_base_url
import scrapy,re
import urllib,urlparse

class MindhacksSpider(BaseSpider):
    name = "lvhecai"
    #domain_name = ""
    #start_urls = ["http://zl77.txy7.us/"]
    #打开site文件作为开始url
    start_urls=[]
    with open('site','r') as f:
        for line in f.readlines():
                start_urls.append('http://'+line.strip())
    lvhecai_keys=[u'中特',u'六合',u'马会',u'玛会',u'一玛',u'一码',u'特码',u'特玛',u'天下彩',u'曾道人',u'白小姐',]
    login_keys=[u'登录',u'注册','login',u'登陆']
    lvhecaihost=[]
    loginhost=[]
    spideredurl=[]

    #搜索关键字的函数
    def myre(self,response,key_list):
    	date=Selector(response)
    	for key in key_list:
    		#llprint key
    		if date.re(key):
    			return 1
    	return 0

    def parse(self, response):
    	#print "#################"
    	base_url = get_base_url(response)
    	page_url=response.url
    	host=urlparse.urlparse(page_url)[1]
    	#print "request url:"+page_url
        #判断是否六合彩网站
    	if self.myre(response,self.lvhecai_keys):
    	#if self.myre(response,self.lvhecai_keys) and Selector(response).re('<xml>|<wml>'):
        #if Selector(response).re('<xml>|<wml>'):
                #判断是否登录网站
    		if self.myre(response,self.login_keys):
                        #判断是否已记录在登录域名
    			#print page_url+":六合彩已记录"
                        if host in self.loginhost:
				pass
    			else:
    				log1=open('login.txt','a')
    				log1.write(page_url+"\n")
    				log1.close()
    				self.loginhost.append(host)
    			if host in self.lvhecaihost:
                        	self.lvhecaihost.remove(host)
		#是六合彩网站不是登录网站
    		else:	
			#判断是否在已记录的登录网站或者六合彩网站，如果记录就不重复
                        #print page_url+":尼马，明显的六合彩网站"
	    		if host not in self.lvhecaihost or host not in self.loginhost:
	    			log2=open('lvhecai.txt','a')
	    			log2.write(page_url+"\n")
	    			log2.close()
	    			self.lvhecaihost.append(host)
			#分析所有a标签
		    	link=response.xpath('//a')
		    	items=[]
		    	if link:
		    		for a in link:
					#抽取连接
		    			links=a.select('@href').extract()
		    			if len(links)>0 :
		    				relative_url =links[0]
		    				url=urlparse.urljoin(base_url, relative_url) 
						#print "url:"+url
		    				query=urlparse.urlparse(url)[4]
		    				path=urllib.splitquery(url)[0]
		    				sorturl=""
						#用base_url加上query的key作为url记录，防止同类型的模版爬太多
		    				if query:
		    					querylist=query.split('&')
							querylist.sort()
		    					sorturl=path+"?"
		    					for key_value in querylist:
		    						sorturl+=urllib.splitvalue(key_value)[0]
		    				elif re.match(".*[0-9]+\.htm$|.*[0-9]+\.asp$|.*[0-9]+\.wml$",url):
							sorturl=url.rsplit('/',1)[0]
						else:
		    					sorturl=url
		    				#if sorturl not in self.spideredurl and urllib.splittype(url)[0]=='http':
		    				if sorturl not in self.spideredurl:
		    					#print "spider:"+url
		    					#yield scrapy.Request(url, callback=self.parse)
		    					self.spideredurl.append(sorturl)
							self.spideredurl.sort()
		    				#print a.select('text()').extract() [0]
						#else:
						#	print "not spider:"+url
						#	print self.spideredurl
		    	#print link
		    	#print items
		    	#print "*********************"
		    	#print self.spideredurl
	else:
		log3=open('no.txt','a')
		log3.write(page_url+"\n")
		log3.close()
                #print page_url+"not_lvhecai"

