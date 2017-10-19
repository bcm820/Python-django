from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.messages import error
from .models import *
import bcrypt
import arrow


# GET

def index(request): # Index page with login & registration
    return render(request, 'bookreview/index.html')

def add(request): # Form to add new book with review
    if not 'user' in request.session:
        error(request, "You must login to access our reviews.")
        return redirect('/bookreview/')

    data = {
        "authors": Author.objects.all(),
        "books": Book.objects.all()
    }

    return render(request, 'bookreview/add.html', data)

def show_book(request, id): # Single book info & review page
    if not 'user' in request.session:
        error(request, "You must login to access our reviews.")
        return redirect('/bookreview/')

    data = {
        "book": Book.objects.get(id=id),
        "reviews": Book.objects.get(id=id).book_reviews.all()
    }

    return render(request, 'bookreview/show.html', data)



### NOT YET

def show_user(request, id):
    if not 'user' in request.session:
        error(request, "You must login to access our reviews.")
        return redirect('/bookreview/')



    return redirect('/bookreview/')


### UPDATE LATER with links to individual pages

def main(request):
    if not 'user' in request.session:
        error(request, "You must login to view your information.")
        return redirect('/bookreview/')

    data = {
        "user": User.objects.get(email=request.session['user']),
        "recent": Review.objects.order_by("-id")[:3],
        "books": Book.objects.order_by("-book_reviews")[4:]
    }
    
    return render(request, 'bookreview/main.html', data)




# POSTS


def new(request):
    
    errors_book = Book.objects.validate_bookreview(request.POST)
    errors_review = Review.objects.validate_bookreview(request.POST)

    if len(errors_book):
        for field, message in errors_book.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/bookreview/books/add/')

    elif len(errors_review):
        for field, message in errors_review.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/bookreview/books/add/')

    else:
        if len(Author.objects.filter(author = request.POST["author"])) < 1:
            Author.objects.create(author = request.POST["author"])
        
        Book.objects.create(
            title = request.POST["title"],
            author = Author.objects.get(author=request.POST["author"])
        )

        Review.objects.create(
            user = User.objects.get(email=request.session["user"]),
            book = Book.objects.last(),
            review = request.POST["review"],
            rating = int(request.POST["rating"])
        )

        book_id = str(Book.objects.get(title=request.POST["title"]).id)
        
        return redirect('/bookreview/books/' + book_id)


def review(request, id):

    errors = Review.objects.validate_bookreview(request.POST)

    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/bookreview/books/' + id)

    else:
        Review.objects.create(
            user = User.objects.get(email=request.session["user"]),
            book = Book.objects.get(id=id),
            review = request.POST["review"],
            rating = int(request.POST["rating"])
        )
        
        return redirect('/bookreview/books/' + id)


def register(request):

    errors = User.objects.validate_registration(request.POST)

    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/bookreview/')

    else:
        User.objects.create(
            name = request.POST["name"],
            alias = request.POST["alias"],
            email = request.POST["email"],
            password = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt())
        )

        request.session['user'] = request.POST["email"]

        return redirect('/bookreview/books/')


def login(request):

    errors = User.objects.validate_login(request.POST)

    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/bookreview/')

    else:
        request.session['user'] = request.POST["email"]

        return redirect('/bookreview/books/')


def logout(request):
    request.session.flush()
    error(request, "You have successfully ended your session. Thank you!")
    return redirect('/bookreview/')
