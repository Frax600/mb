from django.contrib import admin

# Register your models here.
from django.contrib import admin

from posts.models import Post # new

admin.site.register(Post)     # new
