
from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):

    def validate(self, post_data):
        errors = {}
        for field, value in post_data.iteritems():

            if len(value) < 1:
                errors[field] = "{} field is reqired!".format(field.title())

            if field == "title":
                if not field in errors and len(value) < 5:
                    errors[field] = "{} field must contain more than 5 characters!".format(field.title())

            if field == "description":
                if not field in errors and len(value) < 15:
                    errors[field] = "{} field must contain more than 15 characters!".format(field.title())

            if field == "review":
                if not field in errors and len(value) < 15:
                    errors[field] = "{} field must contain more than 15 characters!".format(field.title())

        return errors


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    added = models.DateTimeField(auto_now_add=True)
    objects = CourseManager()

class Review(models.Model):
    review = models.TextField()
    course = models.ForeignKey(Course, related_name="reviews")
    added = models.DateTimeField(auto_now_add=True)
    objects = CourseManager()