from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from .models import CustomUser, Post 
from django import forms
from .forms import CustomUserCreationForm,CustomAuthenticationForm
from .models import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from textblob import TextBlob


def index(request):
    all_posts = Post.objects.all()
    
    
    comments_for_posts = {post.id: Comment.objects.filter(post=post) for post in all_posts}
    
    
    for post in all_posts:
        post.comments = comments_for_posts.get(post.id, [])

    bloggs = {'posts': all_posts}
    return render(request, 'index.html', bloggs)

def my_bloggs(request):
    if request.user.is_authenticated:
        user_posts = Post.objects.filter(author=request.user)
        return render(request, 'my_bloggs.html', {'user_posts': user_posts})
    else:
        return render(request, 'my_bloggs.html')



def logging(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'logging.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(logging)

    else:
        form = CustomUserCreationForm()
        form.fields['username'].help_text = None
        form.fields['password1'].help_text = None
        form.fields['password2'].help_text = None
    return render(request, 'signup.html', {'form': form})

def newPost(request):
    if request.method == 'POST':
        title = request.POST['heading']
        content = request.POST['content']

        if request.user.is_authenticated:
            author = request.user
            analysis = TextBlob(content)
            sentiment = analysis.sentiment.polarity
            
            if sentiment >= 0.05:
                result = "positive"
            elif sentiment <= -0.05:
                result = "negative"
            else:
                result = "neutral"

            
            Post.objects.create(title=title, content=content, author=author, sentiment=result)
            return redirect('index')
        else:
            return redirect('login')
    else:
        return render(request, 'new_post.html')



def post_del(request,id): 
                            
    post= Post.objects.get(pk=id) 
    post.delete() 
    return redirect(my_bloggs)  


def Post_update (request,id): 
    post_up= Post.objects.get(pk=id)  
    return render (request,'update.html',{'post_up' : post_up}) 

def Post_tp_value(request,id):
    if request.method == 'POST':
        title = request.POST['heading']
        content = request.POST['content']
        print("Received POST request")

        if request.user.is_authenticated:
            print("User is authenticated")
            author = request.user
            post=Post.objects.get(pk=id)
            post.author=author
            post.title=title
            post.content=content
            post.save()
            return redirect(my_bloggs)
    return render (request,'update.html')


@login_required
def add_comment(request):
    if request.method == 'POST':
        post_id = request.POST['post_id']
        comment_text = request.POST['comment_text']
        post = Post.objects.get(id=post_id)

        
        Comment.objects.create(post=post, user=request.user, text=comment_text)

    return redirect(index)


def profile (request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

def logout_view(request):
    logout(request)
    return redirect(index)
