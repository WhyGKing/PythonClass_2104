# from django.http import HttpResponse
#
# # Create your views here.
#
# def index(request):
#     return HttpResponse("Hello, bookmark app")

from django.shortcuts import render
from django.views.generic import ListView
from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark