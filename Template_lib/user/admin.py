from django.contrib import admin
from . models import UserAccount,publisherInfo
# Register your models here.

admin.site.register(UserAccount)
admin.site.register(publisherInfo)
