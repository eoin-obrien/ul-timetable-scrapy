# -*- coding: utf-8 -*-
import scrapy

from ultimetable.items import ModuleDetails


class ModuleDetailsSpider(scrapy.Spider):
    name = 'module_details'
    allowed_domains = ['www.timetable.ul.ie']

    def __init__(self, module_id=None, *args, **kwargs):
        super(ModuleDetailsSpider, self).__init__(*args, **kwargs)
        if module_id is None:
            raise TypeError('module_id is required')
        self.module_id = module_id

    def start_requests(self):
        url = 'https://www.timetable.ul.ie/tt_moduledetails_res.asp'
        yield scrapy.FormRequest(url=url,
                                 formdata={'T1': self.module_id},
                                 callback=self.parse)

    def parse(self, response: scrapy.http.Response):
        details = [s.strip() for s in response.xpath('//td[2]//text()').getall()]
        return ModuleDetails(
            module_id=details[0],
            module_name=details[1],
        )
