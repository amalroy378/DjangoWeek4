from django.contrib import admin
from .models import Actor,LatestUpdates

# Register your models here.
admin.site.register(Actor)
admin.site.register(LatestUpdates)