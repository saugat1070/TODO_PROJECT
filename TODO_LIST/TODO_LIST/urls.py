
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_profile/',include('user_profile.urls')),
    path('blog/',include('blog.urls'))
]
