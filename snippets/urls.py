from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('snippets/', views.SnippetList.as_view(), name='snippet_list'),
    path('snippets/<int:pk>', views.SnippetDetail.as_view(), name='snippet_detail'),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail')
]
