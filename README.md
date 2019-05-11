# UL Timetable Scraper

A collection of web spiders for the University of Limerick's timetable, built with [Scrapy][scrapy].

## Getting Started

The project is compatible with Python 2.7 and Python 3.6 or greater.

Install Scrapy and its dependencies by following the [installation guide][scrapy-install].

Install additional requirements from `requirements.txt`.

```bash
$ pip install -r requirements.txt
```

## Storing Crawled Data

Scrapy supports several formats for storing crawled data.

### JSON

```bash
$ scrapy crawl timetable -o timetable.json
```

### JSON Lines

```bash
$ scrapy crawl timetable -o timetable.jl
```

### CSV

```bash
$ scrapy crawl timetable -o timetable.csv
```

### XML

```bash
$ scrapy crawl timetable -o timetable.xml
```

## Available Web Spiders

### Student Timetable

Crawls a student's timetable using their student ID number (7-8 digits).

```bash
$ scrapy crawl student_timetable -a student_id=[student_id]
```

### Course Timetable

Crawls the full timetable for a specific year (1-4) of a course (LM code).

```bash
$ scrapy crawl course_timetable -a course_id=[course_id] -a year=[year]
```

### Module Timetable

Crawls the full timetable for a specific module (2 letters followed by 4 digits).

```bash
$ scrapy crawl module_timetable -a module_id=[module_id]
```

### Room Timetable

Crawls the full timetable for a specific room (building code followed by floor and room number)

```bash
$ scrapy crawl room_timetable -a room_id=[room_id]
```

### Student Exam Timetable

Crawls a student's exam timetable, consisting of module exam timetables.
May not be available until late in the semester.

```bash
$ scrapy crawl student_exam_timetable -a student_id=[student_id]
```

### Module Exam Timetable

Crawls the exam timetable for a specific module.
May not be available until late in the semester.

```bash
$ scrapy crawl module_exam_timetable -a module_id=[module_id]
```

### Module Details

Crawls the details of a specific module.

```bash
$ scrapy crawl module_details -a module_id=[module_id]
```

### Week Dates

Crawls the week dates and details for the current semester.

```bash
$ scrapy crawl week_dates
```

### Complete Timetable

Crawls the collective timetables of every module offered by the University of Limerick
as enumerated in the [Book of Modules][book-of-modules].

```bash
$ scrapy crawl timetable
```

[scrapy]: https://scrapy.org/
[scrapy-install]: https://doc.scrapy.org/en/latest/intro/install.html
[book-of-modules]: https://bookofmodules.ul.ie/
