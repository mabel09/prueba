from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from models import Post
from forms import PostForm

def front(request):
     entries = Post.objects.all().order_by('-date')[:5]
     return render_to_response("blog.html", dict(entries=entries))


def main(request):
     if request.method == 'POST':
          form = PostForm(request.POST)
          if form.is_valid():
               form.save()
               return HttpResponseRedirect('/blog')
     else:
          form = PostForm()
     return render_to_response('main.html', {'form':form})        

