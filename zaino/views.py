from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World!")