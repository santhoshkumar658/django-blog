from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from . models import Blog, Category, Comment
from django.db.models import Q

# Create your views here.
def posts_by_category(request, category_id):
  # fetch the post that belogs to the catogory with the id category_id
  posts = Blog.objects.filter(
    status='Published',
    category_id=category_id,
  ).exclude(slug='')
  # use try/except when we wnt to some custom action if the object is not found, for example redirect the user to homepage
  try:
    category = Category.objects.get(id=category_id)
  except:
    # redirect the user to homepage
    return redirect('home')
  # use get_object_or_404 when you wnat to show 404 error page when the object is not found

  #category = get_object_or_404(Category, pk = category_id)
  context = {
    'posts': posts,
    'category': category,
  }
  return render(request, 'posts_by_category.html', context) 


def blogs(request, slug):
  single_blog = get_object_or_404(Blog, slug=slug, status='Published')
  if request.method == 'POST':
    comment = Comment()
    comment.user = request.user
    comment.blog = single_blog
    comment.comment = request.POST['comment']
    comment.save()
    return redirect('blogs', slug=slug)

  #comments 
  comments = Comment.objects.filter(blog=single_blog)
  comment_count = comments.count()
 
  context = {
    'single_blog': single_blog,
    'comments': comments,
    'comment_count': comment_count,
  }
  return render(request, 'blogs.html', context)

def search(request):
  keyword = (request.GET.get('keyword') or '').strip()
  blogs = Blog.objects.filter(status='Published').exclude(slug='')
  if keyword:
    blogs = blogs.filter(
      Q(title__icontains=keyword) |
      Q(short_description__icontains=keyword) |
      Q(blog_body__icontains=keyword)
    )
  else:
    blogs = blogs.none()
  context= {
    'blogs': blogs,
    'keyword':keyword,
  }
  return render(request, 'search.html',context)
