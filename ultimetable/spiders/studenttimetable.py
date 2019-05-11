# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector


class StudentTimetableSpider(scrapy.Spider):
    name = 'student_timetable'
    allowed_domains = ['www.timetable.ul.ie']

    def __init__(self, student_id=None, *args, **kwargs):
        super(StudentTimetableSpider, self).__init__(*args, **kwargs)
        if student_id is None:
            raise TypeError('student_id is required')
        self.student_id = student_id

    def start_requests(self):
        url = 'https://www.timetable.ul.ie/tt2.asp'
        yield scrapy.FormRequest(url=url,
                                 formdata={'T1': self.student_id},
                                 callback=self.parse)

    def parse(self, response: scrapy.http.Response):
        days = response.xpath('//tr[2]/td')
        return {
            'student_id': self.student_id,
            'timetable': [list(self.parse_lessons(day)) for day in days],
        }

    @staticmethod
    def parse_lessons(day: Selector):
        lessons = day.xpath('p/font')
        for lesson in lessons:
            elements = [s.strip() for s in lesson.xpath('b/text()').getall()]
            yield {
                'start_time': elements[0],
                'finish_time': elements[1],
                'module': elements[2],
                'kind': elements[3],
                'group': elements[4] or None,
                'rooms': elements[5].split(),
                'weeks': elements[6][4:],
            }
