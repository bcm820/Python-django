from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField() # normally unique=True
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploader = models.ForeignKey(User, related_name="uploads")
    liked_by = models.ManyToManyField(User, related_name="likes")



# Create 3 different user accounts
    # User.objects.create(first_name="John", last_name="Wick", email="john@wick.com")
    # User.objects.create(first_name="Jack", last_name="Bauer", email="jack@bauer.com")
    # User.objects.create(first_name="Jackie", last_name="Chan", email="jackie@chan.com")

# Have the first user upload 2 books.
    # Book.objects.create(name="John's book 1", uploader=(User.objects.get(id=1)))
    # Book.objects.create(name="John's book 2", uploader=(User.objects.get(id=1)))

# Have the second user upload 2 other books.
    # Book.objects.create(name="Jack's book 1", uploader=(User.objects.get(id=2)))
    # Book.objects.create(name="Jack's book 2", uploader=(User.objects.get(id=2)))

# Have the third user upload 2 other books.
    # Book.objects.create(name="Jackie's book 1", uploader=(User.objects.get(id=3)))
    # Book.objects.create(name="Jackie's book 2", uploader=(User.objects.get(id=3)))

# Have the first user like the last book and the first book
    # Book.objects.last().liked_by.add(User.objects.get(id=1))
    # Book.objects.last().liked_by.add(User.objects.get(id=1))

# Have the second user like the first book and the third book
    # Book.objects.first().liked_by.add(User.objects.get(id=2))
    # Book.objects.get(id=3).liked_by.add(User.objects.get(id=2))

# Have the third user like all books
    # for book in Book.objects.all():
    #     book.liked_by.add(User.objects.get(id=3))

# Display all users who like the first book
    # users = Book.objects.first().liked_by.all()
    # for user in users:
    #     print user.first_name, user.last_name

# Display the user who uploaded the first book
    # Book.objects.first().uploader

# Display all users who like the second book
    # users = Book.objects.get(id=2).liked_by.all()
    # for user in users:
    #     print user.first_name, user.last_name

# Display the user who uploaded the second book
    # Book.objects.get(id=2).uploader
