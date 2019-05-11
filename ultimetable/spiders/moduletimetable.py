# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector

from ultimetable.items import ModuleTimetable, ModuleTimetableLesson


class ModuleTimetableSpider(scrapy.Spider):
    name = 'module_timetable'
    allowed_domains = ['www.timetable.ul.ie']

    def __init__(self, module_id=None, *args, **kwargs):
        super(ModuleTimetableSpider, self).__init__(*args, **kwargs)
        if module_id is None:
            raise TypeError('module_id is required')
        self.module_id = module_id

    def start_requests(self):
        url = 'https://www.timetable.ul.ie/mod_res.asp'
        yield scrapy.FormRequest(url=url,
                                 formdata={'T1': self.module_id},
                                 callback=self.parse)

    def parse(self, response: scrapy.http.Response):
        days = response.xpath('//tr[2]/td')
        return ModuleTimetable(
            module_id=response.xpath('/html/body/b/h4/text()').get().strip().split(' = ')[1],
            timetable=[list(self.parse_lessons(day)) for day in days],
        )

    @staticmethod
    def parse_lessons(day: Selector):
        lessons = day.xpath('p/font')
        for lesson in lessons:
            elements = [s.strip() for s in lesson.xpath('b/text()').getall()]
            yield ModuleTimetableLesson(
                start_time=elements[0],
                finish_time=elements[1],
                kind=elements[2],
                group=elements[3] or None,
                lecturer=elements[4],
                rooms=elements[5].split(),
                weeks=elements[6][4:],
            )
