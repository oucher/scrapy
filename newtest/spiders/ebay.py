# -*- coding: utf-8 -*-
import scrapy
from newtest.items import DailiIpsItem, CpItem, AvItem


class Test1Spider(scrapy.Spider):
    name = 'ebay'
    allowed_domains = ['www.ebay.com']
    start_urls = ['https://ebay.com/']

    c_Down_Cp = {}

    custom_settings = {
        "DOWNLOAD_DELAY": 3,
        # The download delay setting will honor only one of:
        "CONCURRENT_REQUESTS": 1,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 1,
        "RETRY_TIMES": 1,
        "COOKIES_ENABLED":True,
        "COOKIES_DEBUG":True
    }

    def start_requests(self):
        import json
        #catenames,titles = json.loads("getcate.txt")
        #print catenames,titles,2222222222222
        with open("getcate.txt","r") as f:
            #alldata = f.read()
            #print f.read(),3333444444444444
            catenames, titles = json.loads(f.read())
            #print catenames, titles, 2222222222222
        # for catename in catenames:
        #     yield scrapy.Request("https://www.ebay.com/sch/i.html?_nkw=%s&rt=nc"%catename)

        for title in titles:
            yield scrapy.Request("https://www.ebay.com/sch/i.html?_nkw=%s&rt=nc" % title)

    c_Index = 0
    def parse(self, response):
        import json,jsonlines
        self.c_Index+=1
        url = response.request.url
        alldata = []
        for block in response.css("div.default").xpath("div"):
            alldata.append([
                block.xpath("a/@href").extract_first(),
                block.xpath("span/text()").extract_first(),
            ])
        #hrefs = response.css("div.default").xpath("div/a/@href").extract()
        #cnt = response.css("div.default").xpath("div/span/text()").extract()

        data  =[url,alldata]
        with open("result/%s.txt"%self.c_Index,"w") as f:
            f.write(json.dumps(data,indent=4))

        #file = jsonlines.open("main.json","a")
        #file.write(data)