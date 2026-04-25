from django.shortcuts import render
from assignments.models import About
from blogs.models import Blog, Category

def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True,status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False,status='Published')

    #fetch the about data
    try:
        about = About.objects.get()
    except:
        about = None    
    context = {
        
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
    }
    return render(request, 'home.html',context )