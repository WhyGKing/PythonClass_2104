from django.urls import path
from .views import BookmarkListView

urlpatterns = [
    # path('', views.index, name='index'),
    path('',BookmarkListView.as_view(), name='list'),
]