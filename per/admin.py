from django.contrib import admin
from .models import post
from .models import about

admin.site.register(post)
admin.site.register(about)
