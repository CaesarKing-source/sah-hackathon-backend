from atexit import register
from django.contrib import admin
from home.models import Hackathon
from home.models import Contact


# Register your models here.
admin.site.register(Hackathon)
admin.site.register(Contact)