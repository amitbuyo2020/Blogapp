from django.shortcuts import render, get_object_or_404
from .models import Post, Announcements, Calendar
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html')

def join_group(request):
    return render(request, 'blog/join_group.html')

def contribute(request):
    return render(request, 'blog/contribute.html')

def report_bugs(request):
    return render(request, 'blog/report_bugs.html')

def security_issue(request):
    return render(request, 'blog/security.html')

def swifter_team(request):
    return render(request, 'blog/swifter_team.html')

def code_of_conduct(request):
    return render(request, 'blog/code_of_conduct.html')


def latest_post(request):
    context = {
    'posts': Post.objects.all()
    }
    return render(request, 'blog/latest_post.html', {'title':'Latest Post', 'context': context})

def announcements(request):
    context = {
        'announcements': Announcements.objects.all()
    }
    return render(request, 'blog/announcements.html', context)

def calendar(request):
    context = {
    'calendar':Calendar.objects.all()
    }
    return render(request, 'blog/calendar.html', context)

def searchBar(request):
    if request.method == "GET":
        query = request.GET.get('q')
        sub_btn = request.GET.get('submit')

        if query is not None:
            lookups = Q(title__icontains=query)
            results = Post.objects.filter(lookups).distinct()
            context = {
                'results': results,
                'sub_btn': sub_btn
            }
            return render(request, 'blog/search_results.html', context)

        else:
            return render(request, 'blog/search_results.html')
    else:
        return render(request, 'blog/home.html')
