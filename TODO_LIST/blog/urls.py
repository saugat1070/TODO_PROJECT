from django.urls import path
from blog import views
urlpatterns = [
    path('blog_page/', views.blog_page, name='blog_page'),
    path('blog_page/update/<int:pk>/',views.task_update, name='task_update'),
    path('blog/')

]