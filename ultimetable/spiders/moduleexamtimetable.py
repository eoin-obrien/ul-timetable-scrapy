# -*- coding: utf-8 -*-
import scrapy


class ModuleExamTimetableSpider(scrapy.Spider):
    name = 'module_exam_timetable'
    allowed_domains = ['www.timetable.ul.ie']

    def __init__(self, module_id=None, *args, **kwargs):
        super(ModuleExamTimetableSpider, self).__init__(*args, **kwargs)
        if module_id is None:
            raise TypeError('module_id is required')
        self.module_id = module_id

    def start_requests(self):
        url = 'https://www.timetable.ul.ie/mod_exam_res.asp'
        yield scrapy.FormRequest(url=url,
                                 formdata={'T1': self.module_id},
                                 callback=self.parse)

    def parse(self, response: scrapy.http.Response):
        details = [s.strip() for s in response.xpath('//td[2]/b/font/text()').getall()]
        return {
            'module_id': details[0],
            'module_name': details[1],
            'date': details[2],
            'day': details[3],
            'building': details[4],
            'location': details[5],
            'time': details[6],
            'other_information': details[7] or None,
        }
