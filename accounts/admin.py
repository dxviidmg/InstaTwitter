from django.contrib import admin
from .models import *

admin.site.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
	list_display = ['id','user']

admin.site.register(Contact)