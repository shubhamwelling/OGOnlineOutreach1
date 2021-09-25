from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

from .forms import CommentForm, FeedbackForm
from .models import Post, FAQ, Events, Feedback


def results(request):
 if request.user.is_superuser:
    results=Feedback.objects.all()

    return render(request, 'blog/results.html', {'results':results})
 if not request.user.is_superuser:
        return HttpResponse('You are not allowed to view this site')

def feedback(request):
    form=FeedbackForm()
    if request.method=="POST":
        form=FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'blog/success.html')


    context={'form':form}
    return render(request, 'blog/feedback.html',context)

def search(request):
    if request.method=='POST':
        searched = request.POST['searched']
        posts=Post.objects.filter(title__contains=searched)

        return render(request, 'blog/search.html', {'searched':searched, 'posts':posts})
    else:
        return render(request, 'blog/search.html')

def suggestions(request):
 if request.user.is_superuser:
    list = []
    if request.method=='POST':
        suggestion=request.POST['suggestion']
        list.append(suggestion)
        return render(request,'blog/suggestions.html',{'suggestion':suggestion, 'list':list})
    else:
        return render(request,'blog/suggestions.html')

 if not request.user.is_superuser:
        return HttpResponse('Access Denied')


def second(request):
    return render(request,'blog/redirect.html')

def home(request):
    return render(request,'blog/home.html')


def index(request):
   if request.method == 'POST':
        personname=request.POST['personname']
        email=request.POST['email']
        message = request.POST['message']
        send_mail('ContactForm',"Name: "+personname + "\nEmail: " + email+ "\nMessage:"+message, settings.EMAIL_HOST_USER, ['ogonlineoutreach@outlook.com'],fail_silently=False)

   return render(request, 'blog/index.html')

def frontpage(request):
    posts = Post.objects.all()

    return render(request, 'blog/frontpage.html', {'posts': posts})

def faq(request):
    faqs=FAQ.objects.all()

    return render(request, 'blog/faq.html', {'faqs':faqs})

def events(request):
    events=Events.objects.all()

    return render(request, 'blog/events.html', {'events':events})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()


    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})






