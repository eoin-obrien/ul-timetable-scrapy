# -*- coding: utf-8 -*-
import scrapy

from ultimetable.items import RoomTimetableLesson


class RoomTimetableSpider(scrapy.Spider):
    name = 'room_timetable'
    allowed_domains = ['www.timetable.ul.ie']

    def __init__(self, room_id=None, *args, **kwargs):
        super(RoomTimetableSpider, self).__init__(*args, **kwargs)
        if room_id is None:
            raise TypeError('room_id is required')
        self.room_id = room_id

    def start_requests(self):
        url = 'https://www.timetable.ul.ie/room_res.asp'
        yield scrapy.FormRequest(url=url,
                                 formdata={'T1': self.room_id},
                                 callback=self.parse)

    def parse(self, response: scrapy.http.Response):
        room_id = response.xpath('/html/body/b/text()').get().strip()[6:]
        days = response.xpath('//tr[2]/td')
        for idx, day in enumerate(days):
            lessons = day.xpath('p/font')
            for lesson in lessons:
                elements = [s.strip() for s in lesson.xpath('b/text()').getall()]
                yield RoomTimetableLesson(
                    room_id=room_id,
                    day_id=idx,
                    start_time=elements[0],
                    finish_time=elements[1],
                    module_ids=elements[2].split() if elements[2] else None,
                    kind=elements[3],
                    group=elements[4] or None,
                    size=elements[5][7:],
                    lecturer=elements[6] or None,
                    weeks=elements[7][4:],
                )
