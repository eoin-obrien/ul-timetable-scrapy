# -*- coding: utf-8 -*-
import scrapy

from ultimetable.items import ModuleTimetableLesson


class TimetableSpider(scrapy.Spider):
    name = 'timetable'
    allowed_domains = ['bookofmodules.ul.ie', 'www.timetable.ul.ie']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def start_requests(self):
        url = 'https://bookofmodules.ul.ie/'
        yield scrapy.Request(url=url, callback=self.parse_book_of_modules)

    def parse(self, response: scrapy.http.Response):
        module_id = response.xpath('/html/body/b/h4/text()').get().strip().split(' = ')[1]
        days = response.xpath('//tr[2]/td')
        for idx, day in enumerate(days):
            lessons = day.xpath('p/font')
            for lesson in lessons:
                elements = [s.strip() for s in lesson.xpath('b/text()').getall()]
                yield ModuleTimetableLesson(
                    module_id=module_id,
                    day_id=idx,
                    start_time=elements[0],
                    finish_time=elements[1],
                    kind=elements[2],
                    group=elements[3] or None,
                    lecturer=elements[4],
                    rooms=elements[5].split(),
                    weeks=elements[6][4:],
                )

    def parse_book_of_modules(self, response: scrapy.http.Response):
        url = 'https://www.timetable.ul.ie/mod_res.asp'
        drop_down_xpath = '//*[@id="ctl00_MasterContentPlaceHolder_ModuleDropDown"]/option[position() > 1]/text()'
        module_ids = [title[:6] for title in response.xpath(drop_down_xpath).getall()]
        for module_id in module_ids:
            yield scrapy.FormRequest(url=url,
                                     formdata={'T1': module_id},
                                     callback=self.parse)
