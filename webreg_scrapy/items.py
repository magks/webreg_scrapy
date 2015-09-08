# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CourseItem(scrapy.Item):
    courseNumber = scrapy.Field()
    courseName = scrapy.Field()
    sessions = scrapy.Field()
    pass

class SessionItem(scrapy.Item):
    courseCode = scrapy.Field()
    courseType = scrapy.Field()
    section = scrapy.Field()
    units = scrapy.Field()
    instructor = scrapy.Field()
    time = scrapy.Field()
    place = scrapy.Field()
    final = scrapy.Field()
    maximumEnrollmentAllowed = scrapy.Field()
    currentEnrollmentCount = scrapy.Field()
    currentWaitlistCount = scrapy.Field()
    enrollmentRequests = scrapy.Field()
    reservedForNewStudentsCount = scrapy.Field()
    enrollmentRestrictions = scrapy.Field()
    textbookLink = scrapy.Field()
    courseWebsite = scrapy.Field()
    status = scrapy.Field()
    pass

class DepartmentItem(scrapy.Item):
    abbreviation = scrapy.Field()
    name = scrapy.Field()
    pass