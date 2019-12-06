from django.shortcuts import render, render_to_response

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render_to_response("index.html")
def inbox(request):
    return render_to_response("page_inbox.html")
    #return HttpResponse("Hello, world. You're at the polls index.")