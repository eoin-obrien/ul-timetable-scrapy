# -*- coding: utf-8 -*-
import scrapy

from ultimetable.items import StudentExamTimetableModule


class StudentExamTimetableSpider(scrapy.Spider):
    name = 'student_exam_timetable'
    allowed_domains = ['www.timetable.ul.ie']

    def __init__(self, student_id=None, *args, **kwargs):
        super(StudentExamTimetableSpider, self).__init__(*args, **kwargs)
        if student_id is None:
            raise TypeError('student_id is required')
        self.student_id = student_id

    def start_requests(self):
        url = 'https://www.timetable.ul.ie/stud_exam_res.asp'
        yield scrapy.FormRequest(url=url,
                                 formdata={'T1': self.student_id},
                                 callback=self.parse)

    def parse(self, response: scrapy.http.Response):
        student_id = response.xpath('/html/body/h4/text()').get().split('=')[1].strip()
        modules = response.xpath('//div/center/table')
        for module in modules:
            details = [s.strip() for s in module.xpath('tr/td[2]/b/font/text()').getall()]
            return StudentExamTimetableModule(
                student_id=student_id,
                module_id=details[0],
                module_name=details[1],
                date=details[2],
                day=details[3],
                building=details[4],
                location=details[5],
                time=details[6],
                other_information=details[7] or None,
            )
