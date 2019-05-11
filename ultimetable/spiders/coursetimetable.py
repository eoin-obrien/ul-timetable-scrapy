# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector

from ultimetable.items import CourseTimetable, CourseTimetableLesson


class CourseTimetableSpider(scrapy.Spider):
    name = 'course_timetable'
    allowed_domains = ['www.timetable.ul.ie']

    def __init__(self, course_id=None, year=None, *args, **kwargs):
        super(CourseTimetableSpider, self).__init__(*args, **kwargs)
        if course_id is None:
            raise TypeError('course_id is required')
        if year is None:
            raise TypeError('year is required')
        self.course_id = course_id
        self.year = year

    def start_requests(self):
        url = 'https://www.timetable.ul.ie/course_res.asp'
        yield scrapy.FormRequest(url=url,
                                 formdata={'T1': self.course_id, 'T2': self.year},
                                 callback=self.parse)

    def parse(self, response: scrapy.http.Response):
        header = response.xpath('/html/body/b/h4/text()').get().strip()
        days = response.xpath('//tr[2]/td')
        return CourseTimetable(
            course_id=header.split()[2],
            year=header.split()[5],
            timetable=[list(self.parse_lessons(day)) for day in days],
        )

    @staticmethod
    def parse_lessons(day: Selector):
        lessons = day.xpath('p/font')
        for lesson in lessons:
            elements = [s.strip() for s in lesson.xpath('b/text()').getall()]
            yield CourseTimetableLesson(
                start_time=elements[0],
                finish_time=elements[1],
                module_id=elements[2],
                kind=elements[3],
                group=elements[4] or None,
                lecturer=elements[5],
                rooms=elements[6].split(),
                weeks=elements[7][4:],
            )
