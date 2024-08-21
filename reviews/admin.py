from django.contrib import admin

from .models import *

# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["username", "rating"]
    list_filter = ["rating",]

admin.site.register(Review, ReviewAdmin)