from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def validate_registration(self, post_data):
        errors = {}

        for field, value in post_data.iteritems():
            if not field == "csrfmiddlewaretoken":
                if len(value) < 1:
                    errors[field] = "Error: {} field left empty.".format(field.title())

            if not field in errors:
            
                if field == "name":
                    if len(value) < 2:
                        errors[field] = "Please use at least 2 characters for your name."
                    if not value.replace(' ', '').isalpha(): # account for spaces
                        errors[field] = "Your name should only include letters."

                if field == "alias":
                    if len(value) < 2:
                        errors[field] = "Please use at least 2 characters for your alias."

                if field == "email":
                    if not re.match(email_regex, post_data[field]):
                        errors[field] = "The email address you entered is an invalid format."
                    elif len(self.filter(email = post_data[field])) > 0:
                        errors[field] = "The email address you entered is already in use."

                if field == "password":
                    if len(value) < 8:
                        errors[field] = "Passwords must be at least 8 characters."

                if field == "confirmation":
                    if not value == post_data['password']:
                        errors[field] = "Your password entries do not match."

        return errors

    def validate_login(self, post_data):
        errors = {}

        for field, value in post_data.iteritems():
            if not field == "csrfmiddlewaretoken":

                if field == "email":
                    if len(self.filter(email = post_data[field])) == 0:
                        errors[field] = "Error: Email address not found."

                if field == "password":
                    truepass = self.get(email = post_data['email']).password
                    if not bcrypt.checkpw(post_data[field].encode(), truepass.encode()):
                        errors[field] = "Error: Password invalid."

        return errors


class BookManager(models.Manager):
    def validate_bookreview(self, post_data):
        errors = {}

        for field, value in post_data.iteritems():
            if not field == "csrfmiddlewaretoken":
                
                if field == "title":
                    if len(value) < 2:
                        errors[field] = "Please use at least 2 characters for the book title."
                    if len(Book.objects.filter(title = post_data[field])) > 0:
                        errors[field] = "The book you entered is already in our system!"

                if field == "author":
                    if len(value) < 2:
                        errors[field] = "Please use at least 2 characters for the author's name."

                if field == "review":
                    if len(value) < 30:
                        errors[field] = "Reviews should be at least 30 characters."

                if field == "rating":
                    if int(value) < 1 or int(value) > 5:
                        errors[field] = "Nice try! Ratings can only be 1-5 stars :)"

        return errors


class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    added = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

class Author(models.Model):
    author = models.CharField(max_length=255)
    objects = BookManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="book_author")
    added = models.DateTimeField(auto_now_add=True)
    objects = BookManager()

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="user_reviews")
    book = models.ForeignKey(Book, related_name="book_reviews")
    objects = BookManager()