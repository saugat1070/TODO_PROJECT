from django.contrib import admin
from user_profile.models import User
from blog.models import Blog
# Register your models here.
admin.site.register(User)
admin.site.register(Blog)