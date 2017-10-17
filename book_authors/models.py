from __future__ import unicode_literals
from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="authors")
    email = models.EmailField() # normally set unique=True
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Start
    # python manage.py shell
    # from apps.book_authors.models import *

# Create 5 books with the following names: C sharp, Java, Python, PHP, Ruby
    # Book.objects.create(name="C sharp")
    # Book.objects.create(name="Java")
    # Book.objects.create(name="Python")
    # Book.objects.create(name="PHP")
    # Book.objects.create(name="Ruby")

# Create 5 different authors: Mike, Speros, John, Jadee, Jay
    # Author.objects.create(first_name="Mike")
    # Author.objects.create(first_name="Speros")
    # Author.objects.create(first_name="John")
    # Author.objects.create(first_name="Jadee")
    # Author.objects.create(first_name="Jay")

# Add a new field in the authors table called 'notes'.  Make this a TextField. Successfully create and run the migration files.
    # Done.

# Change the name of the 5th book to C#
    # update = Book.objects.get(id=5)
    # update.name = "C#"
    # update.save()

# Change the first_name of the 5th author to Ketul
    # update = Author.objects.get(id=5)
    # update.first_name = "Ketul"
    # update.save()

# Note- Possible to create querysets via multiple .get and add author via for loop?

# Assign the first author to the first 2 books
    # Book.objects.get(id=1).authors.add(Author.objects.get(id=1))
    # Book.objects.get(id=2).authors.add(Author.objects.get(id=1))

# Assign the second author to the first 3 books
    # Book.objects.get(id=1).authors.add(Author.objects.get(id=2))
    # Book.objects.get(id=2).authors.add(Author.objects.get(id=2))
    # Book.objects.get(id=3).authors.add(Author.objects.get(id=2))

# Assign the third author to the first 4 books
    # Book.objects.get(id=1).authors.add(Author.objects.get(id=3))
    # Book.objects.get(id=2).authors.add(Author.objects.get(id=3))
    # Book.objects.get(id=3).authors.add(Author.objects.get(id=3))
    # Book.objects.get(id=4).authors.add(Author.objects.get(id=3))

# Assign the fourth author to the first 5 books (or in other words, all the books)
    # books = Book.objects.all()
    # for book in books:
    #     book.authors.add(Author.objects.get(id=4))

# For the 3rd book, retrieve all the authors
    # for author in Book.objects.get(id=3).authors.all():
    #     print author.first_name

# For the 3rd book, remove the first author
    # Book.objects.get(id=3).authors.first().delete()

# For the 2nd book, add the 5th author as one of the authors
    # Book.objects.get(id=2).authors.add(Author.objects.get(id=5))

# Find all the books that the 3rd author is part of
    # for book in Book.objects.filter(authors=3):
    #     print book.name

# Find all the books that the 2nd author is part of
    # for book in Book.objects.filter(authors=2):
    #     print book.name (none!)