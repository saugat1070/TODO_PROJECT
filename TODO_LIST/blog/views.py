from django.shortcuts import render
from blog.models import Blog
from user_profile.models import User
from django.core.cache import cache
from django.shortcuts import redirect
# Create your views here.
def blog_page(request):
    if request.method == "GET":
        if request.session.get('username'):
            user_email = request.session.get('email')
            user_object = User.objects.get(email = user_email)
            tasks = Blog.objects.filter(user = user_object).order_by('-created_at')
            data = {
                'task':tasks,
            }
            cache.set(timeout=5000)
            return render(request,'blog_page.html',context=data)


    if request.method == "POST":
        task = cache.get('tasks')
        title = request.POST.get('title')
        description = request.POST.get('description')
        user_email = cache.get('useremail')
        user_object = User.objects.get(email = user_email)
        task = Blog.objects.create(title = title , description = description, user = user_object)
        return redirect('blog_page.html')
    else:
        return redirect('blog.html')