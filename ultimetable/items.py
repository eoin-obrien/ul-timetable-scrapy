# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CourseTimetable(scrapy.Item):
    course_id = scrapy.Field()
    year = scrapy.Field()
    timetable = scrapy.Field()


class CourseTimetableLesson(scrapy.Item):
    start_time = scrapy.Field()
    finish_time = scrapy.Field()
    module_id = scrapy.Field()
    kind = scrapy.Field()
    group = scrapy.Field()
    lecturer = scrapy.Field()
    rooms = scrapy.Field()
    weeks = scrapy.Field()


class ModuleTimetable(scrapy.Item):
    module_id = scrapy.Field()
    timetable = scrapy.Field()


class ModuleTimetableLesson(scrapy.Item):
    start_time = scrapy.Field()
    finish_time = scrapy.Field()
    kind = scrapy.Field()
    group = scrapy.Field()
    lecturer = scrapy.Field()
    rooms = scrapy.Field()
    weeks = scrapy.Field()


class RoomTimetable(scrapy.Item):
    room_id = scrapy.Field()
    timetable = scrapy.Field()


class RoomTimetableLesson(scrapy.Item):
    start_time = scrapy.Field()
    finish_time = scrapy.Field()
    module_ids = scrapy.Field()
    kind = scrapy.Field()
    group = scrapy.Field()
    size = scrapy.Field()
    lecturer = scrapy.Field()
    weeks = scrapy.Field()


class StudentTimetable(scrapy.Item):
    student_id = scrapy.Field()
    timetable = scrapy.Field()


class StudentTimetableLesson(scrapy.Item):
    start_time = scrapy.Field()
    finish_time = scrapy.Field()
    module = scrapy.Field()
    kind = scrapy.Field()
    group = scrapy.Field()
    rooms = scrapy.Field()
    weeks = scrapy.Field()


class ModuleExamTimetable(scrapy.Item):
    module_id = scrapy.Field()
    module_name = scrapy.Field()
    date = scrapy.Field()
    day = scrapy.Field()
    building = scrapy.Field()
    location = scrapy.Field()
    time = scrapy.Field()
    other_information = scrapy.Field()


class StudentExamTimetable(scrapy.Item):
    student_id = scrapy.Field()
    timetable = scrapy.Field()


class ModuleDetails(scrapy.Item):
    module_id = scrapy.Field()
    module_name = scrapy.Field()


class WeekDate(scrapy.Item):
    week_commencing = scrapy.Field()
    teaching_week = scrapy.Field()
    week_displayed_on_timetable = scrapy.Field()
