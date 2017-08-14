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
        for catename in catenames:
            yield scrapy.Request("https://www.ebay.com/sch/i.html?_nkw=%s&rt=nc"%catename)

        for title in titles:
            yield scrapy.Request("https://www.ebay.com/sch/i.html?_nkw=%s&rt=nc" % title)
        # asdf
        # res = []
        # for i in range(1, 100):
        #     #url = 'http://gongying.99114.com/listing/%E5%A4%AA%E9%98%B3%E8%83%BD%20%E7%81%AD%E8%9A%8A%E7%81%AF_1_0_0_0_0_0_1-0-0-0-0_0_"+"%s.html' % i
        #     url = 'https://www.javbus.com/page/%s' % i
        #     print url, 444444
        #     req = scrapy.Request(url)
        #     # 存储所有对应地址的请求
        #     # res.append(req)
        #     yield req
        # return res

#     def parse_info_page(self, response):
#         item = CpItem()
#         item["linkman"] = response.xpath(
#             "//span[@class='p_rzR']/i/text()").extract_first()
#         try:
#             item["make"] = response.xpath(
#                 "//span[@class='p_rzR']/text()").extract()[4]
#         except:
#             pass
#         #tel = scrapy.Field()
#         info = response.xpath("//label[@class='encrypt']/text()").extract()
#         item["phone"] = info[0]
#
#         try:
#             item["tel"] = info[1]
#         except:
#             pass
#         #item["tel"] = info[1]
#         # response.xpath(
#         #    "//span[@class='phoneNumber']/label/text()").extract()
#  #       linkman = scrapy.Field()
#         item["name"] = response.xpath(
#             "//p[@class='companyname']/span/text()").extract_first().strip()
#         item["address"] = response.xpath(
#             "//span[@id='detialAddr']/text()").extract_first().strip()
#         if len(info) == 3:
#             try:
#                 item["mail"] = info[2]
#             except:
#                 pass
#         else:
#             try:
#                 item["mail"] = info[3]
#             except:
#                 pass
#         item["info"] = ",".join(info)
# #         except:
# #             from scrapy.shell import inspect_response
# #             inspect_response(response, self)
# #         make = scrapy.Field()
# #         linkurl = scrapy.Field()
#         return item

#     def parse_main_page(self, response):
#         link = response.xpath(
#             "//a[@title='%s']/@href" % u"联系我们").extract_first()
#         #newpage = ""
#         newpage = "http://shop.99114.com/" + "/" + link
#
#         yield scrapy.Request(newpage, callback=self.parse_info_page, dont_filter=True)
#
#         # return ""  # scrapy.Request(page, callback=self.parse_main_page)
#
#     def parse(self, response):
#
#         alllink = response.xpath(
#             "//a[@class='shopname J_MouseEneterLeave J_ShopInfo']")  # .extract()
#         #table = response.xpath('//table[@id="ip_list"]')[0]
#         # trs = table.xpath('//tr')[1:]  # 去掉标题行
#         items = []
#         for link in alllink:
#             item = CpItem()
#             txt = link.xpath("./span/text()").extract_first()
#             txt = txt.replace("\n", "")
#             txt = txt.replace("\t", "")
#             txt = txt.replace(" ", "")
#
#             href = link.xpath("./@href").extract_first()
#             item["linkurl"] = href
#             item["name"] = txt
#             if href not in self.c_Down_Cp:
#                 self.c_Down_Cp[href] = 1
#                 yield scrapy.Request(href, callback=self.parse_main_page, dont_filter=True)
#             # items.append(item)
#         # print 22222222222222, alllink, items
#        # return items

    # def parse_main_page(self, response):
    #     import requests
    #     #         from scrapy.shell import inspect_response
    #     #         inspect_response(response, self)
    #     try:
    #         item = AvItem()
    #         item["title"] = response.xpath("//h3/text()").extract_first()
    #         item["tags"] = response.xpath(
    #             "//span[@class='genre']/a/text()").extract()
    #         item["pic"] = response.xpath(
    #             "//a[@class='bigImage']/img/@src").extract_first()
    #
    #         item["avcode"] = response.xpath(
    #             "//p/span[@style]/text()").extract_first()
    #         item["url"] = response.url
    #
    #         item["pics"] = response.xpath(
    #             "//div[@class='photo-frame']/img/@src").extract()
    #     except Exception as e:
    #         import traceback
    #         traceback.print_exc()
    #         print e
    #         from scrapy.shell import inspect_response
    #         inspect_response(response, self)
    #     import os
    #     try:
    #         os.makedirs("..\\av\\%s" % avcode)
    #     except:
    #         pass
    #     return item
        # link = response.xpath(
        #    "//a[@title='%s']/@href" % u"联系我们").extract_first()
        #newpage = ""
        #newpage = "http://shop.99114.com/" + "/" + link
        #         from scrapy.shell import inspect_response
        #         inspect_response(response, self)
# yield scrapy.Request(newpage, callback=self.parse_info_page,
# dont_filter=True)
# body > div.container > div.row.movie > div.col-md-9.screencap > a
        # return ""  # scrapy.Request(page, callback=self.parse_main_page)
#/html/body/div[5]/div[1]/div[1]/a
    c_Index = 0
    def parse(self, response):
        import json,jsonlines
        self.c_Index+=1
        #         from scrapy.shell import inspect_response
        #         inspect_response(response, self)
        # alllink = response.xpath(
        #     "//a[@class='movie-box']")
        # for link in alllink:
        #     href = link.xpath("@href").extract_first()
        #     yield scrapy.Request(href, callback=self.parse_main_page, dont_filter=True)

       # from scrapy.shell import inspect_response
        #inspect_response(response, self)

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