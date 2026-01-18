from django.urls import path

from blog_app import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="post-list"),
    path("post-detail/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path('draft-list/', views.DraftListView.as_view(), name="draft-list"),
    path('draft-details/<int:pk>/', views.DraftDetailView.as_view(), name="draft-detail"),
    path("draft-publish/<int:pk>/", views.DraftPubishedView.as_view(), name="draft-publish"),
    path("post-delete/<int:pk>", views.PostDelete.as_view(), name="post-delete"),
    path("post-create", views.PostCreateView.as_view(), name="post-create"),
    path("post-update/<int:pk>", views.PostUpdate.as_view(), name="post-update"),
]