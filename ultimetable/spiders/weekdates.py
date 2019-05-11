# -*- coding: utf-8 -*-
import scrapy


class WeekDatesSpider(scrapy.Spider):
    name = 'week_dates'
    allowed_domains = ['www.timetable.ul.ie']

    def start_requests(self):
        url = 'https://www.timetable.ul.ie/weeks.htm'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response: scrapy.http.Response):
        weeks = response.xpath('//tr[position() > 1]')
        for week in weeks:
            yield {
                'week_commencing': week.xpath('td[1]/text()').get(),
                'teaching_week': week.xpath('td[2]/text()').get(),
                'week_displayed_on_timetable': week.xpath('td[3]/text()').get(),
            }
