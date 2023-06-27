from django.shortcuts import render, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView


# Create your views here.


def store(request):
    if request.method == 'POST':
        form = AlbumTitleSuggestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alex:suggestion_list')
    else:
        form = AlbumTitleSuggestionForm()
    return render(request, 'WebTest.html', {'form': form})

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def noplant(request):
    return render(request, 'noplant.html')

def typical(request):
    return render(request, 'typical.html')

def exgirl(request):
    return render(request, 'exgirl.html')

def evil(request):
    return render(request, 'evil.html')

def blah(request):
    return render(request, 'blah.html')   

def user_login(request):
    return render(request,  'login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(reverse('alex:login'))
    else:
        login(request, user)
    return HttpResponseRedirect(reverse('alex:WebTest')
)




from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('alex:login'))  # Assuming you have a login page with the name 'login'
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlbumTitleSuggestionForm
from .models import AlbumTitleSuggestion



def suggestion_list(request):
    suggestions = AlbumTitleSuggestion.objects.all()
    return render(request, 'suggestion_list.html', {'suggestions': suggestions})

def vote(request, suggestion_id):
    suggestion = get_object_or_404(AlbumTitleSuggestion, pk=suggestion_id)
    suggestion.votes += 1
    suggestion.save()
    return redirect('alex:suggestion_list')

def blog(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'blog.html', {'posts': posts})

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post.html', {'post': post})

