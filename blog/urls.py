from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='blog_home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog_about'),
    path('contribute/', views.contribute, name='contribute'),
    path('code/', views.code_of_conduct, name='code_of_conduct'),
    path('team/', views.swifter_team, name='swifter_team'),
    path('bugs/', views.report_bugs, name='report_bugs'),
    path('security/', views.security_issue, name='security'),
    path('join/', views.join_group, name='join_group'),
    path('latest/', views.latest_post, name='latest_post'),
    path('announcements/', views.announcements, name='announcements'),
    path('calendar/', views.calendar, name='calendar'),
    path('search/', views.searchBar, name='search')
]
