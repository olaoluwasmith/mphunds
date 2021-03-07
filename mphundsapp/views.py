from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.db.models import Q, signals
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')