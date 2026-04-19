from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from . models import Blog, Category

# Create your views here.
def posts_by_category(request, category_id):
  # fetch the post that belogs to the catogory with the id category_id
  posts = Blog.objects.filter(status= 'Published', category_id=category_id)
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