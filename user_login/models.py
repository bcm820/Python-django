from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# User.objects.all()

# User.objects.last()

# User.objects.create(first_name='Brian', last_name='M', email_address='bcm@codingdojo.com', age='33')
# User.objects.create(first_name='Jon', last_name='B', email_address='jon@codingdojo.com', age='30')
# User.objects.create(first_name='Olu', last_name='O', email_address='olu@codingdojo.com', age='31')
# User.objects.create(first_name='Eduardo', last_name='M', email_address='ed@codingdojo.com', age='21')

# User.objects.first()

# User.objects.all().order_by('-first_name')

# change = User.objects.get(id=3)
# change.last_name = "Different"
# change.save()
# User.objects.get(id=3).last_name

# User.objects.get(id=4).delete()