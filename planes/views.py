from django.shortcuts import render
from .models import Plan
from django.utils import timezone

# Create your views here.

def plan_list(request):
    planes = Plan.objects.all()
    return render(request, 'planes/plan_list.html', {'planes': planes})