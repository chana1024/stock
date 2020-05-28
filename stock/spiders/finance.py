# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.http import HtmlResponse
from stock.mysql import mysqldb


class FinanceSpider(scrapy.Spider):
    name = 'finance'
    allowed_domains = ['10jqka.com.cn']
    start_urls = ['http://basic.10jqka.com.cn/api/stock/finance/300800_benefit.json']
    # mysqldb.query('select * from ss limit 3')

    def parse(self, response: HtmlResponse):
        print(response.text)
        dic = json.loads(response.text)
        flash_data = json.loads(dic['flashData'])
        stock_finance_batch = list()
        for i in range(0, 4):
            stock_finance = list()
            stock_finance.append('300800')
            stock_finance.append(flash_data['report'][00][i])
            stock_finance.append(flash_data['report'][22][i])
            # stock_finance.append(flash_data['report'][26][i])
            stock_finance.append('report2')
            stock_finance_batch.append(stock_finance)

        for i in range(0, 4):
            stock_finance = list()
            stock_finance.append('300800')
            stock_finance.append(flash_data['year'][00][i])
            stock_finance.append(flash_data['year'][22][i])
            # stock_finance.append(flash_data['year'][26][i])
            stock_finance.append('year')
            stock_finance_batch.append(stock_finance)
        mysqldb.execute_batch("replace into stockFinance(stock_code, term, income_tax,type) values(%s, %s, %s, %s)", stock_finance_batch)
        pass
