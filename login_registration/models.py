from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    
    def validate(self, post_data):
    
        errors = {}

        for field, value in post_data.iteritems():

            if not field == "csrfmiddlewaretoken":
                if len(value) < 1:
                    errors[field] = "Error: {} field left empty.".format(field.replace('_', ' '))

            if not field in errors:
            
                if field == "first_name":
                    if len(value) < 2:
                        errors[field] = "Your first name must be at least 2 characters."
                    if not value.isalpha():
                        errors[field] = "Your first name should only include letters."

                if field == "last_name":
                    if len(value) < 2:
                        errors[field] = "Your last name must be at least 2 characters."
                    if not value.isalpha():
                        errors[field] = "Your last name should only include letters."

                if field == "email_address":
                    if not re.match(email_regex, post_data[field]):
                        errors[field] = "Your email address format is invalid."
                    elif len(self.filter(email_address = post_data[field])) > 0: # test this
                        errors[field] = "Your email address is already in use."

                if field == "password":
                    if len(value) < 8:
                        errors[field] = "Your password must be at least 8 characters."

                if field == "password_confirmation":
                    if not value == post_data['password']:
                        errors[field] = "Your password entries do not match."

                if field == "login_email":
                    if len(self.filter(email_address = post_data['login_email'])) == 0:
                        errors[field] = "Your email address is not registered in our database."

                if field == "login_password":
                    truepass = self.get(email_address = post_data['login_email']).password
                    if not bcrypt.checkpw(post_data[field].encode(), truepass.encode()):
                        errors[field] = "You have entered an invalid password."

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    objects = UserManager()