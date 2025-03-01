from django.urls import path
from user_profile import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login_page, name='login_page'),

]