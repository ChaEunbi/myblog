from django.views.generic import ListView, DetailView
#from django.shortcuts import render
from blog.models import Post
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
# Create your views here.
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostDV(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'slug', 'content']
    success_url = reverse_lazy('blog:index')
