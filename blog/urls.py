from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.UpdatePostView.as_view(), name='post_edit'),
    path('post/<int:pk>/remove/', views.DeletePostView.as_view(), name='post_remove'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('post/<int:pk>/comment_approved/', views.comments_Approved, name='comments_Approved'),
    path('post/<int:pk>/comment_removed/', views.comments_Removed, name='comments_Removed'),
    path('post/<int:pk>/publish/', views.publish_post, name="publish_post"),
]

