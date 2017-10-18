from __future__ import unicode_literals
from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField()

class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="ninjas")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


# Start
    # python manage.py shell
    # from apps.dojo_ninjas.models import *

# Create 
    # Dojo.objects.create(name="East", city="Tysons Corner", state="VA")
    # Dojo.objects.create(name="Northwest", city="Mountain View", state="WA")
    # Dojo.objects.create(name="Midwest", city="Chicago", state="IL")

# Delete
    # Dojo.objects.get(id=1).delete()
    # Dojo.objects.get(id=2).delete()
    # Dojo.objects.get(id=3).delete()

# Create more
    # DC = Dojo.objects.create(name="DC", city="Tysons Corner", state="VA")
    # Seattle = Dojo.objects.create(name="Seattle", city="Mountain View", state="WA")
    # Chicago = Dojo.objects.create(name="Chicago", city="Chicago", state="IL")

# Create 3 ninjas and add to first dojo
    # Ninja.objects.create(dojo=DC, first_name="Brian", last_name="M")
    # Ninja.objects.create(dojo=DC, first_name="Olu", last_name="O")
    # Ninja.objects.create(dojo=DC, first_name="Jon", last_name="B")

# Create 3 ninjas and add to second dojo
    # Ninja.objects.create(dojo=Seattle, first_name="Nancy", last_name="K")
    # Ninja.objects.create(dojo=Seattle, first_name="Jill", last_name="J")
    # Ninja.objects.create(dojo=Seattle, first_name="Rina", last_name="A")

# Create 3 ninjas and add to third dojo
    # Ninja.objects.create(dojo=Chicago, first_name="Fred", last_name="P")
    # Ninja.objects.create(dojo=Chicago, first_name="Jack", last_name="H")
    # Ninja.objects.create(dojo=Chicago, first_name="Niki", last_name="O")

# Retrieve all ninjas belonging to first and last Dojo
    # Dojo.objects.first().ninjas.all()
    # Dojo.objects.last().ninjas.all()